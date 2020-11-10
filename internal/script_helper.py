# IMPORTS
from datetime import datetime
import os
import json


# READING FROM JSON FILE
def read_from_json(json_file_path):
    with open(json_file_path, mode="r", encoding="utf8") as json_file:
        return json.load(json_file)


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
    elif file_name.startswith("dec"):
        return "Q4"
    else:
        return "Error"


# TO GET THE RELEVANT TOUR DICTIONARY
def get_working_dict(filename):
    quarterName = getQuarter(filename)
    year = now.year
    if year == 2020 and quarterName == "Q4":
        return tour_2020_Q4, "tour_2020_Q4"
    if year == 2021 and filename.startswith("dec"):
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


# PRELOAD
now = datetime.now()
pathDelimiter = "./"
try:
    os.listdir('internal')
except FileNotFoundError:
    pathDelimiter = "../"
try:
    with open(pathDelimiter+"internal/tour_2020_Q4.json", mode="r", encoding="utf8") as input_json:   
        try: 
            tour_2020_Q4 = read_from_json(pathDelimiter+"internal/tour_2020_Q4.json")
        except:
            tour_2020_Q4 = {}
    with open(pathDelimiter+"internal/tour_2021_Q1.json", mode="r", encoding="utf8") as input_json:   
        try: 
            tour_2021_Q1 = read_from_json(pathDelimiter+"internal/tour_2021_Q1.json")
        except:
            tour_2021_Q1 = {}
    with open(pathDelimiter+"internal/tour_2021_Q2.json", mode="r", encoding="utf8") as input_json:   
        try: 
            tour_2021_Q2 = read_from_json(pathDelimiter+"internal/tour_2021_Q2.json")
        except:
            tour_2021_Q2 = {}
    with open(pathDelimiter+"internal/tour_2021_Q3.json", mode="r", encoding="utf8") as input_json:   
        try: 
            tour_2021_Q3 = read_from_json(pathDelimiter+"internal/tour_2021_Q3.json")
        except:
            tour_2021_Q3 = {}
    with open(pathDelimiter+"internal/tour_2021_Q4.json", mode="r", encoding="utf8") as input_json:   
        try: 
            tour_2021_Q4 = read_from_json(pathDelimiter+"internal/tour_2021_Q4.json")
        except:
            tour_2021_Q4 = {}
except:
    with open(pathDelimiter+"internal/tour_2020_Q4.json", mode="w+", encoding="utf8"):
        tour_2020_Q4 = {}
    with open(pathDelimiter+"internal/tour_2021_Q1.json", mode="w+", encoding="utf8"):
        tour_2021_Q1 = {}
    with open(pathDelimiter+"internal/tour_2021_Q2.json", mode="w+", encoding="utf8"):
        tour_2021_Q2 = {}
    with open(pathDelimiter+"internal/tour_2021_Q3.json", mode="w+", encoding="utf8"):
        tour_2021_Q3 = {}
    with open(pathDelimiter+"internal/tour_2021_Q4.json", mode="w+", encoding="utf8"):
        tour_2021_Q4 = {}

