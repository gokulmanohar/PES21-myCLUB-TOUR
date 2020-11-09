# IMPORTS
from datetime import datetime
import os
from tour_2020_Q4 import tour_2020_Q4
from tour_2021_Q1 import tour_2021_Q1
from tour_2021_Q2 import tour_2021_Q2
from tour_2021_Q3 import tour_2021_Q3
from tour_2021_Q4 import tour_2021_Q4

# _GLOBAL VARIABLE
now = datetime.now()


# TO GET THE MONTH NAME FROM FILE NAME
def month_name_abbreviation(file_name):
    month_abbrev_dict = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December",
        }
    file_name = file_name
    file_name_char_list = []
    file_name_split = file_name.split(".")[0]
    month_name_abbrev = ""
    for ch in file_name_split:
        if ch.isalpha():
            file_name_char_list.append(ch)
    month_name_abbrev = "".join(file_name_char_list)
    month_name_abbrev = month_name_abbrev.title()
    return (month_abbrev_dict[month_name_abbrev])


# TO CHECK THE QUARTER OF THE YEAR
def getQuarter(file_name):
    monthName = month_name_abbreviation(file_name)
    Q1 = ["January", "February", "March"]
    Q2 = ["April", "May", "June"]
    Q3 = ["July", "August", "September"]
    Q4 = ["October", "November", "December"]

    if monthName in Q1:
        return "Q1"
    elif monthName in Q2:
        return "Q2"
    elif monthName in Q3:
        return "Q3"
    elif monthName in Q4:
        return "Q4"
    else:
        return "Error"


# TO GET THE RELEVANT TOUR DICTIONARY
def get_working_dict(filename):
    quarterName = getQuarter(filename)
    year = now.year

    if year == 2020 and quarterName == "Q4":
        return tour_2020_Q4, "tour_2020_Q4"

    if year == 2021 and quarterName == "Q1":
        return tour_2021_Q1, "tour_2021_Q1"

    if year == 2021 and quarterName == "Q2":
        return tour_2021_Q2, "tour_2021_Q2"

    if year == 2021 and quarterName == "Q3":
        return tour_2021_Q3, "tour_2021_Q3"

    if year == 2021 and quarterName == "Q4":
        return tour_2021_Q4, "tour_2021_Q4"

# TO GET THE LAST 2 DIGITS OF A YEAR
def get_year_suffix():
    year = str(now.year)
    suffix_year = year[2:4]
    return suffix_year

# TO GET THE PRESENT YEAR
def get_year():
    return str(now.year)

# TO CREATE `tour_complete.py` WITH ALL THE DICTIONARY ITEMS
def edit_tour_complete():
    with open(file="tour_complete_copy.py", mode="w", encoding="utf8") as tour_complete_copy:
        tour_complete_copy.write("tour_complete" + " = {\n")

        for key, val in tour_2020_Q4.items():
            dictline = '\t' + '"' + key + '"' + ': ' + str(val) + ',' + '\n'
            tour_complete_copy.write(dictline)

        for key, val in tour_2021_Q1.items():
            dictline = '\t' + '"' + key + '"' + ': ' + str(val) + ',' + '\n'
            tour_complete_copy.write(dictline)

        for key, val in tour_2021_Q2.items():
            dictline = '\t' + '"' + key + '"' + ': ' + str(val) + ',' + '\n'
            tour_complete_copy.write(dictline)

        for key, val in tour_2021_Q3.items():
            dictline = '\t' + '"' + key + '"' + ': ' + str(val) + ',' + '\n'
            tour_complete_copy.write(dictline)

        for key, val in tour_2021_Q4.items():
            dictline = '\t' + '"' + key + '"' + ': ' + str(val) + ',' + '\n'
            tour_complete_copy.write(dictline)

        tour_complete_copy.write("}")
    os.remove("tour_complete.py")
    os.rename(r'tour_complete_copy.py', r'tour_complete.py')


def printhello():
    print("Hello")