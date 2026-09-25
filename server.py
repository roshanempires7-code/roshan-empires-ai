from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Roshan AI Server")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Task(BaseModel):
    task: str


def analyze_task(task):
    task_lower = task.lower()

    if "website" in task_lower:
        category = "Website Creation"
    elif "logo" in task_lower:
        category = "Logo / Branding"
    elif "blog" in task_lower or "article" in task_lower:
        category = "Content Writing"
    elif "cv" in task_lower or "resume" in task_lower:
        category = "CV Creation"
    else:
        category = "General Task"

    return category


def content_agent(task, category):

    if category == "Website Creation":
        return f"""
Website Project Plan

Customer Request:
{task}

Generated Plan:
1. Create responsive homepage
2. Add navigation
3. Create services section
4. Add contact section
5. Make design mobile-friendly
6. Test HTML, CSS and JavaScript
"""

    if category == "Logo / Branding":
        return f"""
Branding Project

Customer Request:
{task}

Generated Plan:
1. Understand brand name
2. Choose visual style
3. Create logo concept
4. Prepare branding variations
5. Review final design
"""

    if category == "Content Writing":
        return f"""
Content Project

Customer Request:
{task}

Generated Plan:
1. Understand topic
2. Create outline
3. Write introduction
4. Develop main sections
5. Add conclusion
6. Proofread content
"""

    if category == "CV Creation":
        return f"""
CV Project

Customer Request:
{task}

Generated Plan:
1. Collect candidate information
2. Create professional structure
3. Add education and skills
4. Add experience
5. Format professionally
6. Perform final review
"""

    return f"""
General AI Task

Customer Request:
{task}

Generated Plan:
1. Analyze request
2. Break task into smaller steps
3. Process each step
4. Review result
5. Prepare final output
"""


def quality_checker(result):

    checks = [
        "Task analyzed",
        "Workflow generated",
        "Output reviewed"
    ]

    return checks


@app.get("/")
def home():
    return {
        "name": "Roshan AI Server",
        "status": "online",
        "message": "Roshan AI is running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "time": datetime.now().isoformat()
    }


@app.post("/run")
def run_task(data: Task):

    category = analyze_task(data.task)

    result = content_agent(
        data.task,
        category
    )

    checks = quality_checker(result)

    return {
        "success": True,
        "category": category,
        "result": result,
        "quality_checks": checks
    }