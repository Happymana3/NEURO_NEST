from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.models.database import get_db, Task
from planner.parser import TaskParser
from pydantic import BaseModel

router = APIRouter()
task_parser = TaskParser()

class TaskRequest(BaseModel):
    text: str

@router.post("/add-task")
async def add_task(request: TaskRequest, db: Session = Depends(get_db)):
    """Add task from natural language"""
    task_data = task_parser.parse_natural_language(request.text)
    
    task = Task(
        title=task_data['title'],
        description=task_data['description'],
        due_date=task_data['due_date']
    )
    
    db.add(task)
    db.commit()
    
    return {"message": "Task added", "task": task_data}

@router.get("/tasks")
async def get_tasks(db: Session = Depends(get_db)):
    """Get all tasks"""
    tasks = db.query(Task).all()
    return {"tasks": tasks}