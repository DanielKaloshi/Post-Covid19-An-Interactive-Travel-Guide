"""CSC111 Winter 2023 Course Project: Post COVID-19: An Interactive Travel Guide
This module runs and outputs our interactive user module.

Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of the CSC111 instructors and
TAs at the University of Toronto St. George campus. All forms of distribution of this code,
whether as given or with any changes, are strictly prohibited. For more information on
copyright for CSC111 project materials, please consult our Course Syllabus.

This file is Copyright (c) 2023 Alex Nguyen, Anson Lau, Daniel Kaloshi, Dua Hussain
"""


def runner() -> None:
    """ Runner to run file user_interactions.py"""
    with open("user_interactions.py") as f:
        exec(f.read())
