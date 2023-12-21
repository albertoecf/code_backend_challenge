import os
import uvicorn
from fastapi import FastAPI
from controllers import GenerateReport
from app_config import (
    result_file_path,
    bookings_file_path,
    chart_of_accounts_file_path,
)
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse

app = FastAPI(debug=True)


@app.get("/")
def hello_handler():
    return {"msg": "Hello, World!"}


@app.get("/report")
def read_report():
    try:
        # Initialize the controller with necessary file paths
        report_generator = GenerateReport(
            bookings_file_path, chart_of_accounts_file_path
        )

        new_period = {"year": 2020, "month": 6}
        old_period = {"year": 2020, "month": 5}

        # Generate and save the report
        output_file_path = report_generator.generate_and_save_report(
            new_period, old_period
        )

        # Return the final report file as a downloadable response with status code 200
        return FileResponse(
            output_file_path,
            media_type="text/csv",  # Use CSV media type
            filename="final_report.csv",
            status_code=200,
        )
    except ValueError as ve:
        # Handle validation errors and return an error response
        return JSONResponse(content={"error": str(ve)}, status_code=400)
    except Exception as e:
        # Handle other exceptions and return an error response
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", 8000)),
        workers=int(os.getenv("APP_WORKERS", 1)),
        reload=True,
    )
