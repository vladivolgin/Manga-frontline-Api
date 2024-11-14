from app.services.mangadex import MangaDexService
from app.models.manga import MangaInfo, MangaSearchResult

def test_search_manga_by_title():
    results = MangaDexService.search_manga_by_title("Naruto")
    assert isinstance(results, dict)
    assert "data" in results
    assert isinstance(results["data"], list)
    assert len(results["data"]) > 0
    for manga in results["data"]:
        assert "id" in manga
        assert "attributes" in manga
        assert "title" in manga["attributes"] 


