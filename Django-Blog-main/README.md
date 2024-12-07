
# Django Blog Application

A simple and elegant blog application built with Django, featuring articles, authors, and a user-friendly interface. This project demonstrates the use of Django's powerful features for managing content and user interactions.

## Features

- **Article Management**: Create, read, update, and delete articles.
- **Author Management**: Manage authors and view their published articles.
- **Responsive Design**: A modern, sleek UI that works well on both desktop and mobile devices.
- **CSRF Protection**: Secure forms with CSRF tokens for safe data submission.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite
- **Version Control**: Git

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/django-blog.git
   cd django-blog
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (to access the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Visit** `http://127.0.0.1:8000/` in your browser.

## Usage

- Navigate to the home page to view the latest articles.
- Click on an article title to view the full content.
- Manage authors and articles via the admin panel (accessible at `/admin`).

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any feature requests or bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/) for the framework.
- Various online resources for tutorials and best practices.
