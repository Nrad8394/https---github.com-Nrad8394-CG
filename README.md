# Electronic Tracking System

This project is a Django-based web application for electronic tracking and management. It provides user authentication, order management, and administrative features, leveraging a modern UI with Bootstrap and various JavaScript plugins.

## Features
- User authentication (custom backend and middleware)
- Order management and tracking
- Admin dashboard
- Responsive UI with Bootstrap
- Data visualization and advanced table features

## Project Structure
- `base/` - Main Django app with models, views, templates, and custom authentication logic
- `electronic_tracking/` - Django project configuration (settings, URLs, WSGI/ASGI)
- `static/` - Static files (CSS, JS, images, plugins)
- `templates/` - HTML templates for the web interface
- `db.sqlite3` - SQLite database (default for development)
- `manage.py` - Django management script
- `Requirements.txt` - Python dependencies

## Setup Instructions

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```powershell
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Install dependencies:**
   ```powershell
   pip install -r Requirements.txt
   ```
3. **Apply migrations:**
   ```powershell
   python manage.py migrate
   ```
4. **Create a superuser (admin):**
   ```powershell
   python manage.py createsuperuser
   ```
5. **Run the development server:**
   ```powershell
   python manage.py runserver
   ```
6. **Access the app:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage
- Log in with your credentials or as an admin.
- Use the dashboard to manage and track orders.
- Access the admin panel at `/admin/` for advanced management.

## Customization
- Update static files in the `static/` directory for UI changes.
- Modify templates in the `templates/` directory for layout/content changes.
- Add or update models, views, and URLs in the `base/` app as needed.

## License
This project is licensed under the MIT License.

## Contact
For questions or support, please open an issue or contact the project maintainer.
