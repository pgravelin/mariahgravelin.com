import os

auditionPhotos = None
dancePhotos = None
designPhotos = None
portraitPhotos = None

mapper = {"audition": auditionPhotos, "dance": dancePhotos, "design": designPhotos, 
            "portraits": portraitPhotos}

def load(pageName):
    basedir = os.path.abspath(os.path.dirname(__file__))[:-4]
    directory = basedir + "static/img/" + pageName
    paths = list()

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            paths.append(os.path.join("../img/", pageName, filename))
            continue
        else:
            continue
        
    return paths

def cachedLoad(pageName): 
    photos = load(pageName) if mapper[pageName] == None else mapper[pageName]
    
    if mapper[pageName] == None:
        mapper[pageName] = photos
        
    print(photos)