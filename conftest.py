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
    parser.addoption(
        "--level",
        action="store",
        metavar="LEVEL_INT",
        help="Override level, to view older emails",
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

    if debug:
        print(">>> pytest_configure level_state:", level_state)
        print(">>> pytest_configure --level:", level_str)

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

    if debug:
        print(">>> pytest_configure level:", level)

    show_email = config.getoption("--email")
    if show_email:
        display_boss_email(level)
        pytest.exit(f"(after reading email #{level+1})")

    show_rules = config.getoption("--rules")
    if show_rules:
        display_poker_rules(level)
        pytest.exit(f"(after displaying v{(level or 0)+1} Poker rules)")


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

    level = 0
    # Get the --level option, convert to Integer (or None)
    if submit:
        level = load_level_state().get("current_level", 0)
        try:
            level = int(level)
        except ValueError:
            pytest.exit(f"Invalid current_level config option: {level}")

    min_level, max_level = get_level_marks(item)

    if not submit and min_level is not None or max_level is not None:
        pytest.skip("(Not Running any Integration Tests)")
    if min_level and min_level > level:
        pytest.skip("Not Until L{}".format(min_level))
    if max_level and level > max_level:
        pytest.skip("Not After L{}".format(max_level))


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
        print(f"* * * All Tests Passed: Advancing to level {level_state['current_level']}! * * *")
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
            if debug:
                print(f"writing level_state: {level_state}")
            f.write(json.dumps(level_state))
            f.flush()
        except Exception as e:
            print("FAILED TO WRITE CONFIG!")
            print(e)
