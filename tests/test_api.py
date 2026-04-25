import pytest
from fastapi.testclient import TestClient

from app.data import QUESTIONS
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


class TestHomePage:
    def test_home_returns_200(self, client: TestClient):
        response = client.get("/")
        assert response.status_code == 200

    def test_home_contains_start_screen(self, client: TestClient):
        response = client.get("/")
        assert "Soc Ops" in response.text
        assert "Start Game" in response.text
        assert "How to play" in response.text

    def test_home_sets_session_cookie(self, client: TestClient):
        response = client.get("/")
        assert "session" in response.cookies


class TestStartGame:
    def test_start_returns_game_board(self, client: TestClient):
        # First visit to get session
        client.get("/")
        response = client.post("/start")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
        assert "← Back" in response.text

    def test_board_has_25_squares(self, client: TestClient):
        client.get("/")
        response = client.post("/start")
        # Count the toggle buttons (squares with hx-post="/toggle/")
        assert response.text.count('hx-post="/toggle/') == 24  # 24 + 1 free space


class TestToggleSquare:
    def test_toggle_marks_square(self, client: TestClient):
        client.get("/")
        client.post("/start")
        response = client.post("/toggle/0")
        assert response.status_code == 200
        # The response should contain the game screen with a marked square


class TestStartHunt:
    def test_start_hunt_returns_hunt_screen(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert response.status_code == 200
        assert "Hunt Mode" in response.text
        assert "Mission List" in response.text
        assert "← Back" in response.text

    def test_hunt_checklist_has_24_items(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        # Count checkboxes (hx-post="/toggle-hunt/")
        assert response.text.count('hx-post="/toggle-hunt/') == 24

    def test_hunt_progress_starts_at_zero(self, client: TestClient):
        client.get("/")
        response = client.post("/start-hunt")
        assert "0%" in response.text


class TestToggleHuntItem:
    def test_toggle_hunt_item_updates_progress(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        response = client.post("/toggle-hunt/0")
        assert response.status_code == 200
        # Progress should be 4.17% (1/24 ≈ 4.17)
        assert "4%" in response.text or "5%" in response.text  # Approximate

    def test_toggle_hunt_item_twice_resets(self, client: TestClient):
        client.get("/")
        client.post("/start-hunt")
        client.post("/toggle-hunt/0")  # Check
        response = client.post("/toggle-hunt/0")  # Uncheck
        assert "0%" in response.text


class TestStartCard:
    def test_start_card_returns_card_screen(self, client: TestClient):
        client.get("/")
        response = client.post("/start-card")
        assert response.status_code == 200
        assert "Card Deck" in response.text
        assert "Shuffle" in response.text
        assert "← Back" in response.text

    def test_card_screen_has_one_question(self, client: TestClient):
        client.get("/")
        response = client.post("/start-card")
        # Should contain one question from QUESTIONS
        question_found = any(q in response.text for q in QUESTIONS)
        assert question_found


class TestShuffleCard:
    def test_shuffle_card_returns_new_card(self, client: TestClient):
        client.get("/")
        client.post("/start-card")
        first_response = client.post("/start-card")  # Get first card
        second_response = client.post("/shuffle-card")
        assert second_response.status_code == 200
        # Questions should be different (high probability)
        assert first_response.text != second_response.text

    def test_shuffle_card_keeps_card_screen(self, client: TestClient):
        client.get("/")
        client.post("/start-card")
        response = client.post("/shuffle-card")
        assert "Card Deck" in response.text
        assert "Shuffle" in response.text


class TestResetGame:
    def test_reset_returns_start_screen(self, client: TestClient):
        client.get("/")
        client.post("/start")
        response = client.post("/reset")
        assert response.status_code == 200
        assert "Start Game" in response.text
        assert "How to play" in response.text


class TestDismissModal:
    def test_dismiss_returns_game_screen(self, client: TestClient):
        client.get("/")
        client.post("/start")
        response = client.post("/dismiss-modal")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
