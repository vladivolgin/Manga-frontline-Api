from fastapi import FastAPI, HTTPException, Query
import requests

app = FastAPI()

MANGADEX_API_URL = "https://api.mangadex.org"


def fetch_manga_info(manga_id: str):
    """Info about manga by ID using MangaDex API"""
    url = f"{MANGADEX_API_URL}/manga/{manga_id}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    return response.json()


def search_manga_by_title(title: str):
    """Searching manga by title using MangaDex Api"""
    url = f"{MANGADEX_API_URL}/manga"
    params = {"title": title, "limit": 5, "order[relevance]": "desc"}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None
    return response.json()


@app.get("/manga/{manga_id}")
def get_manga_info(manga_id: str):
    """Getting info about manga by ID"""
    data = fetch_manga_info(manga_id)
    
    if not data:
        raise HTTPException(status_code=404, detail="Manga not found")
    
    manga_data = data.get("data", {})
    attributes = manga_data.get("attributes", {})
    
    return {
        "id": manga_id,
        "title": attributes.get("title", {}).get("en", "No title available"),
        "description": attributes.get("description", {}).get("en", "No description available"),
        "status": attributes.get("status", "Unknown"),
        "year": attributes.get("year"),
        "tags": [tag["attributes"]["name"]["en"] for tag in attributes.get("tags", [])],
        "original_language": attributes.get("originalLanguage"),
    }


@app.get("/search")
def search_manga(title: str = Query(..., description="Название манги для поиска")):
    """Getting info about manga by title"""
    search_result = search_manga_by_title(title)

    if not search_result or not search_result.get("data"):
        raise HTTPException(status_code=404, detail="No manga found with that title")

    manga_list = search_result["data"]
    return [
        {
            "id": manga["id"],
            "title": manga["attributes"]["title"].get("en", "No title available"),
            "original_language": manga["attributes"].get("originalLanguage", "N/A")
        }
        for manga in manga_list
    ]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

#curl "http://127.0.0.1:8000/search?title=Chainsaw Man"
