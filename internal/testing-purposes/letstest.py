from threading import main_thread
import wikipedia
from tabulate import tabulate

#     print(wikipedia.suggest("Ronaldo"))


def wiki():

    # print(wikipedia.search("C. Ronaldo"))
    player_inp = "MARCO ASENSIO"
    print(wikipedia.search(player_inp))
    player = wikipedia.search(player_inp)[0]
    print("Details of:", player)

    try:
        wiki_info = wikipedia.summary(player, sentences=2)
        if wiki_info.find("football") == -1:
            print("<wikipedia search not sucessfull>")
            print(wiki_info)
        else:
            print(wiki_info)
    except:
        print("wikipedia search not sucessfull")


def tabularpr():
    table = [['Cristiano Ronaldo', 21, 6, 24.19], ['Lionel Messi', 16, 10, 21.94], ['Kylian Mbappé', 7, 13, 15.16], ['Marco van Basten', 7, 6, 10.65], ['Andrés Iniesta', 6, 2, 7.1], ['Rodrygo', 3, 2, 4.19], ['Adama Traoré', 2, 1, 2.58], ['Alexander Isak', 1, 2, 2.26], ['Patrick Vieira', 2, 0, 1.94], ['Serge Gnabry', 1, 1, 1.61], ['Joshua Kimmich', 0, 2, 1.29], ['Andrew Robertson', 0, 2, 1.29], ['Paul Scholes',
                                                                                                                                                                                                                                                                                                                                                                                                              0, 2, 1.29], ['Luis Alberto', 1, 0, 0.97], ['Erling Braut Håland', 1, 0, 0.97], ['Virgil van Dijk', 0, 1, 0.65], ['Eden Hazard', 0, 1, 0.65], ['Weston McKennie', 0, 1, 0.65], ['Sandro Tonali', 0, 1, 0.65], ['Petr Čech', 0, 0, 0.0], ['Jonathan Tah', 0, 0, 0.0], ['Marc-André ter Stegen', 0, 0, 0.0], ['Alessio Romagnoli', 0, 0, 0.0], ['Paul Pogba', 0, 0, 0.0]]
    headers = ["Name", "Goals", "Assits", "% Involvement"]
    print(tabulate(table, headers, tablefmt="pretty"))

    # table = [["Sun", 696000, 1989100000], ["Earth", 6371, 5973.6],
    #          ["Moon", 1737, 73.5], ["Mars", 3390, 641.85]]


    # print(tabulate(table))

if __name__ == "__main__":
    tabularpr()
    # wiki()
