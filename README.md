# Financial Document Analyzer - Debug Assignment

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.

## Getting Started

### Install Required Libraries
```sh
pip install -r requirement.txt
```

### Sample Document
The system analyzes financial documents like Tesla's Q2 2025 financial update.

**To add Tesla's financial document:**
1. Download the Tesla Q2 2025 update from: https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf
2. Save it as `data/sample.pdf` in the project directory
3. Or upload any financial PDF through the API endpoint

### Installation Setup Guide
**Prerequisites:** Python 3.10+, MongoDB, openrouter API Key.
1.  **Clone Repository:** `git clone <repo_url>`
2.  **Create Virtual Env:** `python -m venv venv`
3.  **Activate Env:** `source venv/bin/activate` or `venv\Scripts\activate` (Windows)
4.  **Install Dependencies:** `pip install -r requirements.txt`

### Configuration Steps
1.  Create a `.env` file in the root directory.
2.  Add keys:
    ```env
    Openrouter_API_KEY=your_Openrouter_api_key
    MONGODB_URL=mongodb://localhost:27017
    Tavliy_API_KEY=your_search_api_key
    ```
3.  Ensure MongoDB is running locally or provide a connection string.

### User Manual (How to Use)
1.  **Start Server:** `uvicorn main:app --reload`
2.  **Access Docs:** Go to `http://localhost:8000/docs`.
3.  **Upload:** Use the **POST /analyze** endpoint. Upload a PDF and provide a query (e.g., "Summarize Q3 performance").
4.  **Get ID:** Copy the returned `task_id`.
5.  **Check Status:** Use **GET /status/{task_id}** to see the result.

### Troubleshooting
*   **Error: Connection Refused:** Check if MongoDB is running.
*   **Error: API Key Invalid:** Verify `.env` file formatting.
*   **Stuck in Processing:** Check server logs for CrewAI loop errors or rate limits.

---

## 7. Performance & Success Metrics

### KPIs
*   **Processing Time:** Average time to analyze a 20-page PDF (Target: < 2 minutes).
*   **Accuracy:** User rating of investment recommendation relevance.
*   **Availability:** API uptime (Target: 99.9%).

### Expected Outcomes
*   80% reduction in time spent on initial document screening.
*   Standardized analysis format across all documents.

---
