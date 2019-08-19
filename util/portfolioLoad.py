import os

auditionFiles = list()
danceFiles = list()
designFiles = list()
portraitFiles = list()

auditionHTML = ""
danceHTML = ""
designHTML = ""
portraitHTML = ""

mapper = {"audition": [auditionHTML, auditionFiles], "dance": [danceHTML, danceFiles], 
          "design": [designHTML, designFiles], "portraits": [portraitHTML, portraitFiles]}

def load(dir_list, pageName):
    print("LOADING")
    paths = list()

    for file in dir_list:
        if file.endswith(".jpg") or file.endswith(".png"): 
            paths.append(os.path.join("../img/", pageName, file))
        
    return paths

def generateHTML(paths):
    return "OK"

def cachedLoad(pageName): 
    basedir = os.path.abspath(os.path.dirname(__file__))[:-4]
    directory = basedir + "static/img/" + pageName
    dir_list = os.listdir(directory)
    
    if mapper[pageName][1] != dir_list:
        mapper[pageName][0] = generateHTML(load(dir_list, pageName))
        mapper[pageName][1] = dir_list
        return mapper[pageName][0]
    else:
        return mapper[pageName][0]
    