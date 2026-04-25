from app.data import FREE_SPACE, QUESTIONS
from app.game_logic import (
    CENTER_INDEX,
    calculate_hunt_progress,
    check_bingo,
    generate_board,
    generate_hunt_checklist,
    get_winning_square_ids,
    toggle_hunt_item,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData


class TestGenerateBoard:
    def test_board_has_25_squares(self):
        board = generate_board()
        assert len(board) == 25

    def test_center_is_free_space(self):
        board = generate_board()
        center = board[CENTER_INDEX]
        assert center.is_free_space is True
        assert center.is_marked is True
        assert center.text == FREE_SPACE

    def test_non_center_squares_are_not_free_space(self):
        board = generate_board()
        for i, square in enumerate(board):
            if i != CENTER_INDEX:
                assert square.is_free_space is False
                assert square.is_marked is False

    def test_all_questions_from_pool(self):
        board = generate_board()
        texts = {s.text for s in board if not s.is_free_space}
        assert texts.issubset(set(QUESTIONS))

    def test_squares_have_sequential_ids(self):
        board = generate_board()
        for i, square in enumerate(board):
            assert square.id == i

    def test_board_is_shuffled(self):
        """Verify two boards aren't identical (high probability)."""
        board1 = generate_board()
        board2 = generate_board()
        texts1 = [s.text for s in board1]
        texts2 = [s.text for s in board2]
        # Extremely unlikely to be identical
        assert texts1 != texts2


class TestHuntLogic:
    def test_generate_hunt_checklist_has_24_items(self):
        from app.game_logic import generate_hunt_checklist

        checklist = generate_hunt_checklist()
        assert len(checklist) == 24

    def test_hunt_checklist_items_have_sequential_ids(self):
        from app.game_logic import generate_hunt_checklist

        checklist = generate_hunt_checklist()
        for i, item in enumerate(checklist):
            assert item.id == i

    def test_hunt_checklist_uses_all_questions(self):
        from app.game_logic import generate_hunt_checklist

        checklist = generate_hunt_checklist()
        texts = {item.text for item in checklist}
        assert texts == set(QUESTIONS)

    def test_hunt_checklist_is_shuffled(self):
        from app.game_logic import generate_hunt_checklist

        checklist1 = generate_hunt_checklist()
        checklist2 = generate_hunt_checklist()
        texts1 = [item.text for item in checklist1]
        texts2 = [item.text for item in checklist2]
        assert texts1 != texts2

    def test_toggle_hunt_item_flips_checked_state(self):
        from app.game_logic import generate_hunt_checklist

        checklist = generate_hunt_checklist()
        original_state = checklist[0].is_checked
        updated = toggle_hunt_item(checklist, 0)
        assert updated[0].is_checked != original_state
        # Other items unchanged
        for i in range(1, 24):
            assert updated[i].is_checked == checklist[i].is_checked

    def test_toggle_hunt_item_returns_new_list(self):
        from app.game_logic import generate_hunt_checklist

        checklist = generate_hunt_checklist()
        updated = toggle_hunt_item(checklist, 0)
        assert updated is not checklist  # New list
        assert len(updated) == len(checklist)

    def test_calculate_hunt_progress_zero_when_none_checked(self):
        checklist = generate_hunt_checklist()
        progress = calculate_hunt_progress(checklist)
        assert progress == 0.0

    def test_calculate_hunt_progress_full_when_all_checked(self):
        checklist = generate_hunt_checklist()
        # Check all items
        for i in range(24):
            checklist = toggle_hunt_item(checklist, i)
        progress = calculate_hunt_progress(checklist)
        assert progress == 100.0

    def test_calculate_hunt_progress_partial(self):
        checklist = generate_hunt_checklist()
        # Check 12 items (half)
        for i in range(12):
            checklist = toggle_hunt_item(checklist, i)
        progress = calculate_hunt_progress(checklist)
        assert progress == 50.0

    def test_calculate_hunt_progress_empty_list(self):
        progress = calculate_hunt_progress([])
        assert progress == 0.0


class TestCardLogic:
    def test_draw_random_card_returns_question(self):
        from app.game_logic import draw_random_card

        card = draw_random_card()
        assert card in QUESTIONS

    def test_draw_random_card_is_random(self):
        from app.game_logic import draw_random_card

        # Not always different, but test multiple times
        cards = {draw_random_card() for _ in range(10)}
        assert len(cards) > 1  # Should get variety


class TestToggleSquare:
    def test_toggle_marks_unmarked_square(self):
        board = generate_board()
        square_id = 0
        assert board[square_id].is_marked is False
        new_board = toggle_square(board, square_id)
        assert new_board[square_id].is_marked is True

    def test_toggle_unmarks_marked_square(self):
        board = generate_board()
        board = toggle_square(board, 0)
        assert board[0].is_marked is True
        board = toggle_square(board, 0)
        assert board[0].is_marked is False

    def test_toggle_does_not_affect_free_space(self):
        board = generate_board()
        new_board = toggle_square(board, CENTER_INDEX)
        assert new_board[CENTER_INDEX].is_marked is True  # Still marked

    def test_toggle_returns_new_list(self):
        board = generate_board()
        new_board = toggle_square(board, 0)
        assert board is not new_board


class TestCheckBingo:
    def _make_board(self, marked_ids: set[int]) -> list[BingoSquareData]:
        board = generate_board()
        result = []
        for square in board:
            if square.id in marked_ids or square.is_free_space:
                result.append(
                    BingoSquareData(
                        id=square.id,
                        text=square.text,
                        is_marked=True,
                        is_free_space=square.is_free_space,
                    )
                )
            else:
                result.append(square)
        return result

    def test_no_bingo_initially(self):
        board = generate_board()
        assert check_bingo(board) is None

    def test_row_bingo(self):
        # Mark first row: indices 0-4
        board = self._make_board({0, 1, 2, 3, 4})
        result = check_bingo(board)
        assert result is not None
        assert result.type == "row"
        assert result.squares == [0, 1, 2, 3, 4]

    def test_column_bingo(self):
        # Mark first column: indices 0, 5, 10, 15, 20
        board = self._make_board({0, 5, 10, 15, 20})
        result = check_bingo(board)
        assert result is not None
        assert result.type == "column"
        assert result.squares == [0, 5, 10, 15, 20]

    def test_diagonal_bingo(self):
        # Mark diagonal: 0, 6, 12, 18, 24 (12 is free space)
        board = self._make_board({0, 6, 18, 24})
        result = check_bingo(board)
        assert result is not None
        assert result.type == "diagonal"
        assert result.squares == [0, 6, 12, 18, 24]

    def test_partial_line_no_bingo(self):
        board = self._make_board({0, 1, 2, 3})  # Only 4 of 5 in first row
        assert check_bingo(board) is None


class TestGetWinningSquareIds:
    def test_none_line_returns_empty_set(self):
        assert get_winning_square_ids(None) == set()

    def test_returns_square_ids(self):
        line = BingoLine(type="row", index=0, squares=[0, 1, 2, 3, 4])
        assert get_winning_square_ids(line) == {0, 1, 2, 3, 4}
