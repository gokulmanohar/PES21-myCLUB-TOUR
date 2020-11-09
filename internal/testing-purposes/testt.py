import  wikipedia
class GlobalVariables:
    mostValuablePlayer = "Lionel Messi"
    mostValuablePlayerWikiInfo = ""

def wiki_search(index):
    GlobalVariables.mostValuablePlayer = wikipedia.search(GlobalVariables.mostValuablePlayer)[index]
    result = wikipedia.search(GlobalVariables.mostValuablePlayer, results = 5) 
    print (result)
    # WikiInfo = wikipedia.summary(result[0], sentences=2)
    print(wikipedia.suggest(result[0]))

    # wiki_search(1)
    # GlobalVariables.mostValuablePlayerWikiInfo = WikiInfo
    # print(WikiInfo)


print("\nMVP: ", end='')
print(GlobalVariables.mostValuablePlayer)
disp_mvp_info = input("\nDo you want to know about "+GlobalVariables.mostValuablePlayer+"? (y/n): ").lower().strip()
if disp_mvp_info == 'y' or disp_mvp_info == '':
    wiki_search(0)
    # print(GlobalVariables.mostValuablePlayerWikiInfo+"\n")