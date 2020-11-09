# IMPORTS
import concurrent.futures
import importlib
import threading
import datetime
import time
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import os
import webbrowser
from tkinter.filedialog import askopenfilename

from wikipedia import wikipedia
# import script_helper

class GlobalVariables:
    totalGoals = 0
    totalAssists = 0
    statObjectsList = []
    completePlayerStats = []
    tour = type
    dictFilename = ""
    txtFilename = ""
    relativePath = "../"
    MVP = ""
    mvpWikiInfo = ""

class PlayerStats():
    def __init__(self, name, goals, assists):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.percentage_goal_involvement = np.around(((self.goals*3 + self.assists*2) / (GlobalVariables.totalGoals*3 + GlobalVariables.totalAssists*2) * 100), decimals=2)
        self.single_player_complete_stat = []
        self.single_player_complete_stat.extend([self.name, self.goals, self.assists, self.percentage_goal_involvement])
        GlobalVariables.completePlayerStats.append(self.single_player_complete_stat)

    def Print_Stats(self):
        print(self.name, "has", self.goals, "goals and", self.assists, "Assists with", str(self.percentage_goal_involvement)+"%"+" Goal involvement")


def get_new_file(filesPath):
    list_of_files = os.listdir(filesPath)
    modified_time_of_new_file = np.format_float_scientific(os.path.getmtime(filesPath+list_of_files[0]))
    filename = list_of_files[0]
    for i in list_of_files:
        mtime = np.format_float_scientific(os.path.getmtime(filesPath+i))
        if mtime > modified_time_of_new_file:
            modified_time_of_new_file = mtime
            filename = i
    print("New file found: ",filename)
    cont = input("Continue? (y/n): ").lower().strip()
    print("\n")
    if cont == 'y' or cont == '':
        return filename
    elif cont == 'n':
        manual_file_select = input("Manual override. Enter filename manually (eg. jan1): ").lower().strip()
        manual_file_select = manual_file_select+".txt"
        if manual_file_select not in list_of_files:
            print("Cannot find ",manual_file_select+". Opening filepicker")
            time.sleep(0.3)
            abs_pdf_path = askopenfilename(filetypes=[('Text Document', '*.txt')])
            tfilename = str(abs_pdf_path).split('/')[-1]
            return tfilename
        else:
            return manual_file_select
    else:
        print("Invalid input. Exiting")
        exit()

def get_working_dict_from_helper():
    script_helper = importlib.import_module("script_helper")
    GlobalVariables.tour, GlobalVariables.dictFilename = script_helper.get_working_dict(GlobalVariables.txtFilename)
    # print("Working Dict =", GlobalVariables.tour)


def sum_of_goals(every_player_stats):
    goal_list = []
    goal_list = np.array(goal_list)
    for i in every_player_stats:
        goal_list = np.append(goal_list, i[1])
    return (int(np.sum(goal_list)))

def sum_of_assists(every_player_stats):
    assist_list = []
    assist_list = np.array(assist_list)
    for i in every_player_stats:
        assist_list = np.append(assist_list, i[2])
    return (int(np.sum(assist_list)))

def wiki_search():
    try:
        GlobalVariables.MVP = wikipedia.search(GlobalVariables.MVP)[0]
        WikiInfo = wikipedia.summary(GlobalVariables.MVP, sentences=2)
        if  WikiInfo.find("football") == -1:
            GlobalVariables.mvpWikiInfo = "Sorry. Wikipedia search was not sucessfull"
        else:
            GlobalVariables.mvpWikiInfo = WikiInfo
    except:
        GlobalVariables.mvpWikiInfo = "Sorry. Wikipedia search was not sucessfull"

def tabular_display(table, headers):
    print(tabulate(table, headers, tablefmt="pretty"))


if __name__ == "__main__":
    time1 = time.time()

    try:
        os.listdir(GlobalVariables.relativePath+"Files")
    except FileNotFoundError:
        GlobalVariables.relativePath = "./"

    GlobalVariables.txtFilename = get_new_file(GlobalVariables.relativePath+"Files/")
    # GlobalVariables.txtFilename = "oct1.txt"


    get_working_dict_from_helper_thread = threading.Thread(target=get_working_dict_from_helper, daemon=False)
    get_working_dict_from_helper_thread.start()

    every_player_stats = []
    single_player_stat = []
    try:
        with open(file=GlobalVariables.relativePath+"Files/"+GlobalVariables.txtFilename, mode="r", encoding="utf-8") as working_file:
            for line in working_file:
                if line.startswith("Player Name"):
                    continue
                else:
                    line = line.strip().split("\t")
                    param1 = str(line[0])
                    param2 = int(line[1])
                    param3 = int(line[2])
                    single_player_stat.extend([param1, param2, param3])
                    every_player_stats.append(list(single_player_stat))
                    single_player_stat.clear()
    except FileNotFoundError:
        print("There is no such file in the directory\n")
        exit()
    
    GlobalVariables.totalGoals = sum_of_goals(every_player_stats)
    GlobalVariables.totalAssists = sum_of_assists(every_player_stats)

    for item in every_player_stats:
        # STORING ALL OBJECTS
        GlobalVariables.statObjectsList.append(PlayerStats(item[0], item[1], item[2]))

    GlobalVariables.completePlayerStats.sort(key = lambda x: x[3], reverse=True)

    GlobalVariables.MVP = GlobalVariables.completePlayerStats[0][0]
    wiki_search_thread = threading.Thread(target=wiki_search, daemon=False)
    wiki_search_thread.start()


    # DISPLAYING THE COMPLETE PLAYER STATS IN A PRETTY TABULAR FORMAT
    tabular_display(GlobalVariables.completePlayerStats, ["Name", "Goals", "Assits", "% Involvement"])


    # DISPLAYING MVP & WIKIPEDIA INFO
    print("\n")
    print("MVP:", GlobalVariables.MVP)
    print("\n")
    disp_mvp_info = input("Do you want to know about "+GlobalVariables.MVP+"? (y/n): ").lower().strip()
    if disp_mvp_info == 'y' or disp_mvp_info == '':
        wiki_search_thread.join()
        print("\n"+GlobalVariables.mvpWikiInfo+"\n")
        srch_about_mvp = input("Want to know more (y/n): ").lower().strip()
        if srch_about_mvp == 'y':
            try:
                url = "https://www.google.com.tr/search?q={}".format(GlobalVariables.MVP)
                print("Searching about", GlobalVariables.MVP+". Opening web-browser")
                time.sleep(0.5)
                webbrowser.open_new_tab(url)
            except:
                print("\nError in opening the webbrowser")
        


    time2 = time.time()
    print("\nTime taken for execution is", time2-time1)