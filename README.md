# CampusVlog Publishing Platform

A Django-based content publishing and management platform designed for creating, organizing, and displaying multilingual articles across multiple categories. The system provides an efficient workflow for content creation, article management, image handling, and category-based navigation.

## Overview

CampusVlog Publishing Platform is a full-stack web application that enables administrators and content creators to publish articles, manage media files, and organize content through a structured category system. The platform supports multiple languages and offers a responsive user experience for readers.

## Features

* Content Management System (CMS)
* Article creation and publishing
* Category and subcategory management
* Multilingual content support
* Image upload and media management
* Dynamic article listing and filtering
* Responsive user interface
* SEO-friendly content structure
* Admin dashboard for content management
* Database-driven content delivery

## Technology Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Database

* SQLite

### Additional Libraries

* Pillow (Image Processing)
* WhiteNoise (Static File Management)
* Gunicorn (Production Server)

## Project Structure

```text
campusvlog/
├── campusvlog/          # Project configuration
├── home/                # Main application
├── static/              # Static assets
├── templates/           # HTML templates
├── media/               # Uploaded media files
├── manage.py
├── requirements.txt
└── Procfile
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/ahammed-ajmal/campusvlog.git 
cd campusvlog-publishing-platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Key Learning Outcomes

This project demonstrates:

* Full-Stack Web Development
* Django Framework Development
* Database Design and Management
* CRUD Operations
* Content Management Systems
* Media Handling
* Responsive Web Design
* MVC/MVT Architecture
* Deployment Configuration

## Future Enhancements

* User authentication and authorization
* Rich text editor integration
* Comment system
* Search functionality
* Article analytics dashboard
* REST API integration
* Social media sharing
* Email notifications

## Author

Developed by ahammed-ajmal

## License

This project is intended for educational and portfolio purposes.
