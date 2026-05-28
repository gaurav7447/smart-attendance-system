# Smart Attendance System using AWS

## 📌 Project Overview

Smart Attendance System is a cloud-based AI-powered attendance management application built using AWS Serverless services.

The system uses:

* Face Recognition using AWS Rekognition
* GPS Geofencing
* Serverless Backend with AWS Lambda
* DynamoDB for attendance storage
* S3 for image storage and frontend hosting
* API Gateway for REST APIs
* GitHub Actions for CI/CD pipeline

This project demonstrates a complete AWS + DevOps workflow with automated deployment.

---

# 🚀 Features

✅ User Registration
✅ Live Camera Face Capture
✅ Upload Existing Image
✅ AI Face Recognition Attendance
✅ GPS-Based Geofencing
✅ Duplicate Attendance Prevention
✅ Attendance Dashboard
✅ Public Frontend Hosting
✅ CI/CD Pipeline using GitHub Actions
✅ Responsive Modern UI

---

# 🏗️ AWS Services Used

| AWS Service    | Purpose                          |
| -------------- | -------------------------------- |
| AWS Lambda     | Serverless backend               |
| API Gateway    | REST API endpoints               |
| DynamoDB       | Attendance & user database       |
| S3             | Image storage & frontend hosting |
| Rekognition    | Face recognition                 |
| IAM            | Access management                |
| GitHub Actions | CI/CD automation                 |

---

# 🧠 System Architecture

```text
Frontend (HTML/CSS/JS)
        ↓
AWS S3 Static Hosting
        ↓
API Gateway
        ↓
AWS Lambda Functions
        ↓
DynamoDB + Rekognition + S3
```

---

# 📂 Project Structure

```text
smart-attendance-system/
│
├── frontend/
│   ├── index.html
│   ├── register.html
│   ├── attendance.html
│   ├── dashboard.html
│   └── style.css
│
├── backend/
│   ├── register-face/
│   ├── mark-attendance/
│   └── get-attendance/
│
└── .github/
    └── workflows/
        └── deploy.yml
```

---

# ⚙️ Features Explanation

## 1️⃣ User Registration

Users can:

* Capture live image from webcam
* Upload image from device

Images are stored in S3 and indexed in AWS Rekognition.

---

## 2️⃣ Face Recognition Attendance

During attendance:

* Live image is captured
* Face matched using AWS Rekognition
* Attendance stored in DynamoDB

---

## 3️⃣ GPS Geofencing

Attendance is only allowed inside configured location radius.

If user is outside allowed location:

```text
Outside allowed location
```

---

## 4️⃣ Duplicate Attendance Prevention

System prevents multiple attendance entries for same user on same day.

---

## 5️⃣ Dashboard

Attendance dashboard displays:

* Name
* Profession
* Date
* Time
* Status
* Location

---

# 🌐 Frontend Hosting

Frontend is hosted using AWS S3 Static Website Hosting.

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically deploys frontend changes to AWS S3.

Workflow:

```text
Code Push → GitHub Actions → AWS S3 Deployment
```

---

# 🛠️ Technologies Used

* HTML
* CSS
* JavaScript
* Python
* AWS Lambda
* AWS Rekognition
* AWS DynamoDB
* AWS S3
* GitHub Actions

---
🚀 Live Demo

🔗 Live Application:

http://smart-attendance-frontend-7447.s3-website.ap-south-1.amazonaws.com

---

# 🔐 Security Features

* IAM-based access control
* Geofencing validation
* Face recognition verification
* Duplicate attendance prevention

---

# 📈 Future Improvements

* HTTPS using CloudFront
* Admin Authentication
* Attendance Analytics
* Export Reports
* Mobile Application
* Email Notifications
* Real-time Monitoring

---

# 👨‍💻 Author

Gaurav Deshmane

---

# ⭐ Project Status

✅ Completed
✅ Deployed on AWS
✅ CI/CD Enabled
✅ Production-Style Architecture
