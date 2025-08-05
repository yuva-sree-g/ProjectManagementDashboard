#!/usr/bin/env python3
"""
Seed Data Script for Project Management Dashboard
Populates the database with sample projects and tasks for demonstration.
"""

from sqlalchemy.orm import Session
from .models import User, Project, Task, TimeLog, TaskStatus, TaskPriority
from .auth import get_password_hash
from datetime import datetime, timedelta
import random

def create_sample_users(db: Session):
    """Create sample users for demonstration."""
    users_data = [
        {
            "username": "yuvasreega",
            "email": "yuvasreega@example.com",
            "full_name": "Yuvasree Ganesan",
            "password": "yuvasree"
        },
        {
            "username": "testuser",
            "email": "testuser@example.com",
            "full_name": "Test User",
            "password": "testuser"
        },
        {
            "username": "developer1",
            "email": "developer1@example.com",
            "full_name": "Developer One",
            "password": "password123"
        },
        {
            "username": "manager1",
            "email": "manager1@example.com",
            "full_name": "Manager One",
            "password": "password123"
        }
    ]
    
    for user_data in users_data:
        # Check if user already exists
        existing_user = db.query(User).filter(User.username == user_data["username"]).first()
        if not existing_user:
            hashed_password = get_password_hash(user_data["password"])
            user = User(
                username=user_data["username"],
                email=user_data["email"],
                full_name=user_data["full_name"],
                hashed_password=hashed_password
            )
            db.add(user)
    
    db.commit()
    print("✅ Sample users created successfully!")

def create_sample_projects(db: Session):
    """Create sample projects for demonstration."""
    projects_data = [
        {
            "title": "E-Commerce Platform Development",
            "description": "Build a modern e-commerce platform with React frontend and FastAPI backend",
            "status": "active",
            "owner_id": 1
        },
        {
            "title": "Mobile App for Task Management",
            "description": "Develop a cross-platform mobile application for task and project management",
            "status": "active",
            "owner_id": 1
        },
        {
            "title": "AI-Powered Analytics Dashboard",
            "description": "Create an intelligent analytics dashboard with machine learning capabilities",
            "status": "on_hold",
            "owner_id": 1
        }
    ]
    
    for project_data in projects_data:
        # Check if project already exists
        existing_project = db.query(Project).filter(Project.title == project_data["title"]).first()
        if not existing_project:
            project = Project(**project_data)
            db.add(project)
    
    db.commit()
    print("✅ Sample projects created successfully!")

def create_sample_tasks(db: Session):
    """Create sample tasks for demonstration."""
    tasks_data = [
        # E-Commerce Platform Tasks
        {
            "title": "Design User Interface",
            "description": "Create wireframes and mockups for the e-commerce platform",
            "status": TaskStatus.COMPLETED,
            "priority": TaskPriority.HIGH,
            "estimated_hours": 16,
            "project_id": 1,
            "assignee_id": 1
        },
        {
            "title": "Implement User Authentication",
            "description": "Set up JWT-based authentication system",
            "status": TaskStatus.IN_PROGRESS,
            "priority": TaskPriority.HIGH,
            "estimated_hours": 12,
            "project_id": 1,
            "assignee_id": 2
        },
        {
            "title": "Create Product Catalog",
            "description": "Build product listing and search functionality",
            "status": TaskStatus.TO_DO,
            "priority": TaskPriority.MEDIUM,
            "estimated_hours": 20,
            "project_id": 1,
            "assignee_id": 3
        },
        {
            "title": "Payment Integration",
            "description": "Integrate Stripe payment gateway",
            "status": TaskStatus.TO_DO,
            "priority": TaskPriority.HIGH,
            "estimated_hours": 24,
            "project_id": 1,
            "assignee_id": 4
        },
        
        # Mobile App Tasks
        {
            "title": "Setup React Native Project",
            "description": "Initialize React Native project with TypeScript",
            "status": TaskStatus.COMPLETED,
            "priority": TaskPriority.MEDIUM,
            "estimated_hours": 8,
            "project_id": 2,
            "assignee_id": 1
        },
        {
            "title": "Design Mobile UI Components",
            "description": "Create reusable UI components for the mobile app",
            "status": TaskStatus.IN_PROGRESS,
            "priority": TaskPriority.HIGH,
            "estimated_hours": 16,
            "project_id": 2,
            "assignee_id": 2
        },
        {
            "title": "Implement Task CRUD Operations",
            "description": "Create task creation, editing, and deletion functionality",
            "status": TaskStatus.TO_DO,
            "priority": TaskPriority.HIGH,
            "estimated_hours": 20,
            "project_id": 2,
            "assignee_id": 3
        },
        {
            "title": "Add Push Notifications",
            "description": "Implement push notifications for task reminders",
            "status": TaskStatus.TO_DO,
            "priority": TaskPriority.MEDIUM,
            "estimated_hours": 12,
            "project_id": 2,
            "assignee_id": 4
        },
        
        # AI Analytics Dashboard Tasks
        {
            "title": "Research ML Algorithms",
            "description": "Research and select appropriate ML algorithms for analytics",
            "status": TaskStatus.IN_PROGRESS,
            "priority": TaskPriority.HIGH,
            "estimated_hours": 24,
            "project_id": 3,
            "assignee_id": 1
        },
        {
            "title": "Design Dashboard Layout",
            "description": "Create responsive dashboard layout with charts and graphs",
            "status": TaskStatus.TO_DO,
            "priority": TaskPriority.MEDIUM,
            "estimated_hours": 16,
            "project_id": 3,
            "assignee_id": 2
        },
        {
            "title": "Implement Data Processing Pipeline",
            "description": "Build ETL pipeline for data processing and analysis",
            "status": TaskStatus.TO_DO,
            "priority": TaskPriority.HIGH,
            "estimated_hours": 32,
            "project_id": 3,
            "assignee_id": 3
        },
        {
            "title": "Create Predictive Models",
            "description": "Develop machine learning models for predictive analytics",
            "status": TaskStatus.TO_DO,
            "priority": TaskPriority.HIGH,
            "estimated_hours": 40,
            "project_id": 3,
            "assignee_id": 4
        }
    ]
    
    for task_data in tasks_data:
        # Check if task already exists
        existing_task = db.query(Task).filter(Task.title == task_data["title"]).first()
        if not existing_task:
            task = Task(**task_data)
            db.add(task)
    
    db.commit()
    print("✅ Sample tasks created successfully!")

def create_sample_time_logs(db: Session):
    """Create sample time logs for demonstration."""
    # Get some tasks to create time logs for
    tasks = db.query(Task).limit(5).all()
    
    for task in tasks:
        # Create 2-3 time logs per task
        for i in range(random.randint(2, 3)):
            hours = random.randint(2, 8)
            date = datetime.now() - timedelta(days=random.randint(1, 7))
            
            time_log = TimeLog(
                task_id=task.id,
                user_id=task.assignee_id or 1,
                hours=hours,
                description=f"Work on {task.title} - day {i+1}",
                date=date
            )
            db.add(time_log)
    
    db.commit()
    print("✅ Sample time logs created successfully!")

def main():
    """Main function to seed the database."""
    from .database import SessionLocal
    
    db = SessionLocal()
    try:
        print("🌱 Starting database seeding...")
        
        create_sample_users(db)
        create_sample_projects(db)
        create_sample_tasks(db)
        create_sample_time_logs(db)
        
        print("🎉 Database seeding completed successfully!")
        
    except Exception as e:
        print(f"❌ Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main() 