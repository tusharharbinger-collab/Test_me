from fastapi import FastAPI

app = FastAPI(title="test_me", version="1.0.0")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/{full_path:path}")
def catch_all(full_path: str):
    return {
        "received_path": full_path,
        "message": "Hello from Test_me",
        "version": "1.0.0",
    }
