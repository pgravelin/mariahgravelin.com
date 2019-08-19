import os

def load(pageName):
    basedir = os.path.abspath(os.path.dirname(__file__))[:-4]
    basedir.strip("/util")
    directory = basedir + "/static/img/" + pageName

    for file in os.listdir( directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            print(os.path.join(directory, filename))
            continue
        else:
            continue