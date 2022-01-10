import json
from os import write
from os.path import exists
import pytest
from spoiler_alert_keep_out.level_documentation import (
    display_boss_email,
    display_poker_rules,
    display_test_level_info,
)

debug = False

MARK_LEVEL = 'level'
MARK_MAX_LEVEL = 'max_level'
ALL_LEVEL_MARKS = (MARK_LEVEL, MARK_MAX_LEVEL)

LEVEL_STATE_PATH = 'spoiler_alert_keep_out/level_state.json'

level_state = {}


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
    parser.addoption(
        "--submit",
        action="store_true",
        help="Advance to the next level (if tests pass)",
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

    level = 0
    level_state = load_level_state()

    level_str = config.getoption("--level")
    if level_str is not None:
        try:
            level = int(level_str)
        except (ValueError, TypeError):
            print("Ignoring invalid --level: {level_str}")
            pass
    else:
        try:
            level = int(level_state['current_level'])
        except (ValueError, TypeError):
            print(f"Ignoring invalid current_level state: {level_state['current_level']}")
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
    submit = item.config.getoption("--submit")

    # Get the --level option, convert to Integer (or None)
    if submit:
        level_str = load_level_state().get("current_level", "0")
    else:
        level_str = "0"

    level_option = None
    if level_str is not None:
        try:
            level_option = int(level_str)
        except ValueError:
            pytest.exit(f"Invalid current_level config option: {level_str}")

    if level_option is not None:
        level, max_level = get_level_marks(item)
        if not submit and level is not None or max_level is not None:
            pytest.skip("(Not Running Integration Tests)")
        if level and level > level_option:
            pytest.skip("Until L{}".format(level))
        if max_level and level_option > max_level:
            pytest.skip("After L{}".format(max_level))


def pytest_sessionfinish(session, exitstatus):
    print("\n")
    status_int = int(exitstatus)
    submit = session.config.getoption("--submit")
    level_state = load_level_state()
    if debug:
        print(f"status_int: {status_int}")
        print(f"submit active: {submit}")
    if submit and status_int == 0:
        level_state['current_level'] += 1
        write_level_state(level_state)
        print(f"All Tests Passed: Advancing to level {level_state['current_level']}!")
    elif submit:
        print(f"(Some Tests Failed - Remaining on level {level_state['current_level']})")


def load_level_state():
    if not exists(LEVEL_STATE_PATH):
        return {"current_level": 0}
    with open(LEVEL_STATE_PATH, 'r') as f:
        try:
            level_state = json.loads(f.read())
            if debug:
                print(f"reading level_state: {level_state}")
            return level_state
        except Exception as e:
            print("FAILED TO LOAD CONFIG!")
            print(e)


def write_level_state(level_state):
    with open(LEVEL_STATE_PATH, 'w') as f:
        try:
            print(f"writing level_state: {level_state}")
            f.write(json.dumps(level_state))
            f.flush()
        except Exception as e:
            print("FAILED TO WRITE CONFIG!")
            print(e)
