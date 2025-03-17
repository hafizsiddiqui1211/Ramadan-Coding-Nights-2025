# FastAPI Side Hustles & Money Quotes API

This is a simple FastAPI application that provides two GET endpoints:
- `/side_hustles`: Returns a random side hustle idea.
- `/money_quotes`: Returns a random money-related quote.

## Features
- Uses FastAPI to create lightweight API endpoints.
- Implements basic API key authentication.
- Returns random responses from predefined lists.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

## Running the Application

Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```

## API Endpoints

### 1. Get a Side Hustle Idea
**Endpoint:** `GET /side_hustles`

**Query Parameters:**
- `apikey` (string, required): API key to authenticate the request.

**Example Request:**
```
GET http://127.0.0.1:8000/side_hustles?apikey=123456789
```

**Example Response:**
```json
{
  "side-hustle": "Freelancing - Start offering your skills online!"
}
```

### 2. Get a Money Quote
**Endpoint:** `GET /money_quotes`

**Query Parameters:**
- `apikey` (string, required): API key to authenticate the request.

**Example Request:**
```
GET http://127.0.0.1:8000/money_quotes?apikey=123456789
```

**Example Response:**
```json
{
  "money_quote": "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett"
}
```

## Notes
- The API requires an API key (`123456789`) for authentication.
- The endpoint `/money_quotews` has a typo in the original code; it should be corrected to `/money_quotes`.

## License
This project is open-source and available under the MIT License.

