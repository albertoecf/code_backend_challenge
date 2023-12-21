import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from src.controllers import GenerateReport
from src.app_config import (
    bookings_file_path,
    chart_of_accounts_file_path,
)

app = FastAPI(
    title="Helu Financial Report API",
    description="API for generating and downloading financial reports",
    version="1.0.0",
)

# Initialize the controller with necessary file paths
report_generator = GenerateReport(bookings_file_path, chart_of_accounts_file_path)


# Dependency to use in the path operation
def get_report_generator():
    return report_generator


@app.get("/")
def hello_handler():
    return {"msg": "Hello, World!"}


@app.get(
    "/report",
    tags=["report"],
    summary="Download Financial Report",
    response_description="The generated financial report in CSV format",
)
def read_report():
    """
    Generate and download the financial report.

    Warning:
        Args are hardcoded, we could improve our endpoint to accept such parameters
        new_period (dict): Dictionary containing 'year' and 'month' for the new period.
        old_period (dict): Dictionary containing 'year' and 'month' for the old period.

    Returns:
        FileResponse: The generated financial report in CSV format.
    """
    try:
        # Generate and save the report
        new_period = {"year": 2020, "month": 6}
        old_period = {"year": 2020, "month": 5}

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
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        # Handle other exceptions and return an error response
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", 8000)),
        workers=int(os.getenv("APP_WORKERS", 1)),
        reload=True,
    )
