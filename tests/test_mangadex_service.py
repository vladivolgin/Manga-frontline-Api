from app.services.mangadex import MangaDexService
from app.models.manga import MangaInfo, MangaSearchResult

def test_search_manga_by_title():
    results = MangaDexService.search_manga_by_title("Naruto")
    assert isinstance(results, list)
    assert len(results) > 0
    assert all(isinstance(result, dict) for result in results)  


def test_parse_manga_info():
    mock_data = {
        "data": {
            "id": "test_id",
            "attributes": {
                "title": {"en": "Test Manga"},
                "description": {"en": "Test Description"},
                "status": "ongoing",
                "year": 2021,
                "tags": [{"attributes": {"name": {"en": "Action"}}}],
                "originalLanguage": "ja"
            }
        }
    }
    result = MangaDexService.parse_manga_info(mock_data)
    assert isinstance(result, MangaInfo)
    assert result.id == "test_id"
    assert result.title == "Test Manga"
    assert result.year == 2021
    assert "Action" in result.tags

def test_parse_manga_search_results():
    mock_data = {
        "data": [
            {
                "id": "test_id_1",
                "attributes": {
                    "title": {"en": "Test Manga 1"},
                    "originalLanguage": "ja"
                }
            },
            {
                "id": "test_id_2",
                "attributes": {
                    "title": {"en": "Test Manga 2"},
                    "originalLanguage": "ko"
                }
            }
        ]
    }
    results = MangaDexService.parse_manga_search_results(mock_data)
    assert len(results) == 2
    assert all(isinstance(result, MangaSearchResult) for result in results)
    assert results[0].id == "test_id_1"
    assert results[1].title == "Test Manga 2"