import json
import os


# GLOBAL VARIABLE CLASS
class GV:
    pathDelimiter = "./"
    AM_PlayerDataDict = {}
    NZ_PlayerDataDict = {}


# SAVING EVERY PLAYERS TOTAL STATS
def record_player_stats(list_element, player_dict, alph):
    if player_dict != {}:
        if list_element[0] in player_dict.keys():
            goal_updated = player_dict[list_element[0]][0] + list_element[1]
            assist_updated = player_dict[list_element[0]][1] + list_element[2]
            val_updated = {list_element[0]: [goal_updated, assist_updated]}
            if alph == "AM":
                GV.AM_PlayerDataDict.update(val_updated)
            else:
                GV.NZ_PlayerDataDict.update(val_updated)
        else:
            remaining_lists_dict = {list_element[0]: [
                list_element[1], list_element[2]]}
            if alph == "AM":
                GV.AM_PlayerDataDict.update(remaining_lists_dict)
            else:
                GV.NZ_PlayerDataDict.update(remaining_lists_dict)
    if player_dict == {}:
        remaining_lists_dict = {list_element[0]: [
            list_element[1], list_element[2]]}
        if alph == "AM":
            GV.AM_PlayerDataDict.update(remaining_lists_dict)
        else:
            GV.NZ_PlayerDataDict.update(remaining_lists_dict)


# MAIN
if __name__ == "__main__":

    pathDelimiter = "./"
    try:
        os.listdir('internal')
    except FileNotFoundError:
        pathDelimiter = "../"
    try:
        with open("internal/testing-purposes/player-records/player_record_am.json", mode="r", encoding="utf8") as player_record_json:
            try:
                player_dict_am = json.load(player_record_json)
            except:
                player_dict_am = {}
        with open("internal/testing-purposes/player-records/player_record_nz.json", mode="r", encoding="utf8") as player_record_json:
            try:
                player_dict_nz = json.load(player_record_json)
            except:
                player_dict_nz = {}
    except FileNotFoundError:
        with open("internal/testing-purposes/player-records/player_record_am.json", mode="w+", encoding="utf8"):
            player_dict_am = {}
        with open("internal/testing-purposes/player-records/player_record_nz.json", mode="w+", encoding="utf8"):
            player_dict_nz = {}

    # lst = [['Petr Čech', 0, 0, 0.0], ['Joshua Kimmich', 0, 2, 1.29], ['Jonathan Tah', 0, 0, 0.0], ['Virgil van Dijk', 0, 1, 0.65], ['Andrew Robertson', 0, 2, 1.29], ['Andrés Iniesta', 6, 2, 7.1], ['Patrick Vieira', 2, 0, 1.94], ['Paul Scholes', 0, 2, 1.29], ['Lionel Messi', 16, 10, 21.94], ['Kylian Mbappé', 7, 13, 15.16], ['Cristiano Ronaldo', 21, 6, 24.19], ['Marc-André ter Stegen', 0,



    #                                                                                                                                                                                                                                                                                                                                                                       0, 0.0], ['Alessio Romagnoli', 0, 0, 0.0], ['Paul Pogba', 0, 0, 0.0], ['Luis Alberto', 1, 0, 0.97], ['Eden Hazard', 0, 1, 0.65], ['Serge Gnabry', 1, 1, 1.61], ['Marco van Basten', 7, 6, 10.65], ['Rodrygo', 3, 2, 4.19], ['Weston McKennie', 0, 1, 0.65], ['Adama Traoré', 2, 1, 2.58], ['Alexander Isak', 1, 2, 2.26], ['Sandro Tonali', 0, 1, 0.65], ['Erling Braut Håland', 1, 0, 0.97]]
    

    alphabets_P1 = list(map(chr, range(65, 78)))
    alphabets_P2 = list(map(chr, range(79, 91)))

    for i in lst:
        player_name_first_char = i[0][0]
        if player_name_first_char in alphabets_P1:
            record_player_stats(i, player_dict_am, "AM")
        elif player_name_first_char in alphabets_P2:
            record_player_stats(i, player_dict_nz, "NZ")
        else:
            print("Unicode error:", player_name_first_char, "in", i[0]+". Skipping")
            pass

    player_dict_am.update(GV.AM_PlayerDataDict)
    player_dict_nz.update(GV.NZ_PlayerDataDict)

    with open("internal/testing-purposes/player-records/player_record_am.json", mode="w+", encoding="utf8") as output_json_am:  
        json.dump(player_dict_am, output_json_am, sort_keys=True, indent=4) 
    with open("internal/testing-purposes/player-records/player_record_nz.json", mode="w+", encoding="utf8") as output_json_nz:  
        json.dump(player_dict_nz, output_json_nz, sort_keys=True, indent=4)