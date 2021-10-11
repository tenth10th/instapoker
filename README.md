# Incremental Poker Scoring Kata

A TDD-(and somewhat BDD)-based exercise, simulating life at an Online Poker startup where things move fast and break often:

## InstaPoker

Your team has been tasked with the implementation of code to score Poker Hands - You will be handling the Poker-hand-scoring logic only, so don't worry about HTTP Requests! There's another team for that, and they _probably_ know what they're doing.

Proceed through a series of levels, introduced by an email from your mysterious boss, attempting to pass the integration tests for each new challenge.

### Setup:

This exercise requires Python 3 and PyTest. (I also recommend the other development tools in requirements.txt, if you're using VSCode as your IDE). I have also provided a `Pipfile` if you'd like to create and manage an environment using `pipenv`.

### How to "Play":

Please don't look in the `spoiler_alert_keep_out` folder, or modify any of the files there!

Please proceed one level at a time, making sure that all (non-skipped) tests pass before proceeding to the next level.

While performing this kata, you will be editing the `poker_scoring_api.py` file, incrementally improving the `score_poker_hand` function: You are also encouraged to practice TDD, and add your own unit tests to `test_poker_scoring.py` as you go.

To run the current suite of tests, simply run:

```
pytest
```

You will find that your Boss has added some integration tests related to the changes they want you to make: To get more information, run pytest with the special `--email` option:

```
pytest --email
```

To see the current email, which will include more information about the work your Boss wants done.

Once you've gotten the initial test(s) passing, you can progress to the next level, by using the special `--level` option: You will default to level 0, which only tests basic API behavior.

This will activate new tests, and also a new email from the Boss, which you can check by adding the `--email` option as well:

```
pytest --level 1 --email
```

Once you've done the work, and written your own tests (running `pytest` alone will target
your unit tests), you can run the level 1 integration tests:

```
pytest --level 1
```

Once you've made all the tests pass in level 1 (and you've done any refactoring you think is necessary), you can proceed to level 2!

You should probably begin a new level by reading the email:

```
pytest --level 2 --email
```

Then, when you think you're ready, run the tests:

```
pytest --level 2
```

(If you'd prefer, you can also edit `pytest.ini` to change the default/current level, so you don't have to keep adding the `--level` option. But you can still use `--level 0` to run your Unit Tests and the basic API integration test only.

Can you survive your first day at *InstaPoker?*

![World's Best Boss](/worlds-best-boss.jpg)
