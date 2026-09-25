import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from google import genai

app = FastAPI(docs_url=None, redoc_url=None)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class Task(BaseModel):
    prompt: str = ""
    task: str = ""

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/health")
def health_check():
    return {"status": "online", "message": "Roshan AI is running 🚀"}

@app.post("/run")
def run_task(task_data: Task):
    user_prompt = task_data.prompt or task_data.task
    if not user_prompt:
        return {"result": "Koyi prompt nahi mila!"}
    
    system_instruction = (
        "You are a web generator. Output ONLY full valid HTML code with inline CSS/Tailwind CDN. "
        "Do NOT output markdown codeblocks, do NOT write explanations, greetings or commentary. "
        "Output pure HTML only starting with <!DOCTYPE html>."
    )
    
    try:
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=f"{system_instruction}\n\nTask: {user_prompt}",
        )
        
        raw_html = response.text.replace("```html", "").replace("```", "").strip()
        return {"result": raw_html}
    except Exception as e:
        return {"result": f"Error: {str(e)}"}
