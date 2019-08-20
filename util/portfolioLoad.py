import os
from flask import Markup

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

def generateHTML(files, pageName):
    html = list()
    for fileName in files:
        html.append("<div class='grid-item'>")
        html.append("<img src='../static/img/%s/%s')> " % \
            (pageName, fileName))
        html.append("</div>")
    return Markup("".join(html))

def cachedLoad(pageName): 
    basedir = os.path.abspath(os.path.dirname(__file__))[:-4]
    directory = basedir + "static/img/" + pageName
    files = os.listdir(directory)
    
    if mapper[pageName][1] != files:
        mapper[pageName][0] = generateHTML(files, pageName)
        mapper[pageName][1] = files
        return mapper[pageName][0]
    else:
        return mapper[pageName][0]
    