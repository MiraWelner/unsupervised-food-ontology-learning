import os
import sys
import re

directory = '.'  # current directory is the default
if len(sys.argv) > 1:
    directory = sys.argv[1]  # If the user gives you a directory, use it

searchWordFile = open(r"searchWordFile.txt", "r")
searchWords = searchWordFile.read().splitlines()
for file in os.listdir(directory):  # iterates through files
    for searchPhrase in searchWords:  # iterates through search phrases
        for searchWord in searchPhrase.split():  # searches for words in search phrases
            fileToSearch = open(directory + "/" + file, "r")
            fileToSearch.readline()  # metadata is the fourth line in the page
            fileToSearch.readline()
            fileToSearch.readline()
            metadata = fileToSearch.readline().lower()
            # finds if term is individual non-email word
            if re.search("[^a-zA-Z0-9@]" + searchWord + "[^a-zA-Z0-9@]", metadata) is not None:
                print(file + " -> " + searchWord)
searchWordFile.close()
