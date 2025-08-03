from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Project, User, Task
from ..schemas.project import ProjectCreate, Project as ProjectSchema, ProjectUpdate
from ..schemas.task import Task as TaskSchema
from ..auth import get_current_active_user

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/", response_model=List[ProjectSchema])
def get_projects(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get all projects in the system (globally visible)."""
    projects = db.query(Project).offset(skip).limit(limit).all()
    return projects

@router.post("/", response_model=ProjectSchema)
def create_project(
    project: ProjectCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Create a new project."""
    db_project = Project(**project.dict(), owner_id=current_user.id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/{project_id}", response_model=ProjectSchema)
def get_project(
    project_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get a specific project by ID (globally visible)."""
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{project_id}", response_model=ProjectSchema)
def update_project(
    project_id: int,
    project_update: ProjectUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update a project (only project owner can update)."""
    db_project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found or you don't have permission to update it")
    
    update_data = project_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_project, field, value)
    
    db.commit()
    db.refresh(db_project)
    return db_project

@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Delete a project (only project owner can delete)."""
    db_project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found or you don't have permission to delete it")
    
    db.delete(db_project)
    db.commit()
    return {"message": "Project deleted successfully"}

@router.get("/{project_id}/tasks", response_model=List[TaskSchema])
def get_project_tasks(
    project_id: int,
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get all tasks for a specific project."""
    # Verify project ownership
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    tasks = db.query(Task).filter(
        Task.project_id == project_id
    ).offset(skip).limit(limit).all()
    
    return tasks

@router.get("/{project_id}/summary")
def get_project_summary(
    project_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Get project summary with task statistics."""
    # Verify project ownership
    project = db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == current_user.id
    ).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Get task statistics
    total_tasks = db.query(Task).filter(Task.project_id == project_id).count()
    todo_tasks = db.query(Task).filter(
        Task.project_id == project_id,
        Task.status == "todo"
    ).count()
    in_progress_tasks = db.query(Task).filter(
        Task.project_id == project_id,
        Task.status == "in_progress"
    ).count()
    review_tasks = db.query(Task).filter(
        Task.project_id == project_id,
        Task.status == "review"
    ).count()
    ready_to_test_tasks = db.query(Task).filter(
        Task.project_id == project_id,
        Task.status == "ready_to_test"
    ).count()
    in_test_tasks = db.query(Task).filter(
        Task.project_id == project_id,
        Task.status == "in_test"
    ).count()
    closed_tasks = db.query(Task).filter(
        Task.project_id == project_id,
        Task.status == "closed"
    ).count()
    
    # Calculate total estimated and actual hours
    tasks = db.query(Task).filter(Task.project_id == project_id).all()
    total_estimated_hours = sum(task.estimated_hours or 0 for task in tasks)
    total_actual_hours = sum(task.actual_hours or 0 for task in tasks)
    
    return {
        "project_id": project_id,
        "project_title": project.title,
        "total_tasks": total_tasks,
        "todo_tasks": todo_tasks,
        "in_progress_tasks": in_progress_tasks,
        "review_tasks": review_tasks,
        "ready_to_test_tasks": ready_to_test_tasks,
        "in_test_tasks": in_test_tasks,
        "closed_tasks": closed_tasks,
        "completion_percentage": round((closed_tasks / total_tasks * 100) if total_tasks > 0 else 0, 2),
        "total_estimated_hours": total_estimated_hours,
        "total_actual_hours": total_actual_hours
    } 