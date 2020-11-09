# IMPORTS
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import webbrowser
import script_helper


# OPENING & READING THE TXT FILE
line_count = 0
index_nos = 0
no_of_goals_lists = []
file_name = input("Enter the Filename: ")
try:
    with open('./workspace/' + file_name + ".txt", mode="r", encoding="utf-8") as file:
        no_of_goals_lists.clear()
        data = file.readlines()
        for line in data:
            line_count = line_count + 1
            words = line.split()
            no_of_goals_lists.append(int(words[-1]))
except FileNotFoundError:
    print("There is no such file in the directory\n")
    exit()
except IndexError:
    print("Error in the file syntax\n")
    exit()

if len(no_of_goals_lists) != line_count:
    print("An error occured!\n")
    exit()


# GETTING THE RELEVANT TOUR DICTIONARY
tour, dict_filename = script_helper.get_working_dict(file_name)


# CALCULATING THE SUM OF GOALS
display_statement_1 = ""
sum_of_goals = sum(no_of_goals_lists)
if(line_count == len(no_of_goals_lists)):
    display_statement_1 = "Goals scored in the Tour Event = " + str(sum_of_goals)
else:
    print("Inviad format")


# FINDING THE GOLDEN BOOT WINNER
no_of_goals_lists.sort(reverse=True)
max_goal = no_of_goals_lists[0]
line_with_highest_scorer = ""
try:
    with open('./workspace/' + file_name + ".txt", mode="r", encoding="utf-8") as file:
        data = file.readlines()
        for line in data:
            words = line.split()
            goal_count_in_each_line = str(words[-1])
            if int(goal_count_in_each_line) == max_goal:
                line_with_highest_scorer = line.strip()
except FileNotFoundError:
    print("There is no such file in the directory\n")
    exit()
except IndexError:
    print("Error in the file syntax\n")
    exit()
golden_boot_winner = line_with_highest_scorer[3:line_with_highest_scorer.rfind(" - ")]
display_statement_2 = "GOLDEN BOOT:" + golden_boot_winner.upper() + " with "+ str(max_goal) + " goals"


# PRINTING DISPLAY STATEMENTS IN TABULAR FORMAT
print("\n")
display_statements_list = [display_statement_1, display_statement_2]
if len(display_statement_1) > len(display_statement_2):
    width = len(display_statement_1)
else:
    width = len(display_statement_2)
print('+-' + '-' * width + '-+')
for s in display_statements_list:
    print('| {0:^{1}} |'.format(s, width))
print('+-' + '-'*(width) + '-+')
print("\n")


# EDITING THE OPERATING DICTIONARY FILE WITH NEW KEY AND VALUE
str_new_key = (file_name[0:3] + " " + file_name[3:]).title()
str_new_value = str(sum_of_goals)
year_suffix = script_helper.get_year_suffix()
refactored_string = '\t' + '"' + year_suffix + '-' + str_new_key + '"' + ': ' + str_new_value + ','
operating_filename = dict_filename + ".py"
itte = 0
try:
    with open(operating_filename, mode="r") as inpt:
        with open("operating_file_copy.py", mode="w") as oupt:
            for line in inpt:
                if line.strip("\n") != "}":
                    oupt.write(line)
                    itte += 1
                    if itte == len(tour.values())+1:
                        oupt.write(refactored_string)
                        oupt.write("\n}")
except SyntaxError:
    print("SyntaxError in " + operating_filename)
    exit()
except FileNotFoundError:
    print(operating_filename + " not found")
    exit()


# UPDATING THE KEY & VALUE PAIRS IN MEMORY
key_with_suffix = year_suffix + '-' + str_new_key
tour.update({key_with_suffix: sum_of_goals})


# SHOWING THE GRAPH
print("Showing Graphical Data\n")
key_lists = []
value_lists = []
for key, value in tour.items():
    key_lists.append(key)
    value_lists.append(value)
plt.rcdefaults()
x_pos = np.arange(len(key_lists))
y_pos = value_lists
plt.bar(x_pos, y_pos, align='center', alpha=0.5)
plt.xticks(x_pos, key_lists)
plt_title = script_helper.get_year() + " " + script_helper.getQuarter(file_name)
plt.title(plt_title)
plt.ylabel('Number of goals')
plt.xlabel('Tour event')
for i, v in enumerate(y_pos):
    plt.text(x=i, y=v+1, s=str(v))
mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt_graph_filepath = "statistics/" + plt_title + ".jpg"
plt.savefig(plt_graph_filepath, format='JPEG')
print("Graph saved at",plt_graph_filepath, "\n")
plt.show()


# REMOVING & RENAMING tourdictionary
try:
    os.remove(operating_filename)
    os.rename(r'operating_file_copy.py', operating_filename)
except:
    print("\nError in removing or renaming the file")


# REMOVING DUPLICATE DICTIONARY ITEMS
with open(file="tourdictionaryDupeFixed.py", mode="w", encoding="utf8") as tourdictionaryfixdupe:
    tourdictionaryfixdupe.write(dict_filename + " = {\n")
    for key, val in tour.items():
        dictline = '\t' + '"' + key + '"' + ': ' + str(val) + ',' + '\n'
        tourdictionaryfixdupe.write(dictline)
    tourdictionaryfixdupe.write("}")
os.remove(operating_filename)
os.rename(r'tourdictionaryDupeFixed.py', operating_filename)


# OPENING WEB-BROWSER
choice_open_web_browser = input("Do you want to search about " + golden_boot_winner +"? (y/n): ").lower().strip()
if choice_open_web_browser == 'y' or choice_open_web_browser == '':
    try:
        url = "https://www.google.com.tr/search?q={}".format(golden_boot_winner)
        webbrowser.open_new_tab(url)
        time.sleep(0.5)
    except:
        print("\nError in opening the webbrowser")


# CREATING `tour_complete.py` AS A BACKUP
script_helper.edit_tour_complete()


# FUTURE PLANS 
"""
    1. Copy to clipboard
    2. Image resizing with OPENCV
    3. --Github Readme.md updation-- [complete]

"""