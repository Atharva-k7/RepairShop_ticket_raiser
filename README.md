# Electronic Repair Shop — Ticket Management System

A Django CRUD application to manage repair tickets for an electronics repair shop.
Built for AAI LAB - CCA1 (Django Project, Basic CRUD Operations).

## Features
- Create, view, update, and delete repair tickets
- Filter tickets by status (Open, In Progress, Waiting for Parts, Completed, Cancelled)
- Django admin panel for backend management
- Fields: customer details, device type/model, issue description, status, estimated cost, dates

## Tech Stack
- Python 3
- Django 5.x
- SQLite (default Django DB)

## Setup Instructions

1. Clone the repository
   ```
   git clone <your-repo-url>
   cd repairshop_project
   ```

2. Create and activate a virtual environment
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run migrations
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (for admin panel access)
   ```
   python manage.py createsuperuser
   ```

6. Run the development server
   ```
   python manage.py runserver
   ```

7. Open in browser
   - App: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Project Structure
```
repairshop_project/
├── manage.py
├── requirements.txt
├── repairshop_project/     # project settings
└── tickets/                # CRUD app
    ├── models.py           # RepairTicket model
    ├── views.py             # CRUD views
    ├── forms.py             # ModelForm
    ├── urls.py
    ├── admin.py
    └── templates/tickets/   # list, form, detail, delete templates
```

## Screenshots
See attached PDF for screenshots of the list, create, edit, and delete views.
