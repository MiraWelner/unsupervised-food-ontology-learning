import re
import sys

import requests

directory = '.'  # current directory is the default
if len(sys.argv) > 1:
    directory = sys.argv[1]  # If the user gives you a directory, use it

# open keyword file
searchWordFile = open(r"searchWordFile.txt", "r")
searchTerms = searchWordFile.read().splitlines()
# open index file
indexFile = requests.get("https://ftp.ncbi.nlm.nih.gov/pub/pmc/manuscript/filelist.csv")
open('indexFile.csv', 'wb').write(indexFile.content)  # Writes to zipfile
with open("indexFile.csv", "r") as openedIndexFile:  # run through indexFile
    openedIndexFile.readline()  # get rid of top line
    for line in openedIndexFile:
        fileName = line[28:38] + ".txt"
        ID = line[39:47]
        metadata = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=" + ID)
        for searchTerm in searchTerms:
            for searchWord in searchTerm.split():
                if re.search("[^a-zA-Z0-9@]" + searchWord + "[^a-zA-Z0-9@]", metadata.text) is not None:
                    print(fileName + " -> " + searchTerm)
searchWordFile.close()
indexFile.close()
