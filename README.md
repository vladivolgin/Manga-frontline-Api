# Manga-frontline-Api

This project is a FastAPI-based wrapper for the MangaDex API, allowing users to search for manga and retrieve detailed information about specific titles.

## Features

- Search for manga by title
- Retrieve detailed information about a specific manga by its ID
- RESTful API design
- Swagger UI documentation

## Setup and Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Setting up the development environment

1. Clone the repository:

git clone https://github.com/vladivolgin/Manga-frontline-Api

2. Create a virtual environment:
```
python -m venv venv
```
3. Install the required dependencies:
```
pip install -r requirements.txt or pip3 install -r requirements.txt
```
### Running the application

1. Start the FastAPI server:
```
python -m app.main or python3 -m app.main
```
2. Open your web browser and navigate to `http://127.0.0.1:8000/docs` to view the Swagger UI documentation and interact with the API.

## Usage

### Searching for manga

To search for manga by title, send a GET request to `/api/v1/search` with the `title` query parameter:
```
curl "http://127.0.0.1:8000/api/v1/search?title=<title>"
```
(Some examples of Manga titles: 'One Piece', 'Naruto', 'Berserk')

### Retrieving manga details

To get detailed information about a specific manga, send a GET request to `/api/v1/manga/{manga_id}`:
```
curl "http://127.0.0.1:8000/api/v1/manga/{manga_id}"
```
 (You can get manga id by searching manga with the name of title)

## Project Structure
```
manga_api/
├── app/                        # Main application package
│   ├── init.py
│   ├── main.py                 # Entry point of the application
│   ├── config.py               # Configuration settings 
│   ├── api/                    # API routes
│   │   ├── init.py
│   │   └── manga.py            # Manga-related endpoints
│   ├── services/               # Business logic
│   │   ├── init.py
│   │   └── mangadex.py         # MangaDex API interaction
│   └── models/                 # Data models
│       ├── init.py
│       └── manga.py            # Manga data models
├── tests/                      # Test directory
│   ├── init.py
│   ├── test_manga_api.py       # API tests
│   └── test_mangadex_service.py    # Service tests
├── .env                        # Environment variables (not in version control)
└── requirements.txt            # Project dependencies
```

## Code Analysis and Quality Tools

This project uses the following tools to maintain code quality:

- **Pytest**: For unit and integration testing. Run tests with `pytest tests/`.
- **Flake8**: For style guide enforcement. Run with `flake8 .`.
- **Black**: For code formatting. Run with `black .`.

To run all quality checks, you can use the following command:
pytest tests/ && flake8 . && black --check .

## Testing

To run tests and ensure the API is working correctly, follow these instructions:

### Running Tests

To run all tests, use the command:
```
pytest
```

