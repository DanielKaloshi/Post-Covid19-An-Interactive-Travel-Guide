""" A runner file to run user_interaction.py to output our Interactive User Module.
 This file was not able to call user_interation in a single runner function since user_interatcion uses the
 library tkinter which layers each function """

from user_interactions import *
# INSTRUCTIONS FOR TA

# -------TO RUN FILE-------
# 1. PLEASE GO INTO USER_INTERACTIONS.PY RUN AND RUN IN CONSOLE. IT SHOULD AUTOMATICALLY OUTPUT THE INTERACTIVE MODULE
# 2. ENTER NAME, ORIGIN COUNTRY AND DESTINATION COUNTRY (VISIT LIMITATIONS)
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
# 1. ENTER SOURCE: VANATU
# 2. ENTER DEST: BELIZE


def runner():
    """Runner to run the entire module.
    """
    check_inputs()
