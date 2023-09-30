# TODO

## Setup and Configuration

### Environment Variables

1. **Subtask:** Update the `.env.example` file with all required environment variables.
2. **Subtask:** Update the README with instructions on copying `.env.example` to `.env` and filling out the variables.

### Database Configuration

1. **Subtask:** Research options for a lightweight database (SQLite, PostgreSQL).
2. **Subtask:** Add chosen database to `poetry.lock`.
3. **Subtask:** Update README with database setup instructions.

## Must-Have Features

### OAuth2 Authentication

1. **Subtask:** Research Flask-OAuthlib as a potential OAuth2 implementation.
2. **Subtask:** Add OAuth2 routes.
3. **Subtask:** Store tokens in a database instead of a file.

### Fetch and Display Playlists

1. **Subtask:** Extend `SpotifyAPI` class to include a `get_playlists` method.
2. **Subtask:** Create a new route `/playlists` to display playlists.
3. **Subtask:** Fetch playlists in the new route and display them.

### Error Handling

1. **Subtask:** Implement try-except blocks for API calls.
2. **Subtask:** Add custom exception classes.
3. **Subtask:** Write a general error handler in Flask.

## Should-Have Features

### Testing

1. **Subtask:** Write unit tests for OAuth2 routes.
2. **Subtask:** Write unit tests for `get_playlists`.
3. **Subtask:** Create mock objects for testing the Spotify API.

### Pagination Support

1. **Subtask:** Add a `page` query parameter to the `/tracks` and `/playlists` routes.
2. **Subtask:** Implement pagination in `SpotifyAPI` methods.
3. **Subtask:** Update the frontend to allow page navigation.

### Code Quality

1. **Subtask:** Run code quality checks using `make lint`.
2. **Subtask:** Fix any issues reported by the linters.
3. **Subtask:** Set up a CI/CD pipeline with GitHub Actions.

## Could-Have Features

### Additional API Features

1. **Subtask:** Add a method in `SpotifyAPI` to fetch albums.
2. **Subtask:** Add a method in `SpotifyAPI` to fetch artist details.

### Frontend Improvements

1. **Subtask:** Research and choose a frontend library (React, Angular).
2. **Subtask:** Rewrite the frontend using the chosen library.
3. **Subtask:** Style the frontend using a CSS framework (Bootstrap, TailwindCSS).

## Won't-Have Features (for now)

1. **Subtask:** Document why real-time updates won't be implemented at this stage.
2. **Subtask:** Document why sharing capabilities won't be added at this stage.
