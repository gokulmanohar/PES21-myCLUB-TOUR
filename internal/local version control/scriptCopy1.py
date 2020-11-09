# IMPORTS
import threading
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
import os
import webbrowser
from tkinter.filedialog import askopenfilename
# import script_helper


def get_new_file():
    file_path = "../Files"
    try:
        list_of_files = os.listdir(file_path)
    except FileNotFoundError:
        file_path = "./Files"
    list_of_files = os.listdir(file_path)
    modified_time_of_new_file = np.format_float_scientific(os.path.getmtime(file_path+"/"+list_of_files[0]))
    filename = list_of_files[0]
    for i in list_of_files:
        mtime = np.format_float_scientific(os.path.getmtime(file_path+"/"+i))
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
        print("Invalid input. Exiting")
        exit()


if __name__ == "__main__":

    time1 = time.time()

    filename = get_new_file()
    print(filename)

    time2 = time.time()

    print("Time taken for execution is", time2-time1)
