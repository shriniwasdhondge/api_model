# api_model

# Response API

## Project Overview
This project is a RESTful API for managing responses, including creating, retrieving, and filtering responses. The API is built using Django Rest Framework (DRF) and includes JWT authentication, rate limiting, caching, and pagination.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Django (>= 4.0)
- Django REST Framework
   SQLite for development
- Redis (for caching)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Rename `.env.example` to `.env`
   - Update database credentials and other settings

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the server:**
   ```bash
   python manage.py runserver
   ```

8. **Start Redis for caching:**
   ```bash
   redis-server
   ```

## API Documentation

### Authentication

**Obtain JWT Token:**
```http
POST /api/token/
```
**Refresh Token:**
```http
POST /api/token/refresh/
```

### Endpoints

#### List All Responses (with Pagination)
```http
GET /api/responses/
```
- Supports pagination with `?page=1&page_size=10`

#### Create a Response
```http
POST /api/responses/
```
**Request Body:**
```json
{
    "prompt": "Test prompt",
    "response_text": "Generated response",
    "model_used": "GPT-4",
    "processing_time": 1.5
}
```
**Response:** `201 Created`

#### Retrieve a Specific Response
```http
GET /api/responses/{id}/
```
**Response:** `200 OK`

#### Filter Responses by Model and Date Range
```http
GET /api/responses/?model_used=GPT-4&start_date=2024-01-01&end_date=2024-01-30
```

## Features Implemented
- ✅ **CRUD operations** for managing responses
- ✅ **JWT authentication** for secure access
- ✅ **Rate limiting** (5 requests per minute per IP)
- ✅ **Pagination** to handle large datasets
- ✅ **Response caching with Redis** for faster access
- ✅ **Filtering** by model and date range
- ✅ **Unit tests** for API reliability

## Technologies Used
- **Backend:** Django, Django REST Framework
- **Database:** ( SQLite for development)
- **Authentication:** JWT (Django SimpleJWT)
- **Caching:** Redis
- **Testing:** Django TestCase (Unit tests)
- **Other Tools:** Docker (optional for deployment)

## Running Tests
To ensure everything works correctly, run:
```bash
python manage.py test api
```

## Deployment
For deployment, use services like AWS, Heroku, or DigitalOcean. Recommended setup includes:
- Gunicorn as WSGI server
- Nginx as reverse proxy
- sqllite as database
- Redis for caching
- Docker for containerization


