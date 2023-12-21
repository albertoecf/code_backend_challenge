# main.py
from fastapi import FastAPI
from controllers import GenerateReport
from app_config import result_file_path, bookings_file_path, chart_of_accounts_file_path
from fastapi.responses import JSONResponse

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
        #todo: comparre both periods
        return JSONResponse(content=new_period_income_statement.dict())

    except ValueError as ve:
        # Handle validation errors and return an error response
        return JSONResponse(content={"error": str(ve)}, status_code=400)
    except Exception as e:
        # Handle other exceptions and return an error response
        return JSONResponse(content={"error": str(e)}, status_code=500)


# todo delete, only for development conveniance
if __name__ == "__main__":
    import uvicorn

    # Run the application using Uvicorn with --reload option
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
