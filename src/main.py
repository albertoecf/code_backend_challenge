import os
import uvicorn
from fastapi import FastAPI
from src.controllers import GenerateReport
from src.app_config import result_file_path, bookings_file_path, chart_of_accounts_file_path
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse

app = FastAPI()


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

        # Generate report for the specified period
        new_period_income_statement = report_generator.generate_report(new_period)
        old_period_income_statement = report_generator.generate_report(old_period)

        # Return the IncomeStatement as JSON
        # todo: comparre both periods
        comparison_results = report_generator.compare_income_statements(
            new_period_income_statement, old_period_income_statement
        )
        # Construct the final report dictionary
        final_report = {
            "June, 2020": new_period_income_statement.dict(),
            "May, 2020": old_period_income_statement.dict(),
            "June vs May, 2020 (Abs)": comparison_results,
        }

        # Save the final report to a JSON file
        import json
        output_file_path = "final_report.json"
        with open(output_file_path, "w") as output_file:
            json.dump(final_report, output_file)

        # Return the final report file as a downloadable response
        return FileResponse(
            output_file_path,
            media_type="application/json",
            filename="final_report.json",
        )

    except ValueError as ve:
        # Handle validation errors and return an error response
        return JSONResponse(content={"error": str(ve)}, status_code=400)
    except Exception as e:
        # Handle other exceptions and return an error response
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", 8000)),
        workers=int(os.getenv("APP_WORKERS", 1)),
        reload=True,
    )
