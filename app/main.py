from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from app.utils import calculate_uptime_downtime

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Restaurant Monitoring System</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f4f4f4; text-align: center; padding: 50px; }
                h1 { color: #333; }
                p { font-size: 18px; color: #666; }
                a { text-decoration: none; color: #007BFF; }
            </style>
        </head>
        <body>
            <h1>Welcome to the Restaurant Monitoring System!</h1>
            <p>Your one-stop solution for monitoring store statuses, business hours, and more.</p>
            <p>To trigger a report, use the <a href="/docs">API Documentation</a>.</p>
        </body>
    </html>
    """

@app.post("/trigger_report", response_class=HTMLResponse)
def trigger_report(store_id: str, start_date: str, end_date: str, background_tasks: BackgroundTasks):
    # Generate a unique report ID
    report_id = f"report_{store_id}_{start_date}_{end_date}"
    
    # Background task for report generation
    background_tasks.add_task(calculate_uptime_downtime, store_id, start_date, end_date)

    return HTMLResponse(content=f"<html><body><h2>Report Triggered</h2><p>Report ID: {report_id}</p></body></html>")

from fastapi import Depends
from app.database import get_db  # Import your database connection function

@app.get("/get_report/{report_id}", response_class=HTMLResponse)
def get_report(report_id: str, db=Depends(get_db)):
    # Fetch the report from the database
    report = db.reports.find_one({"report_id": report_id})  # Adjust as necessary

    if report:
        # Return the report details in HTML format
        report_status = report.get("status", "Unknown")  # Adjust based on your report schema
        return HTMLResponse(content=f"""
            <html>
                <body>
                    <h2>Report Status</h2>
                    <p>Report ID: {report_id}</p>
                    <p>Status: {report_status}</p>
                    <pre>{report}</pre>  <!-- Optionally show the report data -->
                </body>
            </html>
        """)
    else:
        # Return a message if the report is not found
        return HTMLResponse(content=f"""
            <html>
                <body>
                    <h2>Report Not Found</h2>
                    <p>Report ID: {report_id}</p>
                    <p>Status: No report generated for this ID.</p>
                </body>
            </html>
        """)
