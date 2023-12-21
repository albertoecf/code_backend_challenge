from pathlib import Path

# Define the project root
project_root = Path(__file__).resolve().parents[1]

# Define the file paths based on the project root
result_file_path = Path("src/result_report.csv")
bookings_file_path = project_root / "data" / "bookings.csv"
chart_of_accounts_file_path = project_root / "data" / "chart-of-accounts.csv"
