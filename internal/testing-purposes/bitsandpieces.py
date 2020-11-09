# Multithreading
# save_filenames_and_modified_time_thread = threading.Thread(target=save_filenames_and_modified_time, daemon=False)
# save_filenames_and_modified_time_thread.start()



# Logs
#  mtime = np.format_float_scientific(os.path.getmtime("Files/"+i))

# new file 
# def get_new_file():
#     modified_time_list = []
#     modified_time_list = np.array(modified_time_list)
#     working_filename = ""
#     try:
#         filenames = os.listdir("Files")
#         for i in filenames:
#             mtime = os.path.getmtime("Files/"+i)
#             modified_time_list = np.append(modified_time_list, mtime)
#             modified_time_list = np.sort(modified_time_list)[::-1]
#         modified_time_of_last_files = modified_time_list[0]


#     except error:
#         working_filename = input("Error in locating the new file." +
#                                  error+"Enter it manually (eg: oct1)\t")
#         working_filename = working_filename+".txt"
#         return working_filename
#     # try:
#     #     with open("internal/existing_files.txt", mode="r") as existing_files_txt:
#     #         for line in existing_files_txt:
#     #             if line.split("\t")[2].strip() == str(modified_time_list[0]):
#     #                 working_filename = line.split("\t")[0].strip()
#     #     return working_filename
#     # except error:
#     #     working_filename = input("Error in locating the new file." +
#     #                              error+"Enter it manually (eg: oct1)\t")
#     #     working_filename = working_filename+".txt"
#     #     return working_filename


# save filename and modified_time_list

# def save_filenames_and_modified_time():
#     filenames = os.listdir("Files")
#     with open("internal/existing_files.txt", mode="w+") as existing_files_txt:
#         for i in filenames:
#             mtime = os.path.getmtime("Files/"+i)
#             modified_time = datetime.datetime.fromtimestamp(
#                 mtime).strftime('%d-%m-%Y %H:%M:%S')
#             if i != filenames[-1]:
#                 existing_files_txt.write(
#                     i+"\t"+str(modified_time)+"\t"+str(mtime)+"\n")
#             else:
#                 existing_files_txt.write(
#                     i+"\t"+str(modified_time)+"\t"+str(mtime))