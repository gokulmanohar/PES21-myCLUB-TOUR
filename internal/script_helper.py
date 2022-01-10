# IMPORTS
import os
import json
from pathlib import Path


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
    month_name_abbrev = ''
    file_name_split = str(file_name.split(".")[0])
    global year_in_filename
    year_in_filename = int(file_name_split.split('-')[0])
    month_name_abbrev = file_name_split.split('-')[1]
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
    pathDelimiter = "./"
    try:
        os.listdir('internal')
    except FileNotFoundError:
        pathDelimiter = "../"
    tour_dict_file_name = ''
    tour_dict_file = None
    quarterName = getQuarter(filename)
    year = year_in_filename
    tour_dict_file_name = 'tour_' + str(year) + '_' + str(quarterName)
    tour_dict_file_path = Path(
        pathDelimiter + 'internal/' + tour_dict_file_name + '.json')
    tour_dict_file_path.touch(exist_ok=True)
    try:
        with open(pathDelimiter + 'internal/' + tour_dict_file_name + '.json', mode="r", encoding="utf8") as json_file:
            tour_dict_file = json.load(json_file)
    except json.decoder.JSONDecodeError:
        tour_dict_file = {}
    return(tour_dict_file, tour_dict_file_name) # eg: tour_2020_Q4, 'tour_2020_Q4'


# MAIN
# if __name__ == "__main__":
#     dct, dct_name = get_working_dict('2021-dec-4.txt')
#     print('------- ' + dct_name + ' -------')
#     print(dct)
