# LibraryProject

This is my first Django project created as part of the ALX Introduction to Django module.

## Description
LibraryProject is a starter Django setup that demonstrates how to initialize and run a Django development environment.

## Steps
1. Install Django using `pip install django`.
2. Start the project using `django-admin startproject LibraryProject`.
3. Run the development server using `python manage.py runserver`.

# LibraryProject

This Django project demonstrates advanced features and security by using a custom user model, permissions, and groups.

## Custom User Model

- App: `bookshelf`
- Model: `CustomUser` (extends `AbstractUser`)
- Fields: 
  - `date_of_birth`
  - `profile_photo`

## Groups and Permissions

### Groups

1. **Viewers**  
   - Permissions: `can_view`
   - Can only view Book instances.

2. **Editors**  
   - Permissions: `can_view`, `can_create`, `can_edit`
   - Can view, create, and edit Book instances.

3. **Admins**  
   - Permissions: all (view, create, edit, delete)
   - Full access.

### Custom Permissions for Book Model

- `can_view` – allows viewing books
- `can_create` – allows creating books
- `can_edit` – allows editing books
- `can_delete` – allows deleting books

## Enforcing Permissions

- Views in `bookshelf/views.py` use the `@permission_required` decorator to enforce access control.
- Example:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    ...
# Security Measures in LibraryProject

## Django Security Best Practices Implemented

1. **DEBUG=False** in production to prevent detailed error messages from being exposed.
2. **Browser Protections:**
   - `SECURE_BROWSER_XSS_FILTER=True`
   - `X_FRAME_OPTIONS='DENY'`
   - `SECURE_CONTENT_TYPE_NOSNIFF=True`
3. **Cookies Security:**
   - `CSRF_COOKIE_SECURE=True`
   - `SESSION_COOKIE_SECURE=True`
4. **CSRF Protection:** All forms include `{% csrf_token %}`.
5. **SQL Injection Prevention:** All database access uses Django ORM; user inputs are validated.
6. **Content Security Policy:** Configured via `django-csp` to restrict loaded resources.

