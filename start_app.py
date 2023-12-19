#!/usr/bin/env python3
import os
import uvicorn

if __name__ == "__main__":

    uvicorn.run(
        "src.main:app",
        host=os.getenv("APP_HOST", "0.0.0.0"),
        port=int(os.getenv("APP_PORT", 8000)),
        workers=int(os.getenv("APP_WORKERS", 1)),
        reload=True,
    )
