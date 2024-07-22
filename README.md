# Django Blog Application

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies
   ```bash
   pip install -r requirements.txt

## API Endpoints
1. POST /api/posts/: Create a new post
2. GET /api/posts/: List all posts
3. GET /api/posts/<id>/: Retrieve a single post
4. PUT /api/posts/<id>/: Update a post
5. DELETE /api/posts/<id>/: Delete a post
6. POST /api/posts/<post_id>/comments/: Create a new comment
7. GET /api/posts/<post_id>/comments/: List all comments for a post
8. POST /api/signup/`: User signup
9. POST /api/login/`: User login with email and password (returns JWT token)
10. POST /api/token/refresh/`: Refresh JWT token