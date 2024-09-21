# Restaurant Monitoring System

## Project Overview
The Restaurant Monitoring System is a web application designed to monitor store statuses, manage business hours, and generate reports based on uptime and downtime for restaurants. This system utilizes FastAPI for backend development and MongoDB for data storage, providing a robust solution for restaurant management.

## Installation Instructions
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Hsinha11/Harianant_21-09-2024.git
   cd Harianant_21-09-2024
2. Create a virtual environment:
    ```bash
      python -m venv venv
3.  Activate the virtual environment:
    - On Windows
      ```bash
      venv\Scripts\activate
    - On macOS/ Linux
      ```bash
      source venv/bin/activate
4.  Install the required packages:
    ```bash
    pip install -r requirements.txt
5.  Set up your .env file with the following variables:
    ```bash
    MONGO_DB_URL=mongodb://localhost:27017/
    MONGO_DB_NAME=restaurant_monitoring

6.  Start the FastAPI application:
    ```bash
    uvicorn app.main:app --reload
## Usage
- Navigate to http://127.0.0.1:8000 to access the web application.
- Use the /trigger_report endpoint to generate reports.
- Use the /get_report/{report_id} endpoint to fetch the status of your reports.
## Improvement Ideas 
- User Authentication: Implement user authentication for secure access to the system.
- Data Visualization: Add graphs and charts to visualize report data for better insights.
- Error Handling: Enhance error handling and logging to track issues more effectively.
- Unit Testing: Develop unit tests for critical components to ensure reliability and maintainability.
## CSV Output
  A sample CSV output file can be found in the repository:
 - store_status.csv
## Demo Video
You can watch a demo of the application functionality here:

- [Demo Video](www.google.com)
