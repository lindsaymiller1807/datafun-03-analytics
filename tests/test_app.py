"""tests/test_app.py - Smoke test for the project.

WHY: Professional Python projects include tests to verify that code runs
     correctly and to catch problems early when changes are made.
     Running tests is part of the standard workflow in every module.

OBS: You do not need to read or modify this file.
"""


def test_app_runs() -> None:
    """Confirm the project module runs without error."""
    from datafun.app import main

    main()
