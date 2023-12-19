from starlette.testclient import TestClient


def test_report(client: TestClient, file_regression):
    """
    Given a GET request to an endpoint /report,
    The response should match with provided test_report.csv file
    """
    response = client.get("/report")

    file_regression.check(response.content, extension=".csv", binary=True)
