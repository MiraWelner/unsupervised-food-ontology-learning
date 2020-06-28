"""
Authors:
    Mira Welner -mewelner@ucdavis.edu
Description:
    Search for keywords in metadata files
To-do:
"""
import logging
# standard imports
import os
import sys

# local imports
from set_logging import set_logging

set_logging(log_level=logging.INFO)

DIRECTORY = '.'  # current directory is the default
if len(sys.argv) > 1:
    DIRECTORY = sys.argv[1]  # If the user gives you a directory, use it

# open keyword file
searchWordFile = open(r"search_word_file.txt", "r")
searchTerms = searchWordFile.read().splitlines()

logging.info('Searching %s', DIRECTORY)
for file in os.listdir(DIRECTORY):
    if file.endswith('json'):
        with open(DIRECTORY + "/" + file, "r") as openfile:
            metadata = openfile.read()
        for searchTerm in searchTerms:
            for searchWord in searchTerm.split():
                if searchWord in metadata is not None:
                    location = metadata.find("PMC")
                    ID = metadata[location:location + 10] + '.json'
                    print(ID + " -> " + searchWord)
searchWordFile.close()
