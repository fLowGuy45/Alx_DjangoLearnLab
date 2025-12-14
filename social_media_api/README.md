# Social Media API

## Project Overview
A Django REST API for a social media platform with user authentication and profile management.

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd social_media_api


## Posts & Comments API

### Posts
- GET /api/posts/
- POST /api/posts/
- PUT /api/posts/{id}/
- DELETE /api/posts/{id}/

Search:


## User Follow & Feed API

### Follow a User
POST /api/accounts/follow/<user_id>/
Authorization required

### Unfollow a User
POST /api/accounts/unfollow/<user_id>/
Authorization required

### Get User Feed
GET /api/posts/feed/
Returns posts from followed users ordered by newest first.
