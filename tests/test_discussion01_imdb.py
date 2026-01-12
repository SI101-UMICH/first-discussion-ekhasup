import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import main

def test_get_movie_returns_dict():
    try:
        movie = main.get_movie("Inception")
    except Exception as e:
        assert False, (
            "Your program ran, but the TMDB API request did not succeed.\n\n"
            "Most common causes:\n"
            "- TMDB_API_KEY is empty\n"
            "- TMDB_API_KEY is incorrect\n"
            "- The key was pasted outside quotation marks\n"
            "- The file was not saved before committing\n\n"
            "What to do:\n"
            "1. Open main.py\n"
            "2. Paste your TMDB API key into TMDB_API_KEY\n"
            "3. Save the file\n"
            "4. Run the program again\n\n"
            f"Technical details (for reference):\n{e}"
        )

    assert isinstance(movie, dict), (
        "get_movie('Inception') should return a dictionary.\n"
        "If this failed, the TMDB request likely did not return movie data."
    )

def test_movie_title_is_inception():
    movie = main.get_movie("Inception")

    assert "title" in movie, (
        "The returned movie dictionary does not contain a 'title' key.\n"
        "Try printing the dictionary returned by get_movie to inspect it."
    )

    assert movie["title"] == "Inception", (
        "movie['title'] was not 'Inception'.\n"
        "Check that your TMDB API key is correct and that the request succeeded."
    )
