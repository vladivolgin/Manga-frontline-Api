from fastapi import APIRouter, HTTPException, Query
import logging
from typing import List
import requests
from app.services.mangadex import MangaDexService
from app.models.manga import MangaInfo
from app.models.manga import MangaInfo, MangaSearchResult

router = APIRouter()

@router.get("/manga/{manga_id}", response_model=MangaInfo)
def get_manga_info(manga_id: str):
    try:
        data = MangaDexService.fetch_manga_info(manga_id)
        if not data:
            raise HTTPException(status_code=404, detail="Manga not found")
        
        manga_info = MangaDexService.parse_manga_info(data)
        return manga_info
    
    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 404:
            raise HTTPException(status_code=404, detail="Manga not found")
        logging.error(f"HTTP error occurred: {http_err}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    except HTTPException as http_exc:
        raise http_exc
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/search", response_model=List[MangaSearchResult])
def search_manga(title: str = Query(..., description="Manga Title for searching")):
    try:
        search_result = MangaDexService.search_manga_by_title(title)
        if not search_result:
            return []
        return MangaDexService.parse_manga_search_results(search_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching manga: {str(e)}")