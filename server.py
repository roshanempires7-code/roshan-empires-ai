from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(docs_url=None, redoc_url=None)  # docs_url=None se /docs page hide ho jayega

# Request model for /run endpoint
class Task(BaseModel):
    prompt: str

# Root par frontend index.html render hoga
@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/health")
def health_check():
    return {"status": "online", "message": "Roshan AI is running 🚀"}

@app.post("/run")
def run_task(task: Task):
    # Aapka backend logic
    return {"result": f"Processed prompt: {task.prompt}"}
