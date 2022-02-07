from dataclasses import dataclass, field
import json
from os import write
from os.path import exists
import pytest
from _pytest.reports import TestReport
from spoiler_alert_keep_out.level_documentation import (
    display_boss_email,
    display_poker_rules,
)

debug = False

MIN_LEVEL = 'min_level'
MAX_LEVEL = 'max_level'
INTEGRATION = 'integration'
ALL_LEVEL_MARKS = (MIN_LEVEL, MAX_LEVEL)

LEVEL_STATE_PATH = 'spoiler_alert_keep_out/level_state.json'

level_state = {}

@dataclass
class IntegrationStatus:
    """
    Stores integration test status, and level ranges (if applicable)
    """
    is_integration: bool = False
    min_level: int = None
    max_level: int = None

    def __bool__(self):
        """
        Truthyness determined by current is_integration bool
        """
        return self.is_integration


def pytest_addoption(parser):
    parser.addoption(
        "--level",
        action="store",
        metavar="LEVEL_INT",
        help="Override level, e.g. to view older emails",
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
    Register "integration" marker that takes optional level range arguments
    """
    config.addinivalue_line(
        "markers", "integration(min_level, max_level): Only run with --submit, if not outside level range"
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


def get_integration_status(item):
    """
    Return IntegrationStatus object, first checking args, then kwargs.
    (Both min_level and max_level default to None if undefined)
    """
    integration_marks = [
        mark for mark in item.iter_markers()
        if mark.name == INTEGRATION
    ]
    if not integration_marks:
        return IntegrationStatus(is_integration=False)

    mark = integration_marks[0]
    levels = dict()
    if mark.args:
        levels[MIN_LEVEL] = mark.args[0]
        levels[MAX_LEVEL] = mark.args[1] if len(mark.args > 1) else None
    else:
        levels[MIN_LEVEL] = mark.kwargs.get(MIN_LEVEL)
        levels[MAX_LEVEL] = mark.kwargs.get(MAX_LEVEL)

    return IntegrationStatus(is_integration=True, **levels)


def pytest_runtest_setup(item):
    """
    In Submit mode, skip tests whose level min/max excludes the current level
    """
    submitted = item.config.getoption("--submit")

    level = 0
    # Get the --level option, convert to Integer (or None)
    if submitted:
        level = load_level_state().get("current_level", 0)
        try:
            level = int(level)
        except ValueError:
            pytest.exit(f"Invalid current_level config option: {level}")

    integration = get_integration_status(item)

    if integration and not submitted:
        pytest.skip("(Not Running any Integration Tests)")
    if integration and submitted:
        if integration.min_level is not None and level < integration.min_level:
            pytest.skip("Not Until Level {}".format(integration.min_level))
        if integration.max_level is not None and level > integration.max_level:
            pytest.skip("Not After Level {}".format(integration.max_level))


def pytest_sessionfinish(session, exitstatus):
    """
    Handle level advancement, if all Tests pass in --submit mode
    """
    status_int = int(exitstatus)
    submitted = session.config.getoption("--submit")
    level_state = load_level_state()
    if debug:
        print("\n")
        print(f"status_int: {status_int}")
        print(f"submit active: {submitted}")
    if submitted and status_int == 0:
        level_state['current_level'] += 1
        write_level_state(level_state)
        print(f"\n\n* * * All Tests Passed: Advancing to level {level_state['current_level']}! * * *")
    elif submitted:
        print(f"\n\n(Some Tests Failed - Remaining on level {level_state['current_level']})")


def load_level_state():
    """
    Load current (level) config in from file, defaulting to starting state
    """
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
    """
    Write current (level) config out to file
    """
    with open(LEVEL_STATE_PATH, 'w') as f:
        try:
            if debug:
                print(f"writing level_state: {level_state}")
            f.write(json.dumps(level_state))
            f.flush()
        except Exception as e:
            print("FAILED TO WRITE CONFIG!")
            print(e)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Post-Test reporting behaviors

    * Stop PyTest after any one Integration test fails

    * Render Integration test failures in "single line" traceback mode
    """
    test_run = yield
    integration = get_integration_status(item)

    # Do not alter the post-test behavior of non-integration (userspace) tests
    if not integration:
        return

    result = test_run.get_result()
    if result.outcome == 'failed':
        # Stop PyTest after the first failed Integration test
        item.session.shouldfail = "(Integration Test Failed)"

        # Honor --full-trace and --tb by not altering the traceback!
        full_trace = item.config.getoption('--full-trace')
        tb = item.config.getoption('--tb')
        if full_trace or tb != 'auto':
            return

        # Re-render the result repr as a single-line traceback string
        one_liner = item._repr_failure_py(
            call.excinfo,
            style="no"
        )
        one_liner_str = str(one_liner)
        # On AssertionError, or pytest.fail(), use the single-line traceback!
        if "AssertionError" in one_liner_str or "Failed:" in one_liner_str:
            result.longrepr = one_liner

    return result
