# Blog REST API with Django REST Framework

This is a **Blog API** built using **Django REST Framework (DRF)**. It provides endpoints to manage blog posts, authors, and categories. The API supports features like filtering blog posts by category, pagination, and more.

## Features

* **Author Management**: Create, read, and manage authors who write blogs.
* **Blog Management**: View published blog posts with pagination and filtering by category.
* **Category Management**: Manage categories for blogs and filter blogs based on category.
* **Pagination**: Supports pagination for blog list endpoints.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Hasan082/Complete_Blog_REST_API_Using_DRF
cd blog-api
```

### 2. Set up a virtual environment

It's recommended to use a virtual environment to isolate the project dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

* On **Windows**:

  ```bash
  venv\Scripts\activate
  ```
* On **Linux/Mac**:

  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set up the database

Make sure you have a database set up (e.g., SQLite, PostgreSQL). Then, run the following commands to apply migrations and create the necessary database tables:

```bash
python manage.py migrate
```

### 5. Create a superuser

To access the admin panel and add some initial data (like authors or categories), create a superuser:

```bash
python manage.py createsuperuser
```

### 6. Run the server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`.

### 7. Access Swagger UI

Once the server is running, you can access the Swagger UI for API documentation at:

```plaintext
http://127.0.0.1:8000/docs/
```

This will give you a visual interface to explore and test the API endpoints.

---

## API Endpoints

### Authors

* **GET /authors/**: List all authors.
* **GET /authors/{id}/**: Retrieve details of a specific author.

### Blogs

* **GET /blogs/**: List all published blogs, with optional filtering by category.
* **GET /blogs/{id}/**: Retrieve details of a specific blog.

### Categories

* **GET /categories/**: List all categories.
* **GET /categories/{id}/**: Retrieve details of a specific category.

---

## Project Structure

```
.
├── api/                        # Django app for the API
│   ├── migrations/
│   ├── models.py               # Models for Author, Blog, Category
│   ├── serializers.py          # DRF serializers
│   ├── views.py                # DRF viewsets
│   ├── urls.py                 # URL routing for the API
│   └── pagination.py           # Custom pagination for blogs
├── manage.py                   # Django management script
├── requirements.txt            # Project dependencies
├── settings.py                 # Django settings
└── README.md                   # Project documentation (this file)
```

---

## Usage

### 1. Author Viewset

* **List authors**: `GET /authors/`
* **Retrieve a specific author**: `GET /authors/{id}/`

### 2. Blog Viewset

* **List blogs** (only published blogs are listed by default):

  * `GET /blogs/`
  * You can filter by category by passing a `category` query parameter: `/blogs/?category={category_slug}`
* **Retrieve a specific blog**: `GET /blogs/{id}/`

### 3. Category Viewset

* **List categories**: `GET /categories/`
* **Retrieve a specific category**: `GET /categories/{id}/`

---

## Custom Pagination

The Blog API supports pagination using the `BlogPagination` class. By default, each page will return 5 blog posts, but you can customize the `page_size` by passing a query parameter `page_size`.

Example:

```plaintext
GET /blogs/?page_size=10
```

---

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:
* The Swagger UI is set up at /swagger/, using drf-spectacular, which automatically generates interactive API documentation based on your serializers and viewsets.

* The ReDoc documentation is available at /redoc/ for an alternative API documentation view.

* Pagination for the blog posts is handled using a custom pagination class in pagination.py.

* Make sure to test all endpoints and ensure your model relationships and migrations are properly set up.




