# AI Prompt Library

## Database Design Prompts

### Prompt 1: Schema Generation
**Prompt**: "Design a PostgreSQL database schema for a project management system with users, projects, tasks, time logs, and comments. Include proper relationships, constraints, and indexes."
**Context**: Need for a scalable project management system with user authentication, project tracking, and time management
**Output Quality**: 9/10
**Iterations**: 2 refinements needed for time tracking relationships
**Final Result**: Implemented complete schema with users, projects, tasks, time_logs, and comments tables with proper foreign key relationships

### Prompt 2: Database Migration
**Prompt**: "Create Alembic migration for adding time tracking functionality to existing project management database"
**Context**: Existing database with users, projects, tasks tables
**Output Quality**: 8/10
**Iterations**: 1 refinement for proper foreign key constraints
**Final Result**: Successful migration adding time_logs table with proper relationships

## Code Generation Prompts

### Prompt 3: API Endpoint Creation
**Prompt**: "Create FastAPI endpoint for time tracking with CRUD operations, proper validation, and authorization"
**Context**: Need RESTful API for time log management with user authentication
**Output Quality**: 9/10
**Modifications**: Added custom validation for hours field and date constraints
**Final Result**: Complete time tracking API with create, read, update, delete operations

### Prompt 4: React Component Generation
**Prompt**: "Create a React component for time tracking form with validation, date picker, and hours input"
**Context**: Need user-friendly form for logging time spent on tasks
**Output Quality**: 8/10
**Modifications**: Enhanced with better error handling and user feedback
**Final Result**: Functional time tracking form with proper validation and UX

### Prompt 5: Redux Slice Creation
**Prompt**: "Create Redux Toolkit slice for time tracking with async thunks for API calls"
**Context**: Need state management for time logs with API integration
**Output Quality**: 9/10
**Modifications**: Added error handling and loading states
**Final Result**: Complete Redux slice with create, fetch, update, delete operations

## Problem-Solving Prompts

### Prompt 6: CORS Configuration
**Prompt**: "Fix CORS issues in FastAPI backend for React frontend running on different ports"
**Context**: Frontend on localhost:3000, backend on localhost:8000
**Output Quality**: 10/10
**Effectiveness**: Immediately resolved CORS errors
**Final Result**: Proper CORS configuration allowing frontend-backend communication

### Prompt 7: Docker Configuration
**Prompt**: "Create Docker Compose setup for React frontend, FastAPI backend, and PostgreSQL database"
**Context**: Need containerized development environment
**Output Quality**: 9/10
**Modifications**: Added volume mounts for development and proper networking
**Final Result**: Complete Docker setup with hot reloading and database persistence

### Prompt 8: Authentication Flow
**Prompt**: "Implement JWT authentication flow with login, register, and token refresh in FastAPI"
**Context**: Need secure user authentication system
**Output Quality**: 8/10
**Modifications**: Enhanced with password hashing and proper error handling
**Final Result**: Complete authentication system with JWT tokens

## UI/UX Prompts

### Prompt 9: Dashboard Design
**Prompt**: "Design a modern dashboard layout with project statistics, task overview, and recent activity"
**Context**: Need comprehensive project management dashboard
**Output Quality**: 8/10
**Modifications**: Added responsive design and better data visualization
**Final Result**: Professional dashboard with charts and statistics

### Prompt 10: Form Validation
**Prompt**: "Create comprehensive form validation for project creation with proper error messages"
**Context**: Need user-friendly project creation form
**Output Quality**: 9/10
**Modifications**: Added real-time validation and better UX
**Final Result**: Robust form validation with excellent user experience

## Deployment Prompts

### Prompt 11: Environment Configuration
**Prompt**: "Set up environment variables for production deployment with proper security"
**Context**: Need secure configuration for production environment
**Output Quality**: 9/10
**Modifications**: Added database URL configuration and secret management
**Final Result**: Secure environment configuration for deployment

### Prompt 12: Docker Production Build
**Prompt**: "Create production-ready Dockerfile for React frontend with optimized build"
**Context**: Need optimized production build for frontend
**Output Quality**: 8/10
**Modifications**: Added multi-stage build for smaller image size
**Final Result**: Optimized production Docker image

## Testing Prompts

### Prompt 13: API Testing
**Prompt**: "Create comprehensive test cases for project management API endpoints"
**Context**: Need thorough testing for API functionality
**Output Quality**: 7/10
**Modifications**: Added edge cases and error scenario testing
**Final Result**: Complete test suite covering all API endpoints

### Prompt 14: Component Testing
**Prompt**: "Write React component tests for time tracking functionality"
**Context**: Need unit tests for React components
**Output Quality**: 8/10
**Modifications**: Added integration tests and user interaction testing
**Final Result**: Comprehensive component test coverage

## Performance Optimization Prompts

### Prompt 15: Database Query Optimization
**Prompt**: "Optimize database queries for dashboard statistics with proper indexing"
**Context**: Need fast dashboard loading with complex statistics
**Output Quality**: 8/10
**Effectiveness**: Improved query performance by 60%
**Final Result**: Optimized queries with proper database indexing

### Prompt 16: React Performance
**Prompt**: "Optimize React components for large task lists with virtualization"
**Context**: Need smooth performance with hundreds of tasks
**Output Quality**: 7/10
**Modifications**: Implemented pagination instead of virtualization
**Final Result**: Improved performance with paginated task lists

## Debugging Prompts

### Prompt 17: Docker Issues Resolution
**Prompt**: "Fix Docker Compose network issues and port conflicts"
**Context**: Docker containers not starting due to network and port conflicts
**Output Quality**: 9/10
**Effectiveness**: Resolved all Docker startup issues
**Final Result**: Stable Docker development environment

### Prompt 18: API Route Debugging
**Prompt**: "Debug why FastAPI endpoints are returning 404 errors despite being defined"
**Context**: API routes not accessible despite proper router inclusion
**Output Quality**: 8/10
**Effectiveness**: Identified missing import in __init__.py file
**Final Result**: All API endpoints working correctly

### Prompt 19: Database Connection Issues
**Prompt**: "Fix PostgreSQL connection errors in Docker environment"
**Context**: Backend unable to connect to database container
**Output Quality**: 9/10
**Effectiveness**: Resolved database connectivity issues
**Final Result**: Stable database connection in Docker environment

## Integration Prompts

### Prompt 20: Frontend-Backend Integration
**Prompt**: "Integrate React frontend with FastAPI backend for time tracking feature"
**Context**: Need seamless integration between frontend time tracking and backend API
**Output Quality**: 9/10
**Modifications**: Added proper error handling and loading states
**Final Result**: Complete time tracking integration with excellent UX 