def eat_ghost(power_pellet_active, touching_ghost):
    """Return True if Pac-Man can eat a ghost: he must have an active power pellet and be touching a ghost."""
    return bool(power_pellet_active and touching_ghost)


def score(touching_power_pellet, touching_dot):
    """Return True if Pac-Man scored: touching a power pellet or touching a dot."""
    return bool(touching_power_pellet or touching_dot)


def lose(power_pellet_active, touching_ghost):
    """Return True if Pac-Man loses: touching a ghost without an active power pellet."""
    return bool(touching_ghost and not power_pellet_active)


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Return True if Pac-Man wins: all dots eaten and the player has not lost."""
    # Pac-Man wins only if all dots are eaten and he hasn't lost by touching a ghost without a pellet.
    return bool(has_eaten_all_dots and not lose(power_pellet_active, touching_ghost))


""" Summary

This module implements four small boolean rules from Pac‑Man: whether Pac‑Man can eat a ghost, whether he scored, whether he loses, and whether he wins. Each function returns a boolean based on its inputs. The bottom block includes quick example checks you can run locally.
Function-by-function description

eat_ghost(power_pellet_active, touching_ghost)
Purpose: Determine whether Pac‑Man can eat a ghost.
Parameters:
power_pellet_active: bool — True if Pac‑Man currently has an active power pellet.
touching_ghost: bool — True if Pac‑Man is touching a ghost.
Logic: Returns True only when both inputs are true (Pac‑Man is empowered and touching a ghost).
Return: bool
Example:
eat_ghost(True, True) -> True
eat_ghost(False, True) -> False
score(touching_power_pellet, touching_dot)
Purpose: Determine whether Pac‑Man scored by touching a pellet or a dot.
Parameters:
touching_power_pellet: bool
touching_dot: bool
Logic: Returns True if Pac‑Man is touching a power pellet OR touching a dot.
Return: bool
Example:
score(True, False) -> True
score(False, False) -> False
lose(power_pellet_active, touching_ghost)
Purpose: Determine whether Pac‑Man loses (GAME OVER).
Parameters:
power_pellet_active: bool
touching_ghost: bool
Logic: Pac‑Man loses only if he touches a ghost while he does NOT have an active power pellet. Implemented as touching_ghost and not power_pellet_active.
Return: bool
Example:
lose(False, True) -> True
lose(True, True) -> False
win(has_eaten_all_dots, power_pellet_active, touching_ghost)
Purpose: Determine whether Pac‑Man has won the game (all dots eaten and not lost).
Parameters:
has_eaten_all_dots: bool
power_pellet_active: bool
touching_ghost: bool
Logic: A win is true only when all dots are eaten AND Pac‑Man has not lost. The function reuses lose(...) and returns has_eaten_all_dots and not lose(...).
Return: bool
Example:
win(True, False, False) -> True
win(True, False, True) -> False (touched ghost without pellet → lose)
win(True, True, True) -> True (has pellet, touching ghost → can eat ghost, not lose)
How the pieces work together

The win function depends on the lose function to determine whether a “win” is valid — this keeps logic consistent and avoids duplicating the losing rule.
All functions return booleans and use short boolean expressions, making them concise and easy to read.
Example test block

The if __name__ == "__main__": block runs a few example calls when the file is executed directly. LeetCode or other automated graders ignore this block, so it’s safe to include for local testing.
Notes, edge cases & behavior

The functions accept any truthy/falsy values (not strictly bools). Using bool(...) ensures a boolean return even if callers pass e.g. 0, 1, or non-empty strings.
The code treats booleans in the usual Python way: truthy values (non-empty lists/strings, non-zero numbers) evaluate as True in if contexts.
The win function requires has_eaten_all_dots to be True; even if Pac‑Man cannot lose (e.g., not touching a ghost), he still must have eaten all dots to win.
Possible improvements (optional)

Add type hints for clarity: def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
Add unit tests (pytest) to cover more combinations and guard against regressions.
If you expect strictly boolean inputs, you can return expressions directly (without wrapping in bool()) — but keeping bool(...) is safe.  

"""
