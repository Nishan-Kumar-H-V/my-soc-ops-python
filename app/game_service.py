from dataclasses import dataclass, field

from app.game_logic import (
    calculate_hunt_progress,
    check_bingo,
    draw_random_card,
    generate_board,
    generate_hunt_checklist,
    get_winning_square_ids,
    toggle_hunt_item,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameState, HuntItem


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    game_state: GameState = GameState.START
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False
    hunt_items: list[HuntItem] = field(default_factory=list)
    current_card: str = ""

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def has_bingo(self) -> bool:
        return self.game_state == GameState.BINGO

    @property
    def hunt_progress_percentage(self) -> int:
        return int(calculate_hunt_progress(self.hunt_items))

    def start_game(self) -> None:
        self.board = generate_board()
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.show_bingo_modal = False

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return
        self.board = toggle_square(self.board, square_id)

        if self.winning_line is None:
            bingo = check_bingo(self.board)
            if bingo is not None:
                self.winning_line = bingo
                self.game_state = GameState.BINGO
                self.show_bingo_modal = True

    def start_hunt(self) -> None:
        self.hunt_items = generate_hunt_checklist()
        self.game_state = GameState.HUNT

    def handle_hunt_click(self, item_id: int) -> None:
        if self.game_state == GameState.HUNT:
            self.hunt_items = toggle_hunt_item(self.hunt_items, item_id)

    def start_card(self) -> None:
        self.current_card = draw_random_card()
        self.game_state = GameState.CARD

    def shuffle_card(self) -> None:
        if self.game_state == GameState.CARD:
            self.current_card = draw_random_card()

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.board = []
        self.winning_line = None
        self.show_bingo_modal = False
        self.hunt_items = []
        self.current_card = ""

    def dismiss_modal(self) -> None:
        self.show_bingo_modal = False
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
