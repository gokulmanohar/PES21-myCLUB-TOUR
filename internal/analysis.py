# IMPORTS
import json
import os
import sys
import colorama
from termcolor import cprint
from tabulate import tabulate


# CLASS CONTANING GLOBAL VARIABLES
class GlobalVariables:
    pathDelimiter = "../"
    matchingNames = []
    player_dictionary_ag = {}
    player_dictionary_hm = {}
    player_dictionary_ns = {}
    player_dictionary_tz = {}
    top_stats_numeric_value = []
    top_player_names = []


# SUBSTRING CHECK FOR PLAYER NAME IN THE INPUT
def find_matching_names(name_list, player_name):
    names_matched = [i for i in name_list if player_name in i]
    GlobalVariables.matchingNames.extend(names_matched)


# FINDING THE CORRESPONDING DICTIONARY FOR THE NAME (A-Z)
def dict_according_to_name(player_name):
    alphabets_P1 = list(map(chr, range(65, 72)))
    alphabets_P2 = list(map(chr, range(72, 78)))
    alphabets_P3 = list(map(chr, range(78, 84)))
    alphabets_P4 = list(map(chr, range(84, 91)))
    player_name_first_char = player_name[0]
    if player_name_first_char in alphabets_P1:
        return(GlobalVariables.player_dictionary_ag)
    elif player_name_first_char in alphabets_P2:
        return(GlobalVariables.player_dictionary_hm)
    elif player_name_first_char in alphabets_P3:
        return(GlobalVariables.player_dictionary_ns)
    elif player_name_first_char in alphabets_P4:
        return(GlobalVariables.player_dictionary_tz)
    else:
        return("Error")


# MATCHING PLAYER NAMES & FINDING THE PLAYER TO ANALYSIS
def match_player(total_player_names, analysis_player_name):
    for lst in total_player_names:
        find_matching_names(lst, analysis_player_name)
    if len(GlobalVariables.matchingNames) == 0:
        sys.exit("\nSorry. Player not found.")
    elif len(GlobalVariables.matchingNames) == 1:
        analysis_player_name = GlobalVariables.matchingNames[0]
    else:
        print("["+str(len(GlobalVariables.matchingNames)), "players found]\n")
        index = 1
        for i in GlobalVariables.matchingNames:
            print(str(index)+":", i)
            index += 1
        try:
            name_choice = int(input("\nWhich one? ").strip())
        except ValueError:
            sys.exit("Invalid input")
        try:
            analysis_player_name = GlobalVariables.matchingNames[name_choice-1]
        except IndexError:
            sys.exit("Invalid input")
    GlobalVariables.matchingNames.clear()
    dict_name = dict_according_to_name(analysis_player_name)
    if dict_name == "Error":
        sys.exit("Unicode Error raised while reading the characters")
    else:
        return(dict_name, analysis_player_name)


# PRINTING PLAYER ANALYSIS
def player_analysis(player_name, dict):
    print("\n"+player_name)
    print("App:".title(), dict[player_name][2][2])
    print("Goals:".title(), dict[player_name][0])
    print("Assists:".title(), dict[player_name][1])
    print("Avg Goals:".title(), dict[player_name][2][0])
    print("Avg Assists:".title(), dict[player_name][2][1])


# PRINTING PLAYER COMPARISON
def player_comparison(player1, player1_dict, player2, player2_dict):
    print("\nApp".title())
    print(player1+":", player1_dict[player1][2][2])
    print(player2+":", player2_dict[player2][2][2])
    print("\nGoals".title())
    print(player1+":", player1_dict[player1][0])
    print(player2+":", player2_dict[player2][0])
    print("\nAssists".title())
    print(player1+":", player1_dict[player1][1])
    print(player2+":", player2_dict[player2][1])
    print("\nAvg Goals".title())
    print(player1+":", player1_dict[player1][2][0])
    print(player2+":", player2_dict[player2][2][0])
    print("\nAvg Assists".title())
    print(player1+":", player1_dict[player1][2][1])
    print(player2+":", player2_dict[player2][2][1])


# PRINTING THE BEST PLAYER STATS
def print_best_players(string_param):
    try:
        cprint("\n"+string_param, end="\n", color="green")
    except:
        print("\n"+string_param, end="\n")
    GlobalVariables.top_player_names.sort(key=lambda x: x[1], reverse=True)
    print(tabulate(GlobalVariables.top_player_names,
                   ["Name", "Value"], tablefmt="always"))


# CLEARING THE RECORDS FOR FACILITATING REPEATED EXECUTIONS
def clear_the_max_record():
    GlobalVariables.maximum_value = 0
    GlobalVariables.max_stat_player_name = []
    GlobalVariables.top_stats_numeric_value = []
    GlobalVariables.top_player_names = []


# FINDING THE TOP STAT NUMERICAL VALUES
def top_stat_numerical_values(param, alpha_dict):
    total_numeric_param_list = GlobalVariables.top_stats_numeric_value
    shortened_value_numeric_param_list = []
    limit = 0
    for stat in alpha_dict.values():
        if param == "Goals":
            limit = 5
            total_numeric_param_list.append(stat[0])
        if param == "Assists":
            limit = 5
            total_numeric_param_list.append(stat[1])
        if param == "Appearances":
            limit = 3
            total_numeric_param_list.append(stat[2][2])
    total_numeric_param_list = list(set(total_numeric_param_list))
    total_numeric_param_list.sort(reverse=True)
    if len(total_numeric_param_list) > limit:
        for num in range(0, limit):
            shortened_value_numeric_param_list.append(
                total_numeric_param_list[num])
    else:
        shortened_value_numeric_param_list = total_numeric_param_list
    GlobalVariables.top_stats_numeric_value.clear()
    GlobalVariables.top_stats_numeric_value = shortened_value_numeric_param_list


# FINDING THE TOP PLAYERS
def top_players(top_stat_value_list, param, alpha_dict):
    for stat in alpha_dict.values():
        if param == "Goals":
            index = stat[0]
        elif param == "Assists":
            index = stat[1]
        else:
            index = stat[2][2]
        temp_list = []
        for value in top_stat_value_list:
            if index == value:
                temp_list = [str(list(alpha_dict.keys())[
                    list(alpha_dict.values()).index(stat)]), value]
                GlobalVariables.top_player_names.append(temp_list)


# MAIN
def main():

    # FINDING CORRECT PATH pathDelimiter FOR BAT EXECUTION
    try:
        os.listdir(GlobalVariables.pathDelimiter+"files")
    except FileNotFoundError:
        GlobalVariables.pathDelimiter = "./"

    # READING AND STORING JSON FILES
    try:
        with open(GlobalVariables.pathDelimiter+"playerdata/player_record_ag.json", mode="r", encoding="utf8") as input_json:
            GlobalVariables.player_dictionary_ag = json.load(input_json)
        with open(GlobalVariables.pathDelimiter+"playerdata/player_record_hm.json", mode="r", encoding="utf8") as input_json:
            GlobalVariables.player_dictionary_hm = json.load(input_json)
        with open(GlobalVariables.pathDelimiter+"playerdata/player_record_ns.json", mode="r", encoding="utf8") as input_json:
            GlobalVariables.player_dictionary_ns = json.load(input_json)
        with open(GlobalVariables.pathDelimiter+"playerdata/player_record_tz.json", mode="r", encoding="utf8") as input_json:
            GlobalVariables.player_dictionary_tz = json.load(input_json)
    except FileNotFoundError:
        sys.exit("No files found.")

    # DISPLAYING TITLE
    display_statements_list = [
        "1:  Player analysis", "2:  Player comparison",  "3:  List the top"]
    width = len(display_statements_list[1])
    colorama.init()
    print('+-' + '-' * width + '-+')
    for s in display_statements_list:
        try:
            cprint('| {0:<{1}} |'.format(s, width), color='green')
        except:
            print('| {0:<{1}} |'.format(s, width))
        print('+-' + '-'*(width) + '-+')

    # USER CHOICE
    task = input("\nYour choice: ").strip()
    print("\n")
    try:
        task = int(task)
    except ValueError:
        sys.exit("Invalid input")

    # DETERMINING WHAT TO EXECUTE BASED ON THE USER INPUT
    if int(task) == 1:
        ag_player_names = list(GlobalVariables.player_dictionary_ag.keys())
        hm_player_names = list(GlobalVariables.player_dictionary_hm.keys())
        ns_player_names = list(GlobalVariables.player_dictionary_ns.keys())
        tz_player_names = list(GlobalVariables.player_dictionary_tz.keys())
        total_player_names = [ag_player_names,
                              hm_player_names, ns_player_names, tz_player_names]
        analysis_player_name = input(
            "Player to analyse: ").title().strip()
        dict_name, analysis_player_name = match_player(
            total_player_names, analysis_player_name)
        player_analysis(analysis_player_name, dict_name)

    elif int(task) == 2:
        ag_player_names = list(GlobalVariables.player_dictionary_ag.keys())
        hm_player_names = list(GlobalVariables.player_dictionary_hm.keys())
        ns_player_names = list(GlobalVariables.player_dictionary_ns.keys())
        tz_player_names = list(GlobalVariables.player_dictionary_tz.keys())
        total_player_names = [ag_player_names,
                              hm_player_names, ns_player_names, tz_player_names]
        compare_player1 = input("Player #1: ").title().strip()
        dict_name1, compare_player1 = match_player(
            total_player_names, compare_player1)
        compare_player2 = input("\nPlayer #2: ").title().strip()
        dict_name2, compare_player2 = match_player(
            total_player_names, compare_player2)
        player_comparison(compare_player1, dict_name1,
                          compare_player2, dict_name2)

    elif int(task) == 3:
        total_number_of_players = len(GlobalVariables.player_dictionary_ag) + len(GlobalVariables.player_dictionary_hm) + len(
            GlobalVariables.player_dictionary_ns) + len(GlobalVariables.player_dictionary_tz)
        print("[Analying", total_number_of_players, "players]")
        alpha_dict_combined = [GlobalVariables.player_dictionary_ag, GlobalVariables.player_dictionary_hm,
                               GlobalVariables.player_dictionary_ns, GlobalVariables.player_dictionary_tz]
        # TOP GOAL SCORER
        for i in alpha_dict_combined:
            top_stat_numerical_values("Goals", i)
        top_goals_values = GlobalVariables.top_stats_numeric_value
        for i in alpha_dict_combined:
            top_players(top_goals_values, "Goals", i)
        print_best_players("Top goal scorers")
        clear_the_max_record()

        # TOP ASSIST MAKER
        for i in alpha_dict_combined:
            top_stat_numerical_values("Assists", i)
        top_assists_values = GlobalVariables.top_stats_numeric_value
        for i in alpha_dict_combined:
            top_players(top_assists_values, "Assists", i)
        print_best_players("Top assist maker")
        clear_the_max_record()

        # TOP APPEARANCES
        for i in alpha_dict_combined:
            top_stat_numerical_values("Appearances", i)
        top_assists_values = GlobalVariables.top_stats_numeric_value
        for i in alpha_dict_combined:
            top_players(top_assists_values, "Appearances", i)
        print_best_players("Top appearances")
        clear_the_max_record()
    else:
        sys.exit("Invalid input")
    print("\nDONE!")


if __name__ == "__main__":
    main()
