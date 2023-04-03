""" A runner file to run user_interaction.py which runs the entire project module.
To run please run function runner()"""

from user_interactions import *
# INSTRUCTIONS FOR TA

# -------TO RUN FILE-------
# 1. PLEASE RUN runner() IN CONSOLE
# 2. ENTER NAME, SOURCE COUNTRY AND DESTINATION COUNTRY (VISIT LIMITATIONS)
# 3. TO VIEW MAP, PRESS LINK ABOVE

# NOTE: THERE ARE THREE OUTPUT PAGES, DIRECT FLIGHT, LAYOVER FLIGHT, NO FLIGHT FOUND
#       WE HAVE PROVIDED SAMPLE INPUTS FOR EACH PAGE
#       TO VIEW EACH PAGE FOLLOW INSTRUCTIONS BELOW
#
# ------TO VIEW DIRECT FLIGHT PAGE-----
# 1. ENTER SOURCE COUNTRY: CANADA
# 2. ENTER DESTINATION COUNTRY: FRANCE
#
# ------TO VIEW LAYOVER PAGE-----
# 1. ENTER SOURCE COUNTRY: CANADA
# 2. ENTER DESTINATION COUNTRY: INDIA

# ------TO VIEW NO DIRECT FLIGHT-----
# 1. ENTER SOURCE: VANUATU
# 2. ENTER DEST: BELIZE

# Links to obtain data file:
# https://utoronto-my.sharepoint.com/personal/ansonbt_lau_mail_utoronto_ca/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fansonbt%5Flau%5Fmail%5Futoronto%5Fca%2FDocuments%2Fdata%2Ezip&parent=%2Fpersonal%2Fansonbt%5Flau%5Fmail%5Futoronto%5Fca%2FDocuments&ga=1


def runner():
    """Runner to run the entire module.
    """
    check_inputs()
