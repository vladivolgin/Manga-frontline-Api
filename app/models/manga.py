from pydantic import BaseModel
from typing import List, Optional

class MangaInfo(BaseModel):
    id: str
    title: str
    description: str
    status: str
    year: int | None
    tags: List[str]
    original_language: str

class MangaSearchResult(BaseModel):
    id: str
    title: str
    original_language: str