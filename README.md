# Incremental Poker Scoring Kata

A TDD-(and somewhat BDD)-based exercise, simulating life at an Online Poker startup where things move fast and break often.

## InstaPoker

Your team has been tasked with the implementation of code to score Poker Hands - You will be handling the Poker-hand-scoring logic only, so don't worry about HTTP Requests! There's another team for that, and they _probably_ know what they're doing.

Proceed through a series of levels, introduced by an email from your mysterious boss, implementing new features, and attempting to pass the integration tests for each new challenge. The job posting said you didn't need any prior experience with Poker, but it's starting to sound like your Boss is also learning along the way...

### Setup:

This exercise requires Python 3 and PyTest. (I also recommend the other development tools in requirements.txt, if you're using VSCode as your IDE). I have also provided a `Pipfile` if you'd like to create and manage an environment using `pipenv`. This project includes a few custom PyTest plugins to automate the experience, via special commands described below. 

### How to "Play":

Please don't look in the `spoiler_alert_keep_out` folder, or modify any of the files there!

Please proceed one level at a time, making sure that all (non-skipped) tests pass before proceeding to the next level.

While performing this kata, you will be editing the `poker_scoring_api.py` file, incrementally improving the `score_poker_hand` function: You are also encouraged to practice TDD, and add your own unit tests to `test_poker_scoring.py` as you go. Feel free to create more functions, as well as additional python modules or test files to organize your code, if you'd like.

To run your current suite of tests, you can just invoke pytest with no arguments:
```
pytest
```

To get more information about what your boss wants you to do next, run pytest with the special `--email` option:
```
pytest --email
```
This displays the current email, in which your Boss will describe the next feature(s) to be implemented.

To review the accumulated Poker rules and policies, run pytest with the special `--rules` option:
```
pytest --rules
```

Once you've gotten the initial test (and your own unit tests, if any) passing, and believe that you've implemented the requested spec, you can "submit" your work for approval by running pytest with the special `--submit` option:
```
pytest --submit
```

This will run your tests, as well as Integration tests from other stakeholders at your virtual company - If any of them fail, you should improve your implementation before trying again. If all the tests pass, you will advance to the next "level". This will prompt a new email from the Boss, which you can check with the `--email` command:

```
pytest --email
```

And so on, progressing through levels and emails until you're "done", or at least, until your Boss decides to call it a night.

### Hints:

* Don't forget to check your email each time you advance!

* You can view past emails by running pytest by adding the level option: `--level 0` is the intro, `--level 1` is after the first `submit`, etc...

* You can review the currently specified rule with `--rules`

* Beware of premature optimization: The CTOs of startups are notoriously fickle...

Can you survive your first day at *InstaPoker?*

![World's Best Boss](/worlds-best-boss.jpg)
