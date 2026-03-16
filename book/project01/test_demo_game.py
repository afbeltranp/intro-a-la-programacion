"""
test_demo_game.py
=================
Automated test runner for Bulls and Cows student submissions.
Runs the student's script as a subprocess and feeds it inputs,
then checks the output against expected patterns.

Usage:
    python test_demo_game.py demo_game.py
    python test_demo_game.py scrip.py
"""

import subprocess
import sys
import os
import re
from typing import List, Tuple

# ── Seed reference table (Python random) ────────────────────────────────────
# seed 42  -> 1043
# seed 7   -> 5260
# seed 100 -> 2765
# seed 999 -> 1987

# ── Colours (disabled on Windows if not supported) ───────────────────────────
def supports_color():
    return sys.platform != "win32" or "ANSICON" in os.environ or "WT_SESSION" in os.environ

GREEN  = "\033[92m" if supports_color() else ""
RED    = "\033[91m" if supports_color() else ""
YELLOW = "\033[93m" if supports_color() else ""
CYAN   = "\033[96m" if supports_color() else ""
RESET  = "\033[0m"  if supports_color() else ""
BOLD   = "\033[1m"  if supports_color() else ""

# ── Test infrastructure ──────────────────────────────────────────────────────
results = []

def run_game(script: str, inputs: List[str], timeout: int = 10) -> Tuple[str, bool]:
    """Run the student script with the given inputs and return (output, timed_out)."""
    inp = "\n".join(inputs) + "\n"
    try:
        proc = subprocess.run(
            [sys.executable, script],
            input=inp,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return proc.stdout + proc.stderr, False
    except subprocess.TimeoutExpired:
        return "", True

def check(name: str, output: str, timed_out: bool,
          must_contain: List[str] = None,
          must_not_contain: List[str] = None,
          notes: str = ""):
    """Evaluate a single test case and record the result."""
    passed = True
    failures = []

    if timed_out:
        passed = False
        failures.append("Script timed out (possible infinite loop or missing input handling)")
    else:
        for phrase in (must_contain or []):
            if phrase.lower() not in output.lower():
                passed = False
                failures.append(f'Expected to find: "{phrase}"')
        for phrase in (must_not_contain or []):
            if phrase.lower() in output.lower():
                passed = False
                failures.append(f'Should NOT contain: "{phrase}"')

    results.append((name, passed, failures, output, notes))
    status = f"{GREEN}PASS{RESET}" if passed else f"{RED}FAIL{RESET}"
    print(f"  {status}  {name}")
    if not passed:
        for f in failures:
            print(f"        {YELLOW}↳ {f}{RESET}")
    if notes and not passed:
        print(f"        {CYAN}ℹ {notes}{RESET}")

# ── Test cases ───────────────────────────────────────────────────────────────

def test_welcome(script):
    out, to = run_game(script, ["1", "42", "3", "give up", "n"])
    check(
        "Welcome message",
        out, to,
        must_contain=["Welcome to Bulls and Cows"],
        notes="The function welcome_message() should print this exact text."
    )

def test_seed_generates_correct_code(script):
    # seed 42 -> code 1043; guess it correctly to confirm the code was right
    out, to = run_game(script, ["1", "42", "3", "1043", "n"])
    check(
        "Seed 42 generates code 1043",
        out, to,
        must_contain=["you win"],
        notes="random.seed(42) should produce 1043. If the guess '1043' wins, the seed is correct."
    )

def test_seed_7(script):
    # seed 7 -> code 5260; guess it correctly to confirm
    out, to = run_game(script, ["1", "7", "3", "5260", "n"])
    check(
        "Seed 7 generates code 5260",
        out, to,
        must_contain=["you win"],
        notes="random.seed(7) should produce 5260. If the guess '5260' wins, the seed is correct."
    )

def test_win_condition(script):
    # Manual code 1234, easy difficulty, guess correctly first try
    out, to = run_game(script, ["2", "1234", "1", "1234", "n"])
    check(
        "Win condition",
        out, to,
        must_contain=["you win"],
        notes="When the correct code is guessed, 'You win!' should be printed."
    )

def test_win_shows_no_loss_message(script):
    out, to = run_game(script, ["2", "1234", "1", "1234", "n"])
    check(
        "Win does not show lose message",
        out, to,
        must_not_contain=["you lose"],
        notes="After winning, the lose message should not appear."
    )

def test_lose_condition(script):
    # Hard mode (5 guesses), manual code 1234
    # Make 5 wrong guesses then check for lose message
    wrong_guesses = ["5678", "5679", "5670", "5671", "5672"]
    inputs = ["2", "1234", "3"] + wrong_guesses + ["n"]
    out, to = run_game(script, inputs)
    check(
        "Lose condition (run out of guesses)",
        out, to,
        must_contain=["you lose"],
        notes="After all guesses are used, 'You lose' should be printed."
    )

def test_lose_reveals_code(script):
    wrong_guesses = ["5678", "5679", "5670", "5671", "5672"]
    inputs = ["2", "1234", "3"] + wrong_guesses + ["n"]
    out, to = run_game(script, inputs)
    check(
        "Lose reveals the correct code",
        out, to,
        must_contain=["1234"],
        notes="After losing, the correct answer should be shown."
    )

def test_bulls_and_cows_output(script):
    # Code: 1234, guess: 1567 -> 1 bull (1 in position 0), 1 cow (2... wait)
    # Code: 1234, guess: 1357 -> Bulls:1 (1@pos0), Cows:1 (3@pos2->pos1 no... 3 in code at pos2, guess pos1)
    # Let's use: code=1234, guess=1256 -> Bulls:2 (1,2), Cows:0
    inputs = ["2", "1234", "1", "1256", "1234", "n"]
    out, to = run_game(script, inputs)
    check(
        "Bulls and Cows count displayed",
        out, to,
        must_contain=["Bulls:", "Cows:"],
        notes="After each wrong guess, Bulls: and Cows: counts must be printed."
    )

def test_bulls_correct_count(script):
    # code=1234, guess=1256 -> 2 bulls (1 and 2 in correct positions)
    inputs = ["2", "1234", "1", "1256", "1234", "n"]
    out, to = run_game(script, inputs)
    check(
        "Bulls count is correct (expect 2)",
        out, to,
        must_contain=["Bulls: 2"],
        notes="For code=1234, guess=1256: digits 1 and 2 are in the right position → 2 bulls."
    )

def test_guesses_remaining(script):
    inputs = ["2", "1234", "2", "5678", "1234", "n"]  # medium = 8 guesses
    out, to = run_game(script, inputs)
    check(
        "Remaining guesses shown after wrong guess",
        out, to,
        must_contain=["7 guesses left"],
        notes="After 1 wrong guess in Medium mode (8 guesses), should show 7 guesses left."
    )

def test_give_up(script):
    inputs = ["2", "1234", "1", "give up", "n"]
    out, to = run_game(script, inputs)
    check(
        "Give up exits the game without crashing",
        out, to,
        must_not_contain=["traceback", "you win"],
        notes="Typing 'give up' should exit the current game cleanly without crashing."
    )

def test_invalid_input_letters(script):
    # Type letters instead of a code, then give valid input to continue
    inputs = ["2", "abcd", "1234", "1", "1234", "n"]
    out, to = run_game(script, inputs)
    check(
        "Invalid input: letters rejected",
        out, to,
        must_contain=["problem processing"],
        notes="Non-digit input should trigger the error message."
    )

def test_invalid_input_too_short(script):
    inputs = ["2", "12", "1234", "1", "1234", "n"]
    out, to = run_game(script, inputs)
    check(
        "Invalid input: too short (2 digits) rejected",
        out, to,
        must_contain=["problem processing"],
        notes="Codes shorter than 4 digits should be rejected."
    )

def test_invalid_input_duplicate_digits(script):
    inputs = ["2", "1123", "1234", "1", "1234", "n"]
    out, to = run_game(script, inputs)
    check(
        "Invalid input: duplicate digits rejected",
        out, to,
        must_contain=["problem processing"],
        notes="Codes with repeated digits (e.g. 1123) should be rejected."
    )

def test_invalid_guess_letters(script):
    inputs = ["2", "1234", "1", "abcd", "1234", "n"]
    out, to = run_game(script, inputs)
    check(
        "Invalid guess: letters rejected during play",
        out, to,
        must_contain=["problem processing"],
        notes="Letter input during guessing phase should trigger error message."
    )

def test_invalid_difficulty(script):
    inputs = ["2", "1234", "9", "1", "1234", "n"]
    out, to = run_game(script, inputs)
    check(
        "Invalid difficulty input rejected",
        out, to,
        must_contain=["problem processing"],
        notes="Difficulty input other than 1/2/3 should show an error."
    )

def test_play_again_yes(script):
    # Play once (give up), then play again and win
    inputs = ["2", "1234", "1", "give up", "y", "2", "5678", "1", "5678", "n"]
    out, to = run_game(script, inputs)
    check(
        "Play again: yes restarts the game",
        out, to,
        must_contain=["you win"],
        notes="After choosing 'y' to play again, a new game should start and be winnable."
    )

def test_play_again_no(script):
    inputs = ["2", "1234", "1", "give up", "n"]
    out, to = run_game(script, inputs, timeout=5)
    check(
        "Play again: no exits cleanly",
        out, to,
        must_not_contain=["traceback", "error"],
        notes="Choosing 'n' should exit without crashing."
    )

def test_easy_difficulty_12_guesses(script):
    wrong = ["5678"] * 11  # 11 wrong, then correct
    inputs = ["2", "1234", "1"] + wrong + ["1234", "n"]
    out, to = run_game(script, inputs, timeout=15)
    check(
        "Easy mode allows 12 guesses",
        out, to,
        must_contain=["you win"],
        must_not_contain=["you lose"],
        notes="Easy mode should allow 12 guesses. Winning on the 12th should still work."
    )

def test_hard_difficulty_5_guesses(script):
    wrong = ["5678"] * 5
    inputs = ["2", "1234", "3"] + wrong + ["n"]
    out, to = run_game(script, inputs)
    check(
        "Hard mode only allows 5 guesses",
        out, to,
        must_contain=["you lose"],
        notes="Hard mode should end after exactly 5 wrong guesses."
    )

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(f"{RED}Usage: python test_demo_game.py <student_script.py>{RESET}")
        sys.exit(1)

    script = sys.argv[1]

    if not os.path.exists(script):
        print(f"{RED}Error: File '{script}' not found.{RESET}")
        sys.exit(1)

    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}  Bulls and Cows — Automated Test Runner{RESET}")
    print(f"{BOLD}  Testing: {script}{RESET}")
    print(f"{BOLD}{'='*60}{RESET}\n")

    tests = [
        ("Welcome & Setup",      [test_welcome, test_seed_generates_correct_code, test_seed_7]),
        ("Win Condition",        [test_win_condition, test_win_shows_no_loss_message]),
        ("Lose Condition",       [test_lose_condition, test_lose_reveals_code]),
        ("Bulls & Cows Logic",   [test_bulls_and_cows_output, test_bulls_correct_count, test_guesses_remaining]),
        ("Give Up",              [test_give_up]),
        ("Invalid Inputs",       [test_invalid_input_letters, test_invalid_input_too_short,
                                  test_invalid_input_duplicate_digits, test_invalid_guess_letters,
                                  test_invalid_difficulty]),
        ("Play Again",           [test_play_again_yes, test_play_again_no]),
        ("Difficulty Levels",    [test_easy_difficulty_12_guesses, test_hard_difficulty_5_guesses]),
    ]

    for section, fns in tests:
        print(f"{BOLD}{CYAN}{section}{RESET}")
        for fn in fns:
            fn(script)
        print()

    # ── Summary ──────────────────────────────────────────────────────────────
    total  = len(results)
    passed = sum(1 for _, p, _, _, _ in results if p)
    failed = total - passed
    pct    = int(passed / total * 100)

    print(f"{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}  Results: {passed}/{total} passed  ({pct}%){RESET}")
    if failed:
        print(f"\n{RED}{BOLD}  Failed tests:{RESET}")
        for name, p, failures, _, notes in results:
            if not p:
                print(f"  {RED}✗ {name}{RESET}")
                for f in failures:
                    print(f"    • {f}")
                if notes:
                    print(f"    {CYAN}ℹ {notes}{RESET}")
    else:
        print(f"\n{GREEN}{BOLD}  All tests passed! 🎉{RESET}")
    print(f"{BOLD}{'='*60}{RESET}\n")

    sys.exit(0 if failed == 0 else 1)

if __name__ == "__main__":
    main()
