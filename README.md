# Django Blog Application

## Setup

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies
   ```bash
   pip install -r requirements.txt
  
4. After installing dependencies apply makemigrations and migrate if you want to use new DB

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


### User Authentication Endpoints with body parameters

- **User Signup**
  - `POST /api/signup/`
  - **Body**: `{ "username": "user", "email": "user@example.com", "password": "password" }`

- **User Login**
  - `POST /api/login/`
  - **Body**: `{ "username": "user", "password": "password" }`
  - After login in response wil get refresh token and access token use access token to access blow API end points. 


### Posts Endpoints with body parameters

- **List Posts**
  - `GET /api/posts/`
  
- **Create Post**
  - `POST /api/posts/`
  - **Body**: `{ "title": "Post Title", "content": "Post Content" }`

- **Retrieve Post**
  - `GET /api/posts/{id}/`

- **Update Post**
  - `PUT /api/posts/{id}/`
  - **Body**: `{ "title": "Updated Title", "content": "Updated Content" }`

- **Delete Post**
  - `DELETE /api/posts/{id}/`

- **Like Post**
  - `POST /api/posts/{id}/like/`
  - **Response**: `{ "status": "liked" }` or `{ "status": "unliked" }`

### Comments Endpoints with body parameters

- **List Comments**
  - `GET /api/posts/{post_id}/comments/`

- **Create Comment**
  - `POST /api/posts/{post_id}/comments/`
  - **Body**: `{ "text": "Comment Text" }`


### Swagger API URL
- **Swagger**
  -api/swagger/
  - Past url `Past url in your browser like {localhost}api/swagger/`
  - To access Swagger need to signup and login to get access token
  - Click on Authorize and post user Access token like `Bearer {then token}`
  - Now you can access any API endpoint