import os
import sys
import re

def listDataFiles():
    dataPath = "/srv/data"
    files = []
    for f in os.listdir(dataPath):
        if os.path.isfile(os.path.join(dataPath, f)):
            fn = re.sub('\.json$', '', f)
            files.append({
                "filename": f,
                "name": fn.lower(),
                "display": fn.capitalize()
            })
    return files