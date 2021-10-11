import pytest
from spoiler_alert_keep_out.level_documentation import (
    display_boss_email,
    display_poker_rules,
    display_test_level_info,
)

MARK_LEVEL = 'level'
MARK_MAX_LEVEL = 'max_level'
ALL_LEVEL_MARKS = (MARK_LEVEL, MARK_MAX_LEVEL)


def pytest_addoption(parser):
    """
    --level (highest "level" of test to run, defaulting to 0)
    --email (display level notes in "boss email" form)
    --rules (list Poker Rules as of the current level)
    """
    parser.addoption(
        "--level",
        action="store",
        metavar="NAME",
        default=0,
        help="run integration tests of integer [level] or lower",
    )
    parser.addoption(
        "--email",
        action="store_true",
        help="display the Boss Email for the selected level",
    )
    parser.addoption(
        "--rules",
        action="store_true",
        help="list Poker Rules as of the current level",
    )


def pytest_configure(config):
    """
    Register an additional "level" marker that takes a single integer argument
    """
    config.addinivalue_line(
        "markers", "level(level_int): Run only at a certain testing level or higher"
    )

    config.addinivalue_line(
        "markers", "max_level(max_level_int): Maximum level cap to run a level-ed test"
    )

    level_str = config.getoption("--level")
    level = 0
    if level_str is not None:
        try:
            level = int(level_str)
        except (ValueError, TypeError):
            pass

    show_email = config.getoption("--email")
    if show_email:
        display_boss_email(level)
        pytest.exit("(after reading email #{})".format(level+1))

    show_email = config.getoption("--rules")
    if show_email:
        display_poker_rules(level)
        level_info = ""
        if level:
            level_info = " for level {}".format(level)
        pytest.exit("(after displaying Poker rules{})".format(level_info))

    display_test_level_info(level)


def get_level_marks(item):
    level_marks = {
        mark.name: mark.args[0] for mark in item.iter_markers()
        if mark.name in ALL_LEVEL_MARKS
    }
    return level_marks.get(MARK_LEVEL), level_marks.get(MARK_MAX_LEVEL)


def pytest_runtest_setup(item):
    """
    Skip any tests whose "level" mark is above our current --level setting
    (or whose max_level is less than our current --level setting)
    """
    # Get the --level option, convert to Integer (or None)
    level_str = item.config.getoption("--level")
    level_option = None
    if level_str is not None:
        try:
            level_option = int(level_str)
        except ValueError:
            pytest.exit(f"Invalid --level value: {level_str}")

    if level_option is not None:
        level, max_level = get_level_marks(item)
        if level and level > level_option:
            pytest.skip("Until L{}".format(level))
        if max_level and level_option > max_level:
            pytest.skip("After L{}".format(max_level))
