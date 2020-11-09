# IMPORTS
import concurrent.futures
import json
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
import colorama
from termcolor import cprint

class GlobalVariables:
    totalGoals = 0
    totalAssists = 0
    statObjectsList = []
    completePlayerStats = []
    tour = type
    dictFilename = ""
    txtFilename = ""
    pathDelimiter = "../"
    maxPercentageGoalInvolvement = 0
    mostValuablePlayer = ""
    mvpWikiInfo = ""
    AM_PlayerDataDict = {}
    NZ_PlayerDataDict = {}
    script_helper = type

class PlayerStats():
    def __init__(self, name, goals, assists):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.percentage_goal_involvement = np.around(((self.goals*3 + self.assists*2) / (GlobalVariables.totalGoals*3 + GlobalVariables.totalAssists*2) * 100), decimals=2)
        self.single_player_complete_stat = []
        self.single_player_complete_stat.extend([self.name, self.goals, self.assists, self.percentage_goal_involvement])
        GlobalVariables.completePlayerStats.append(self.single_player_complete_stat)
        if self.percentage_goal_involvement > GlobalVariables.maxPercentageGoalInvolvement:
            GlobalVariables.maxPercentageGoalInvolvement = self.percentage_goal_involvement
            GlobalVariables.mostValuablePlayer = self.name

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
        raise Exception("Invalid input. Exiting")

def get_working_dict_from_helper():
    GlobalVariables.script_helper = importlib.import_module("script_helper")
    GlobalVariables.tour, GlobalVariables.dictFilename = GlobalVariables.script_helper.get_working_dict(GlobalVariables.txtFilename)
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
        GlobalVariables.mostValuablePlayer = wikipedia.search(GlobalVariables.mostValuablePlayer)[0]
        WikiInfo = wikipedia.summary(GlobalVariables.mostValuablePlayer, sentences=2)
        if  WikiInfo.find("football") == -1:
            GlobalVariables.mostValuablePlayerWikiInfo = "Sorry. Wikipedia search was not sucessfull"
        else:
            GlobalVariables.mostValuablePlayerWikiInfo = WikiInfo
    except:
        GlobalVariables.mostValuablePlayerWikiInfo = "Sorry. Wikipedia search was not sucessfull"


# SAVING EVERY PLAYER'S TOTAL STATS
def record_player_stats(list_element, player_dict, alph):
    if player_dict != {}:
        if list_element[0] in player_dict.keys():
            goal_updated = player_dict[list_element[0]][0] + list_element[1]
            assist_updated = player_dict[list_element[0]][1] + list_element[2]
            val_updated = {list_element[0]: [goal_updated, assist_updated]}
            if alph == "AM":
                GlobalVariables.AM_PlayerDataDict.update(val_updated)
            else:
                GlobalVariables.NZ_PlayerDataDict.update(val_updated)
        else:
            remaining_lists_dict = {list_element[0]: [
                list_element[1], list_element[2]]}
            if alph == "AM":
                GlobalVariables.AM_PlayerDataDict.update(remaining_lists_dict)
            else:
                GlobalVariables.NZ_PlayerDataDict.update(remaining_lists_dict)
    if player_dict == {}:
        remaining_lists_dict = {list_element[0]: [
            list_element[1], list_element[2]]}
        if alph == "AM":
            GlobalVariables.AM_PlayerDataDict.update(remaining_lists_dict)
        else:
            GlobalVariables.NZ_PlayerDataDict.update(remaining_lists_dict)


def tabular_display(table, headers):
    print("\n")
    print(tabulate(table, headers, tablefmt="pretty"))


# MAIN
if __name__ == "__main__":
    time1 = time.time()


    # FINDING CORRECT PATH DELIMITER FOR BAT EXECUTION
    try:
        os.listdir(GlobalVariables.pathDelimiter+"Files")
    except FileNotFoundError:
        GlobalVariables.pathDelimiter = "./"


    # FINDING THE LATEST MODIFIED FILE
    GlobalVariables.txtFilename = get_new_file(GlobalVariables.pathDelimiter+"Files/")
    if GlobalVariables.txtFilename == '':
        raise FileNotFoundError("No file chosen")
    # GlobalVariables.txtFilename = "oct1.txt"


    # GETTING THE RELEVANT TOUR DICTIONARY
    get_working_dict_from_helper_thread = threading.Thread(target=get_working_dict_from_helper, daemon=False)
    get_working_dict_from_helper_thread.start()

    # READING FROM THE TXT FILE
    every_player_stats = []
    single_player_stat = []
    try:
        with open(file=GlobalVariables.pathDelimiter+"Files/"+GlobalVariables.txtFilename, mode="r", encoding="utf-8") as working_file:
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
        raise FileNotFoundError("There is no such file in the directory\n")
    

    # FINDING TOTAL GOALS & ASSIST NUMBERS
    GlobalVariables.totalGoals = sum_of_goals(every_player_stats)
    GlobalVariables.totalAssists = sum_of_assists(every_player_stats)


    # STORING ALL OBJECTS
    for item in every_player_stats:
        GlobalVariables.statObjectsList.append(PlayerStats(item[0], item[1], item[2]))
    

    # WIKIPEDIA SEARCH THREAD
    wiki_search_thread = threading.Thread(target=wiki_search, daemon=False)
    wiki_search_thread.start()
    

    # SAVING EVERY PLAYERS TOTAL STATS
    analy_mode = input("\nTurn on player analysis mode? (y/n): ").lower().strip()
    if analy_mode == 'y' or analy_mode == '':
        try:
            with open(GlobalVariables.pathDelimiter+"internal/testing-purposes/player-records/player_record_am.json", mode="r", encoding="utf8") as player_record_json:
                try:
                    player_dict_am = json.load(player_record_json)
                except:
                    player_dict_am = {}
            with open(GlobalVariables.pathDelimiter+"internal/testing-purposes/player-records/player_record_nz.json", mode="r", encoding="utf8") as player_record_json:
                try:
                    player_dict_nz = json.load(player_record_json)
                except:
                    player_dict_nz = {}
        except FileNotFoundError:
            with open(GlobalVariables.pathDelimiter+"internal/testing-purposes/player-records/player_record_am.json", mode="w+", encoding="utf8"):
                player_dict_am = {}
            with open(GlobalVariables.pathDelimiter+"internal/testing-purposes/player-records/player_record_nz.json", mode="w+", encoding="utf8"):
                player_dict_nz = {}
        
        alphabets_P1 = list(map(chr, range(65, 78)))
        alphabets_P2 = list(map(chr, range(79, 91)))

        for i in GlobalVariables.completePlayerStats:
            player_name_first_char = i[0][0]
            if player_name_first_char in alphabets_P1:
                record_player_stats(i, player_dict_am, "AM")
            elif player_name_first_char in alphabets_P2:
                record_player_stats(i, player_dict_nz, "NZ")
            else:
                print("Unicode error:", player_name_first_char, "in", i[0]+". Skipping")
                pass

        player_dict_am.update(GlobalVariables.AM_PlayerDataDict)
        player_dict_nz.update(GlobalVariables.NZ_PlayerDataDict)
        GlobalVariables.AM_PlayerDataDict.clear()
        GlobalVariables.NZ_PlayerDataDict.clear()

        with open(GlobalVariables.pathDelimiter+"internal/testing-purposes/player-records/player_record_am.json", mode="w+", encoding="utf8") as output_json_am:  
            json.dump(player_dict_am, output_json_am, sort_keys=True, indent=4) 
        with open(GlobalVariables.pathDelimiter+"internal/testing-purposes/player-records/player_record_nz.json", mode="w+", encoding="utf8") as output_json_nz:  
            json.dump(player_dict_nz, output_json_nz, sort_keys=True, indent=4)


    #SORTING TABLE
    table = GlobalVariables.completePlayerStats
    sorting_method = input("\nSpecify sorting method (1:Default | 2:Name | 3:Goals | 4:Assist | 5:Percentage involvement): ").lower().strip()
    if sorting_method == "1" or sorting_method == '':
        pass
    elif sorting_method == '2':
        table.sort(key = lambda x: x[0], reverse=False)
    elif sorting_method == '3':
        table.sort(key = lambda x: x[1], reverse=True)
    elif sorting_method == '4':
        table.sort(key = lambda x: x[2], reverse=True)
    elif sorting_method == '5':
        table.sort(key = lambda x: x[3], reverse=True)
    else:
        print("Input not valid. Default sorting selected")
        pass


    # DISPLAYING THE COMPLETE PLAYER STATS IN A PRETTY TABULAR FORMAT ALONG WITH TOTAL GOALS & ASSISTS
    tabular_display(table, ["Name", "Goals", "Assits", "% Involvement"])
    print("Total Goals:", GlobalVariables.totalGoals, "\tTotal Assists:",GlobalVariables.totalAssists)


    # DISPLAYING MVP & WIKIPEDIA INFO
    colorama.init()
    print("\nMVP: ", end='')
    cprint(GlobalVariables.mostValuablePlayer, color='green')
    disp_mvp_info = input("\nDo you want to know about "+GlobalVariables.mostValuablePlayer+"? (y/n): ").lower().strip()
    if disp_mvp_info == 'y' or disp_mvp_info == '':
        wiki_search_thread.join()
        print(GlobalVariables.mostValuablePlayerWikiInfo+"\n")
        srch_about_mvp = input("Want to know more (y/n): ").lower().strip()
        if srch_about_mvp == 'y':
            try:
                url = "https://www.google.com.tr/search?q={}".format(GlobalVariables.mostValuablePlayer)
                print("Searching about", GlobalVariables.mostValuablePlayer+". Opening web-browser")
                time.sleep(0.3)
                webbrowser.open_new_tab(url)
            except:
                raise Exception("\nError in opening the webbrowser")


    # UPDATING THE WORKING DICTIONARY WITH NEW FILE'S TOTAL GOALS
    get_working_dict_from_helper_thread.join()
    year_suffix = GlobalVariables.script_helper.get_year_suffix()
    raw_file_name = GlobalVariables.txtFilename.split(".txt")[0]
    updated_key = year_suffix + '-' + (GlobalVariables.txtFilename[0:3] + "-" + raw_file_name[3:]).title()
    GlobalVariables.tour.update({updated_key: GlobalVariables.totalGoals})
    with open(GlobalVariables.pathDelimiter+"internal/"+GlobalVariables.dictFilename+".json", mode="w+", encoding="utf8") as dict_json:  
        json.dump(GlobalVariables.tour, dict_json, indent=4)


    # SHOWING THE GRAPH
    graph_show = input("\nSave graphical data? (y/n): ").lower().strip()
    if graph_show == 'y' or graph_show == '':
        key_lists = []
        value_lists = []
        for key, value in GlobalVariables.tour.items():
            key_lists.append(key)
            value_lists.append(value)
        x_pos = np.arange(len(key_lists))
        y_pos = value_lists
        plt.rcdefaults()
        plt.bar(x_pos, y_pos, align='center', alpha=0.5)
        plt.xticks(x_pos, key_lists)
        plt_title = GlobalVariables.script_helper.get_year() + " " + GlobalVariables.script_helper.getQuarter(GlobalVariables.txtFilename)
        plt.title(plt_title)
        plt.ylabel('Number of goals')
        plt.xlabel('Tour event')
        for i, v in enumerate(y_pos):
            plt.text(x=i, y=v+1, s=str(v))
        plt_graph_filepath = GlobalVariables.pathDelimiter+"statistics/" + plt_title + ".jpg"
        mng = plt.get_current_fig_manager()
        mng.window.state("zoomed")
        plt.savefig(plt_graph_filepath, format='JPEG')
        plt.show()
        print("\nGraph saved at",plt_graph_filepath)



    time2 = time.time()
    print("\nTime taken for execution is", time2-time1)