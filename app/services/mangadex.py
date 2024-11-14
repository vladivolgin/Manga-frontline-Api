import logging
from typing import List, Dict, Any, Optional
import requests
from app.config import settings
from app.models.manga import MangaInfo, MangaSearchResult
from pydantic import BaseModel

class MangaDexService:
    @staticmethod
    def fetch_manga_info(manga_id: str) -> Optional[Dict]:
        url = f"{settings.MANGADEX_API_URL}/manga/{manga_id}"
        logging.info(f"Fetching manga info from URL: {url}")
        try:
            response = requests.get(url)
            logging.info(f"Response status code: {response.status_code}")
            response.raise_for_status()
            data = response.json()
            logging.info(f"Received data: {data}")
            return data
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            if response.status_code == 404:
                logging.warning(f"Manga with ID {manga_id} not found.")
                return None
            raise
        except Exception as err:
            logging.error(f"Unexpected error occurred: {err}")
            raise

    @staticmethod
    def search_manga_by_title(title: str) -> Dict:
        url = f"{settings.MANGADEX_API_URL}/manga"
        params = {"title": title, "limit": 5, "order[relevance]": "desc"}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()      
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error searching manga: {e}", exc_info=True)
            raise

    @staticmethod
    def parse_manga_search_results(data: List[Dict]) -> List[MangaSearchResult]:
        manga_list = data.get("data", [])
        logging.info(f"Parsing {len(manga_list)} manga results")
        results = []
        for manga in manga_list:
            try:
                result = MangaSearchResult(
                    id=manga.get("id"),
                    title=manga.get("attributes", {}).get("title", {}).get("en", "No title available"),
                    original_language=manga.get("attributes", {}).get("originalLanguage", "N/A")
                )
                results.append(result)
            except Exception as e:
                logging.error(f"Error parsing manga data: {e}", exc_info=True)
        logging.info(f"Successfully parsed {len(results)} manga results")
        return results

    @staticmethod
    def parse_manga_info(data: dict) -> MangaInfo:
        manga_data = data.get("data", {})
        attributes = manga_data.get("attributes", {})
        return MangaInfo(
            id=manga_data.get("id"),
            title=attributes.get("title", {}).get("en", "No title available"),
            description=attributes.get("description", {}).get("en", "No description available"),
            status=attributes.get("status", "Unknown"),
            year=attributes.get("year"),
            tags=[tag.get("attributes", {}).get("name", {}).get("en", "Unknown") for tag in attributes.get("tags", [])],
            original_language=attributes.get("originalLanguage")
        )

class MangaSearchResult(BaseModel):
    id: str
    title: str
    original_language: str