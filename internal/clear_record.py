import os
import sys
import colorama
from termcolor import cprint


class GlobalVariables:
    pathDelimiter = "../"
    clear_check = 0


def clear_files(directory_name, file_format):
    files = [f for f in os.listdir(
        GlobalVariables.pathDelimiter+directory_name) if f.endswith(file_format)]
    print("\nFrom "+os.path.abspath(GlobalVariables.pathDelimiter+directory_name))
    try:
        cprint("[Removing]", color="cyan")
    except:
        print("[Removing]")
    for f in files:
        try:
            os.remove(GlobalVariables.pathDelimiter+directory_name+"/"+f)
        except:
            clear_complete(1, f)
        clear_complete(0, f)
    if GlobalVariables.clear_check == 1:
        print("Error in deleting one or more files")


def clear_complete(flag, file_name):
    if flag == 0:
        try:
            cprint("Successfully deleted ", color="green", end='')
        except:
            print("Successfully deleted ", end='')
        print(file_name)
    else:
        GlobalVariables.clear_check = 1
        try:
            cprint("Failed to delete ", color="green", end='')
        except:
            print("Failed to delete ", end='')
        print(file_name)


def main():

    try:
        colorama.init()
        cprint("Warning! ", color="red", end='')
    except:
        print("Warning! ", end='')
    c = input(
        "This will clear all the records.\nDo you want to continue? (Type 'yes' for confirmation): ").lower().strip()

    try:
        os.listdir(GlobalVariables.pathDelimiter+"files")
    except FileNotFoundError:
        GlobalVariables.pathDelimiter = "./"

    if c == 'yes':
        filetypes = {
            "files": ".txt",
            "statistics": ".jpg",
            "playerdata": ".json",
            "internal": ".json"
        }
        for k, v in filetypes.items():
            clear_files(k, v)

    elif c == 'n':
        sys.exit("Exiting")
    else:
        sys.exit("Invalid input")

if __name__ == "__main__":
    main()