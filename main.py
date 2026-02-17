from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Response
import os
import uuid
import asyncio

from crewai import Crew, Process
from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from task import analyze_financial_document, investment_analysis, risk_assessment, verification
from database import save_analysis_status, update_analysis_result, get_analysis_by_id
from fastapi import BackgroundTasks

app = FastAPI(title="Financial Document Analyzer")

async def run_crew_task(task_id: str, query: str, file_path: str):
    """Background task to run the crew and update the database"""
    try:
        financial_crew = Crew(
            agents=[verifier, financial_analyst, investment_advisor, risk_assessor],
            tasks=[verification, analyze_financial_document, investment_analysis, risk_assessment],
            process=Process.sequential,
            verbose=True
        )
        
        result = financial_crew.kickoff(inputs={'query': query, 'file_path': file_path})
        await update_analysis_result(task_id, str(result))
    except Exception as e:
        await update_analysis_result(task_id, f"Error: {str(e)}", status="FAILED")
    finally:
        # Cleanup file after processing
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Financial Document Analyzer API is running"}

@app.get("/favicon.ico")
async def favicon():
    """Handle favicon requests to avoid 404 logs"""
    return Response(status_code=204)

@app.post("/analyze")
async def analyze_document_endpoint(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    query: str = Form(default="Analyze this financial document for investment insights")
):
    """Analyze financial document in the background and return a task ID"""
    
    task_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{task_id}.pdf"
    
    try:
        os.makedirs("data", exist_ok=True)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Save initial status to MongoDB
        await save_analysis_status(task_id, query, file.filename)
        
        # Dispatch background task
        background_tasks.add_task(run_crew_task, task_id, query.strip(), file_path)
        
        return {
            "status": "processing",
            "task_id": task_id,
            "message": "Analysis started. Check status using the /status endpoint."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error starting analysis: {str(e)}")

@app.get("/status/{task_id}")
async def get_status(task_id: str):
    """Get the status and result of an analysis task from MongoDB"""
    record = await get_analysis_by_id(task_id)
    if not record:
        raise HTTPException(status_code=404, detail="Task ID not found")
    return record

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)