# TODO

## Setup and Configuration

### Environment Variables

- Subtask: [Done] Update the .env.example file with all required environment variables.
    - Created .env.example with SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET

- Subtask: Update the README with instructions on copying .env.example to .env and filling out the variables.
    - Note: Consider automating this with a script.

- Subtask: [New, Done] Create a script to populate .env file from user input.
    - Script asks for SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET
    - Validations added for variable length
    - Quotes stripped if added

- Subtask: [New] Rename setup script to `dev_environment_setup.py`
    - Done: Renamed to better indicate its purpose for development environment setup

- Subtask: [New] Update test coverage to include `dev_environment_setup.py`
    - Done: Modified `--cov` arg to include the script, improving visibility on its test coverage


Database Configuration

    Subtask: Research options for a lightweight database (SQLite, PostgreSQL).
    Subtask: Add chosen database to poetry.lock.
    Subtask: Update README with database setup instructions.

Must-Have Features
OAuth2 Authentication

    Subtask: Research Flask-OAuthlib as a potential OAuth2 implementation.
    Subtask: Add OAuth2 routes.
    Subtask: Store tokens in a database instead of a file.

Fetch and Display Playlists

    Subtask: Extend SpotifyAPI class to include a get_playlists method.
    Subtask: Create a new route /playlists to display playlists.
    Subtask: Fetch playlists in the new route and display them.

Error Handling

    Subtask: Implement try-except blocks for API calls.
    Subtask: Add custom exception classes.
    Subtask: Write a general error handler in Flask.

Should-Have Features
Testing

    Subtask: [New, Partially Done] Write unit tests for .env setup script.
        Tested function that checks variable length
    Subtask: Write unit tests for OAuth2 routes.
    Subtask: Write unit tests for get_playlists.
    Subtask: Create mock objects for testing the Spotify API.

Pagination Support

    Subtask: Add a page query parameter to the /tracks and /playlists routes.
    Subtask: Implement pagination in SpotifyAPI methods.
    Subtask: Update the frontend to allow page navigation.

Code Quality

    Subtask: Run code quality checks using make lint.
    Subtask: Fix any issues reported by the linters.
    Subtask: Set up a CI/CD pipeline with GitHub Actions.

Could-Have Features
Additional API Features

    Subtask: Add a method in SpotifyAPI to fetch albums.
    Subtask: Add a method in SpotifyAPI to fetch artist details.

Frontend Improvements

    Subtask: Research and choose a frontend library (React, Angular).
    Subtask: Rewrite the frontend using the chosen library.
    Subtask: Style the frontend using a CSS framework (Bootstrap, TailwindCSS).

Won't-Have Features (for now)

    Subtask: Document why real-time updates won't be implemented at this stage.
    Subtask: Document why sharing capabilities won't be added at this stage.

Let me know if this captures all the details or if there's anything more you'd like to add.
