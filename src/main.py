from fastapi import FastAPI
from controllers import GenerateReport
from app_config import result_file_path, bookings_file_path, chart_of_accounts_file_path


app = FastAPI()


@app.get("/")
def hello_handler():
    return {"msg": "Hello, World!"}


@app.get("/report")
def read_report():
    # todo : docstrings

    # Initialize the controller with necessary file paths
    report_generator = GenerateReport(
        bookings_file_path, chart_of_accounts_file_path, result_file_path
    )

    new_period = {"year": 2020, "month": 6}
    old_period = {"year": 2020, "month": 5}
    # todo add new_period, old_perdiod
    new_period_df = report_generator.generate_report()  # new_period
    old_period_df = report_generator.generate_report()  # old_period

    return new_period_df

    # return FileResponse(response_file_path)


# todo delete, only for development conveniance
if __name__ == "__main__":
    import uvicorn

    # Run the application using Uvicorn with --reload option
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
