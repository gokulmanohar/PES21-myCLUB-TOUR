import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from os import listdir as oslistdir
from json import load as jsonload

fl = oslistdir()
json_file_list = []
for i in fl:
    if i.endswith(".json"):
        json_file_list.append(i)
for i in json_file_list:
    f_name = str(i.split(".")[0])
    json_dict_year = f_name.split("_")[1]
    json_dict_quarter = f_name.split("_")[2]
    print("\n--- " + f_name + " ---")
    with open(file=str(i), mode='r', encoding="utf-8") as j_f:
        j_dict = jsonload(j_f)
        key_lists = []
        value_lists = []
        for key, value in j_dict.items():
            key_lists.append(key)
            value_lists.append(value)
        x_pos = np.arange(len(key_lists))
        y_pos = value_lists
        plt.rcdefaults()
        plt.bar(x_pos, y_pos, align='center', alpha=0.5)
        plt.xticks(x_pos, key_lists)
        plt_title = json_dict_year + " " + json_dict_quarter
        plt.title(plt_title)
        plt.ylabel('Number of goals')
        plt.xlabel('Tour event')
        for i, v in enumerate(y_pos):
            plt.text(x=i, y=v+1, s=str(v))
        plt_graph_filepath = "statistics/" + plt_title + ".jpg"
        root = Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()
        figure = plt.gcf()
        figure.set_size_inches(screen_width/100, screen_height/100)
        plt.savefig(plt_graph_filepath, format='JPEG')
        # mng = plt.get_current_fig_manager()
        # mng.window.state("zoomed")
        # plt.show()
        plt.clf()
        print("\nGraph saved at", plt_graph_filepath)

