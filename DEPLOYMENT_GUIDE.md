# 🚀 Deployment Guide

This guide will help you deploy the Project Management Dashboard to Vercel (frontend) and Render (backend).

## 📋 Prerequisites

- GitHub repository: [https://github.com/yuva-sree-g/ProjectManagementDashboard](https://github.com/yuva-sree-g/ProjectManagementDashboard)
- Vercel account: [https://vercel.com](https://vercel.com)
- Render account: [https://render.com](https://render.com)

## 🔧 Step 1: Deploy Backend to Render

### 1.1 Create Render Account
1. Go to [Render.com](https://render.com)
2. Sign up with your GitHub account
3. Connect your GitHub repository

### 1.2 Deploy Backend Service
1. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `yuva-sree-g/ProjectManagementDashboard`

2. **Configure Service Settings**
   ```
   Name: project-dashboard-backend
   Environment: Python 3
   Build Command: pip install -r backend/requirements.txt
   Start Command: cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

3. **Add Environment Variables**
   ```
   DATABASE_URL: [Will be set after database creation]
   SECRET_KEY: [Generate a random string]
   ALGORITHM: HS256
   ACCESS_TOKEN_EXPIRE_MINUTES: 30
   CORS_ORIGINS: *
   ```

4. **Create PostgreSQL Database**
   - Go to "New +" → "PostgreSQL"
   - Name: `project-dashboard-db`
   - Copy the database URL and update `DATABASE_URL` in your web service

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Copy your backend URL (e.g., `https://your-app.onrender.com`)

## 🌐 Step 2: Deploy Frontend to Vercel

### 2.1 Create Vercel Account
1. Go to [Vercel.com](https://vercel.com)
2. Sign up with your GitHub account
3. Import your GitHub repository

### 2.2 Configure Vercel Deployment
1. **Import Repository**
   - Click "New Project"
   - Import: `yuva-sree-g/ProjectManagementDashboard`
   - Framework Preset: `Create React App`

2. **Configure Build Settings**
   ```
   Root Directory: frontend
   Build Command: npm run build
   Output Directory: build
   Install Command: npm install
   ```

3. **Add Environment Variables**
   ```
   REACT_APP_API_URL: [Your Render backend URL]
   ```

4. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete
   - Copy your frontend URL (e.g., `https://your-app.vercel.app`)

## 🔗 Step 3: Update Configuration

### 3.1 Update Backend CORS
After getting your Vercel frontend URL, update the backend CORS settings:

1. Go to your Render backend service
2. Add environment variable:
   ```
   CORS_ORIGINS: https://your-frontend-url.vercel.app
   ```
3. Redeploy the backend service

### 3.2 Update Frontend API URL
1. Go to your Vercel frontend project
2. Update environment variable:
   ```
   REACT_APP_API_URL: https://your-backend-url.onrender.com
   ```
3. Redeploy the frontend

## ✅ Step 4: Verify Deployment

### 4.1 Test Backend
- Visit: `https://your-backend-url.onrender.com/docs`
- Should show FastAPI documentation
- Test the health endpoint: `/`

### 4.2 Test Frontend
- Visit: `https://your-frontend-url.vercel.app`
- Should load the React application
- Test user registration and login

### 4.3 Test Full Integration
1. Register a new user
2. Create a project
3. Create tasks
4. Test time tracking
5. Verify all features work

## 🔧 Troubleshooting

### Common Issues

#### Backend Issues
- **Database Connection**: Ensure `DATABASE_URL` is correct
- **CORS Errors**: Update `CORS_ORIGINS` with your frontend URL
- **Build Failures**: Check Python version and dependencies

#### Frontend Issues
- **API Connection**: Verify `REACT_APP_API_URL` is correct
- **Build Errors**: Check Node.js version and dependencies
- **Environment Variables**: Ensure all variables are set in Vercel

### Debug Commands

#### Render Backend Logs
```bash
# View backend logs in Render dashboard
# Or use Render CLI if available
```

#### Vercel Frontend Logs
```bash
# View frontend logs in Vercel dashboard
# Or use Vercel CLI
vercel logs
```

## 📊 Monitoring

### Render Backend
- **Health Checks**: Monitor service health
- **Logs**: View application logs
- **Metrics**: Monitor performance

### Vercel Frontend
- **Analytics**: View user analytics
- **Performance**: Monitor Core Web Vitals
- **Deployments**: Track deployment history

## 🔄 Continuous Deployment

Both Vercel and Render will automatically redeploy when you push changes to your GitHub repository.

### Update Process
1. Make changes locally
2. Test locally: `docker-compose up`
3. Commit and push to GitHub
4. Automatic deployment to Vercel and Render

## 📝 Final URLs

After deployment, update your README with:

```markdown
## 🌐 Live Application

- **Frontend**: https://your-app.vercel.app
- **Backend API**: https://your-app.onrender.com
- **API Documentation**: https://your-app.onrender.com/docs
```

## 🎉 Success!

Your Project Management Dashboard is now live and accessible to users worldwide! 