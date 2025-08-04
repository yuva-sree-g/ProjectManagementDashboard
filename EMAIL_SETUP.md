# Email Notification Setup

## 📧 Email Configuration

This application supports email notifications for task assignments and updates. To enable email notifications, you need to configure SMTP settings.

## 🔧 Environment Variables

Add these environment variables to your Render backend service:

```
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_FROM=your-email@gmail.com
FRONTEND_URL=https://project-management-dashboard-dno2.vercel.app
```

## 📧 Gmail Setup (Recommended)

### Step 1: Enable 2-Factor Authentication
1. Go to your Google Account settings
2. Enable 2-Factor Authentication

### Step 2: Generate App Password
1. Go to Google Account → Security
2. Click "App passwords"
3. Generate a new app password for "Mail"
4. Use this password as `MAIL_PASSWORD`

### Step 3: Update Environment Variables
```
MAIL_USERNAME=your-gmail@gmail.com
MAIL_PASSWORD=your-16-digit-app-password
MAIL_FROM=your-gmail@gmail.com
```

## 🎯 Email Notifications

The application sends emails for:

### 1. Task Assignment
- **When:** A task is assigned to a user
- **Recipients:** The assigned user
- **Content:** Task details, project name, assigned by

### 2. Task Updates
- **When:** Task status, description, or other fields are updated
- **Recipients:** The task assignee
- **Content:** Update type, task details, updated by

### 3. Task Completion
- **When:** Task status is changed to "completed"
- **Recipients:** The task assignee
- **Content:** Completion notification, project details

## 🔧 Alternative Email Providers

### Outlook/Hotmail
```
MAIL_SERVER=smtp-mail.outlook.com
MAIL_PORT=587
```

### Yahoo Mail
```
MAIL_SERVER=smtp.mail.yahoo.com
MAIL_PORT=587
```

### Custom SMTP
```
MAIL_SERVER=your-smtp-server.com
MAIL_PORT=587
MAIL_USERNAME=your-username
MAIL_PASSWORD=your-password
```

## 🧪 Testing Email Notifications

1. **Create a task** and assign it to a user with a valid email
2. **Update the task** status or description
3. **Check the user's email** for notifications

## ⚠️ Troubleshooting

### Common Issues:
1. **Authentication failed:** Check app password
2. **Connection timeout:** Verify SMTP settings
3. **Emails not sending:** Check environment variables

### Debug Mode:
Email sending errors are logged to console but don't break the application.

## 📝 Email Templates

The application uses HTML email templates with:
- Professional styling
- Task details
- Direct links to the application
- Responsive design

**Note:** Email notifications are sent asynchronously to avoid blocking the API response. 