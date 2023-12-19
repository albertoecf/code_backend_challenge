import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient
import sys
from pathlib import Path

# Add the project's root directory to sys.path
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))
from src.main import app as orig_app


@pytest.fixture
def app() -> FastAPI:
    testing_app = orig_app

    return testing_app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app)
