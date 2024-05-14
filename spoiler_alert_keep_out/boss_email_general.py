"""
commonalities to all the boss' emails that hold for every level
"""
from datetime import datetime, timedelta
import random

class BossEmailTemplating:
    """
    the common parts to all the boss's emails
    """
    def __init__(self, main_subject : str,
                 boss_email: str,
                 first_email : datetime = datetime(2021, 10, 11, 9, 45)):
        self.main_subject = main_subject
        self.boss_email = boss_email
        self.first_email = first_email

    def __procedural_datetime(self,level: int):
        random.seed(45)
        email_time = self.first_email
        for _ in range(level):
            proc_minutes = random.randrange(45, 65)
            email_time += timedelta(minutes=proc_minutes)
        return email_time.strftime("%b %d, %Y, %I:%M %p")

    def display_email_headers(self,level: int) -> str:
        """
        before the body of the email
        """
        subject = self.main_subject if level == 0 else f"re: {self.main_subject}"
        datetime_str = self.__procedural_datetime(level)
        return "\n".join([
            f"from:    {self.boss_email}",
            f"date:    {datetime_str}",
            f"subject: {subject}"
        ])

    def print_email_headers(self,level : int) -> None:
        """
        print display_email_headers with appropriate newline spacing
        """
        print()
        header = self.display_email_headers(level)
        print(header)
