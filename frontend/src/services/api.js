import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle auth errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Auth API
export const authAPI = {
  login: (credentials) => {
    // Convert to URL-encoded form data for OAuth2PasswordRequestForm
    const formData = new URLSearchParams();
    formData.append('username', credentials.username);
    formData.append('password', credentials.password);
    return api.post('/auth/login', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
  },
  register: (userData) => api.post('/auth/register', userData),
};

// Projects API
export const projectsAPI = {
  getAll: (params) => api.get('/projects', { params }),
  getById: (id) => api.get(`/projects/${id}`),
  create: (projectData) => api.post('/projects', projectData),
  update: (id, projectData) => api.put(`/projects/${id}`, projectData),
  delete: (id) => api.delete(`/projects/${id}`),
};

// Tasks API
export const tasksAPI = {
  getAll: (params) => api.get('/tasks', { params }),
  getById: (id) => api.get(`/tasks/${id}`),
  create: (taskData) => api.post('/tasks', taskData),
  update: (id, taskData) => api.put(`/tasks/${id}`, taskData),
  delete: (id) => api.delete(`/tasks/${id}`),
  getMyTasks: (params) => api.get('/tasks/my-tasks', { params }),
  getMyTaskStats: () => api.get('/tasks/my-tasks/stats'),
  getTimeLogs: (taskId) => api.get(`/tasks/${taskId}/time-logs`),
  createTimeLog: (taskId, timeLogData) => api.post(`/tasks/${taskId}/time-logs`, timeLogData),
};

// Comments API
export const commentsAPI = {
  create: (commentData) => api.post('/comments', commentData),
  getTaskComments: (taskId) => api.get(`/comments/task/${taskId}`),
  getProjectComments: (projectId) => api.get(`/comments/project/${projectId}`),
  update: (commentId, commentData) => api.put(`/comments/${commentId}`, commentData),
  delete: (commentId) => api.delete(`/comments/${commentId}`),
};

// Users API
export const usersAPI = {
  getCurrentUser: () => api.get('/users/me'),
  updateCurrentUser: (userData) => api.put('/users/me', userData),
  getAll: (params) => api.get('/users', { params }),
};

// Time Log API
export const timelogAPI = {
  createTimeLog: (timeLogData) => api.post('/timelog', timeLogData),
  getTimeLogs: (filters = {}) => api.get('/timelog', { params: filters }),
  getTimeLog: (id) => api.get(`/timelog/${id}`),
  updateTimeLog: (id, timeLogData) => api.put(`/timelog/${id}`, timeLogData),
  deleteTimeLog: (id) => api.delete(`/timelog/${id}`),
  getTimeSummary: (userId, filters = {}) => api.get(`/timelog/summary/user/${userId}`, { params: filters }),
};

export default api; 