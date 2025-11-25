# Advanced API Project — Custom Views and Generic Views

## Views Implemented
- **BookListView** — List all books (public)
- **BookDetailView** — Retrieve single book (public)
- **BookCreateView** — Create new book (authenticated)
- **BookUpdateView** — Update existing book (authenticated)
- **BookDeleteView** — Delete book (authenticated)

## Customizations
- Integrated permissions using DRF permission classes
- Added custom hooks (`perform_create`, `perform_update`)
- Auto-validation through the serializer

## Endpoints
- `GET /api/books/`
- `GET /api/books/<id>/`
- `POST /api/books/create/`
- `PUT /api/books/<id>/update/`
- `DELETE /api/books/<id>/delete/`



## Filtering, Searching, and Ordering

### Filtering
Use query parameters:
- `?title=`
- `?author=`
- `?publication_year=`

Example:
`GET /api/books/?author=2`

### Searching
Search across title and author name:
`GET /api/books/?search=django`

### Ordering
Order results using:
- `?ordering=title`
- `?ordering=-publication_year`

Example:
`GET /api/books/?ordering=-title`
