import os
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# MongoDB Connection String - Default to local if not provided
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGODB_URL)
db = client.financial_analyzer

async def save_analysis_status(task_id: str, query: str, filename: str, status: str = "PENDING"):
    """Saves or updates the initial status of an analysis task"""
    await db.results.update_one(
        {"task_id": task_id},
        {
            "$set": {
                "query": query,
                "filename": filename,
                "status": status,
                "created_at": datetime.utcnow()
            }
        },
        upsert=True
    )

async def update_analysis_result(task_id: str, result: str, status: str = "COMPLETED"):
    """Updates the analysis task with the final result"""
    await db.results.update_one(
        {"task_id": task_id},
        {
            "$set": {
                "result": result,
                "status": status,
                "completed_at": datetime.utcnow()
            }
        }
    )

async def get_analysis_by_id(task_id: str):
    """Retrieves an analysis record by its task ID"""
    return await db.results.find_one({"task_id": task_id}, {"_id": 0})
