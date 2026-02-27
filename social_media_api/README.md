# Social Media API - Project Setup and User Authentication

This project implements the initial setup for a Social Media API using Django and Django REST Framework, with token-based authentication.

## Features Implemented

- Django project and `accounts` app setup
- Custom user model extending `AbstractUser`
- Extra user fields:
  - `bio`
  - `profile_picture`
  - `followers` (self-referencing `ManyToManyField`, `symmetrical=False`)
- Token authentication with `rest_framework.authtoken`
- API endpoints for:
  - User registration
  - User login
  - User profile retrieval/update

## Project Structure

- `social_media_api/social_media_api/settings.py`
- `social_media_api/social_media_api/urls.py`
- `social_media_api/accounts/models.py`
- `social_media_api/accounts/serializers.py`
- `social_media_api/accounts/views.py`
- `social_media_api/accounts/urls.py`
- `social_media_api/accounts/migrations/0001_initial.py`
- `social_media_api/accounts/migrations/0002_alter_user_followers.py`
- `social_media_api/accounts/migrations/0003_alter_user_groups_alter_user_user_permissions.py`

## Setup Instructions

1. Install dependencies:

```bash
pip install django djangorestframework
```

2. Move into project directory:

```bash
cd social_media_api
```

3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start development server:

```bash
python manage.py runserver
```

## API Endpoints

Base path: `/api/accounts/`

- `POST /register` - Create a user and return auth token
- `POST /login` - Authenticate and return auth token
- `GET /profile` - Retrieve authenticated user profile
- `PUT/PATCH /profile` - Update authenticated user profile

## Request/Response Examples

### Register

`POST /api/accounts/register`

```json
{
  "username": "alice",
  "email": "alice@example.com",
  "password": "StrongPass123",
  "bio": "Hello from Alice"
}
```

Response includes:
- `user` object
- `token`

### Login

`POST /api/accounts/login`

```json
{
  "username": "alice",
  "password": "StrongPass123"
}
```

Response includes:
- `user` object
- `token`

### Profile

Include token in header:

```text
Authorization: Token <your_token>
```

Then call:
- `GET /api/accounts/profile`
- `PATCH /api/accounts/profile`
