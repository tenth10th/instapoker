from datetime import datetime, timedelta
import random
from spoiler_alert_keep_out.boss_emails import boss_emails
from spoiler_alert_keep_out.poker_rules import poker_rules


def procedural_datetime(level):
    random.seed(45)
    email_time = datetime(2021, 10, 11, 9, 45)
    for i in range(level):
        proc_minutes = random.randrange(45, 65)
        email_time += timedelta(minutes=proc_minutes)
    return email_time.strftime("%b %d, %Y, %I:%M %p")


def display_boss_email(level):
    subject = "Poker" if level == 0 else "re: Poker"
    datetime_str = procedural_datetime(level)
    if level < len(boss_emails):
        print()
        print("from:    the-bawss@instapoker.com")
        print("date:    {}".format(datetime_str))
        print("subject: {}".format(subject))
        print(boss_emails[level])
    else:
        print("(No Boss Email available for Level {})".format(level))


def display_test_level_info(level, submit):
    if not submit:
        print("(Running your local tests only)")
    if level == 0:
        print("(Test Level 0: Not running incremental tests)")
    elif level == 1:
        print("(Running Incremental Tests for level 1)")
    elif level > 1:
        print("(Running Incremental Tests for levels 1 - {})".format(level))


def display_poker_rules(level):
    display_rules = list()
    for r in poker_rules:
        rule_level = r.get('level')
        rule_level_range = r.get('level_range')

        if rule_level and rule_level > level:
            continue

        if rule_level_range:
            rule_min, rule_max = rule_level_range
            if rule_min > level or rule_max < level:
                continue

        display_rules.append(r)

    display_rules.sort(key=lambda x: x.get('sort_order'), reverse=True)

    print()
    for r in display_rules:
        print(r.get('text', '').strip())
        print()
