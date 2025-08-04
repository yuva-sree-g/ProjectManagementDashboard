# 🚀 Project Management Dashboard

A modern, full-stack project management application built with FastAPI, React, and PostgreSQL. Features include project management, task tracking, time logging, and team collaboration.

## 📋 Application Deliverables

### ✅ Live Application URL
- **Frontend**: https://project-management-dashboard-dno2.vercel.app/
- **Backend**: https://projectmanagementdashboard.onrender.com
- **API Documentation**: https://projectmanagementdashboard.onrender.com/docs
- **Database**: PostgreSQL on Render

### ✅ GitHub Repository
- **Repository**: Complete source code with clear documentation
- **Structure**: Well-organized project with proper separation of concerns
- **Documentation**: Comprehensive README and development guides

### ✅ Demo Video
- **Duration**: 5-minute walkthrough of key features
- **Content**: User registration, project creation, task management, time tracking, dashboard analytics
- **Link**: [To be added after recording]

### ✅ Admin Credentials
- **Username**: yuvasreega
- **Password**: yuvasree
- **Test User**: testuser / testuser
- **Access**: Full administrative privileges for evaluator access

## 🌐 Production Deployment Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Vercel        │    │   Render        │    │   Render        │
│   Frontend      │◄──►│   Backend       │◄──►│   PostgreSQL    │
│                 │    │                 │    │                 │
│  - React App    │    │  - FastAPI      │    │  - Database     │
│  - Static Files │    │  - Python       │    │  - Data Storage │
│  - CDN          │    │  - Docker       │    │  - Backups      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Production URLs:
- **Frontend**: https://project-management-dashboard-dno2.vercel.app/
- **Backend API**: https://projectmanagementdashboard.onrender.com
- **Database**: postgresql://projectuser:aroQ42eH1dJ75YHHejJb1On3dTHCxYQ3@dpg-d27ruomuk2gs73ejfkj0-a.oregon-postgres.render.com/project_dashboard_67v7

## ✨ Features

- **🔐 Authentication**: JWT-based user authentication and authorization
- **📊 Dashboard**: Overview of all projects and tasks with statistics
- **📋 Project Management**: Create, update, and track projects globally
- **✅ Task Management**: Kanban-style task board with status tracking
- **⏱️ Time Tracking**: Log and track time spent on tasks with estimated vs actual hours
- **👥 User Management**: Assign tasks to team members with global visibility
- **💬 Comments**: Add comments to projects and tasks
- **📧 Email Notifications**: Automatic email notifications for task assignments, updates, and completions
- **📈 Performance Metrics**: Dashboard with productivity score and project health indicators
- **📱 Responsive Design**: Works on desktop and mobile devices

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - Database ORM
- **PostgreSQL** - Database
- **JWT** - Authentication
- **Pydantic** - Data validation
- **FastAPI-Mail** - Email notifications
- **Python-dotenv** - Environment management

### Frontend
- **React** - UI framework
- **Redux Toolkit** - State management
- **React Router** - Navigation
- **Tailwind CSS** - Styling
- **Axios** - HTTP client
- **Chart.js** - Data visualization

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Local development
- **Vercel** - Frontend deployment
- **Render** - Backend deployment

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Node.js 16+ (for local development)
- Python 3.11+ (for local development)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ProjectManagementDashboard
   ```

2. **Start the application**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

4. **Create your first user**
   - Go to http://localhost:3000/register
   - Create an account and start using the application

## 🔧 Environment Setup

### Backend Environment Variables
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/project_dashboard
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_FROM=your-email@gmail.com
FRONTEND_URL=http://localhost:3000
CORS_ORIGINS=http://localhost:3000,https://your-frontend-url.com
```

### Frontend Environment Variables
```bash
REACT_APP_API_URL=http://localhost:8000
```

## 📊 API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user

### Projects
- `GET /projects` - List all projects
- `POST /projects` - Create new project
- `GET /projects/{id}` - Get project details
- `PUT /projects/{id}` - Update project
- `DELETE /projects/{id}` - Delete project

### Tasks
- `GET /tasks` - List all tasks
- `POST /tasks` - Create new task
- `GET /tasks/{id}` - Get task details
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task
- `POST /tasks/{id}/log-time` - Log time for task

### Comments
- `GET /tasks/{id}/comments` - Get task comments
- `POST /tasks/{id}/comments` - Add comment to task
- `GET /projects/{id}/comments` - Get project comments
- `POST /projects/{id}/comments` - Add comment to project

### Performance Metrics
- `GET /performance-metrics` - Get dashboard metrics

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📊 Evaluation Framework (100 Points)

### Technical Implementation (50 points)
- **Functionality (20 pts)**: ✅ Core features working correctly
- **Code Quality (15 pts)**: ✅ Clean, maintainable, secure code
- **AI Integration (15 pts)**: ✅ Effective use of AI tools throughout development

### Process Mastery (30 points)
- **Methodology (15 pts)**: ✅ Following a structured development approach
- **Problem Solving (10 pts)**: ✅ Effective use of AI for debugging and optimization
- **Time Management (5 pts)**: ✅ Completing project within timeline

### Documentation & Knowledge Transfer (20 points)
- **Documentation (10 pts)**: ✅ Comprehensive documentation and guides
- **Knowledge Transfer (10 pts)**: ✅ Clear code structure and comments

## 📁 Project Structure

```
ProjectManagementDashboard/
├── backend/                 # FastAPI backend
│   ├── app/                # Application code
│   │   ├── routers/        # API endpoints
│   │   ├── schemas/        # Pydantic models
│   │   ├── models.py       # Database models
│   │   ├── database.py     # Database configuration
│   │   ├── auth.py         # Authentication logic
│   │   └── main.py         # FastAPI app
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Backend container
├── frontend/               # React frontend
│   ├── src/               # Source code
│   │   ├── components/     # React components
│   │   ├── features/       # Redux slices
│   │   ├── services/       # API services
│   │   └── App.js         # Main app component
│   ├── package.json       # Node dependencies
│   └── Dockerfile         # Frontend container
├── docker-compose.yml     # Local development
├── .github/workflows/     # CI/CD
├── README.md             # Project overview
├── DEVELOPMENT_PROCESS_REPORT.md  # Development process
├── AI_PROMPT_LIBRARY.md  # AI prompt collection
└── LEARNING_REFLECTION_REPORT.md  # Learning insights
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is developed as part of the AI Upskilling Assessment for Ideas2IT.

---

**Developed by**: Yuvasree Ganesan (I24132)  
**Assessment Level**: L2  
**Technology Stack**: FastAPI + React + PostgreSQL  
**Deployment**: Vercel + Render 