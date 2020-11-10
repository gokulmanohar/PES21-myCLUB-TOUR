import shutil
import os

filetypes = {
    "files": ".txt",
    "statistics": ".jpg",
    "playerdata": ".json",
    "internal": ".json"
}

for k, v in filetypes.items():
    foldername = k
    f_format = v

    filenames = [f for f in os.listdir(foldername+"/New folder") if f.endswith(f_format)]
    for f in filenames:
        for i in range(2):
            shutil.copy2(foldername+'/New folder/'+f, foldername+'/'+str(f).split(".")[0]+str(i)+f_format)