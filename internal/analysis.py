import json
import os
import sys

import colorama
from termcolor import cprint


class GlobalVariables:
    pathDelimiter = "../"
    matchingNames = []
    player_dictionary_ag = {}
    player_dictionary_hm = {}
    player_dictionary_ns = {}
    player_dictionary_tz = {}


def find_matching_names(name_list, player_name):
    names_matched = [i for i in name_list if player_name in i]
    GlobalVariables.matchingNames.extend(names_matched)


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


def match_player(total_player_name, analysis_player_name):
    for lst in total_player_name:
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


def player_analysis(player_name, dict):
    print("\n"+player_name.upper())
    print("App:", dict[player_name][2][2])
    print("Goals:", dict[player_name][0])
    print("Assists:", dict[player_name][1])
    print("Avg Goals:", dict[player_name][2][0])
    print("Avg Assists:", dict[player_name][2][1])


def player_comparison(player1, player1_dict, player2, player2_dict):
    print("\n"+"\u0332".join("App "))
    print(player1+":", player1_dict[player1][2][2])
    print(player2+":", player2_dict[player2][2][2])
    print("\n"+"\u0332".join("Goals "))
    print(player1+":", player1_dict[player1][0])
    print(player2+":", player2_dict[player2][0])
    print("\n"+"\u0332".join("Assists "))
    print(player1+":", player1_dict[player1][1])
    print(player2+":", player2_dict[player2][1])
    print("\n"+"\u0332".join("Avg Goals "))
    print(player1+":", player1_dict[player1][2][0])
    print(player2+":", player2_dict[player2][2][0])
    print("\n"+"\u0332".join("Avg Assists "))
    print(player1+":", player1_dict[player1][2][1])
    print(player2+":", player2_dict[player2][2][1])


if __name__ == "__main__":

    try:
        os.listdir(GlobalVariables.pathDelimiter+"files")
    except FileNotFoundError:
        GlobalVariables.pathDelimiter = "./"

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

    ag_player_name = list(GlobalVariables.player_dictionary_ag.keys())
    hm_player_name = list(GlobalVariables.player_dictionary_hm.keys())
    ns_player_name = list(GlobalVariables.player_dictionary_ns.keys())
    tz_player_name = list(GlobalVariables.player_dictionary_tz.keys())

    total_player_name = [ag_player_name,
                         hm_player_name, ns_player_name, tz_player_name]

    # DISPLAYING TITLE
    display_statements_list = [
        "1:  Player analysis  ", "2:  Player comparison"]
    width = len(display_statements_list[1])
    colorama.init()
    print('+-' + '-' * width + '-+')
    for s in display_statements_list:
        try:
            cprint('| {0:^{1}} |'.format(s, width), color='green')
        except:
            print('| {0:^{1}} |'.format(s, width))
        print('+-' + '-'*(width) + '-+')
    task = input("\nYour choice: ").strip()
    try:
        task = int(task)
    except ValueError:
        sys.exit("Invalid input")

    if int(task) == 1:
        analysis_player_name = input(
            "\nName of the player to analyse: ").title().strip()
        dict_name, analysis_player_name = match_player(
            total_player_name, analysis_player_name)
        player_analysis(analysis_player_name, dict_name)

    elif int(task) == 2:
        compare_player1 = input("\nName of the player #1: ").title().strip()
        dict_name1, compare_player1 = match_player(
            total_player_name, compare_player1)
        compare_player2 = input("\nName of the player #2: ").title().strip()
        dict_name2, compare_player2 = match_player(
            total_player_name, compare_player2)
        player_comparison(compare_player1, dict_name1,
                          compare_player2, dict_name2)

    print("\nDONE!")
