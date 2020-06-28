"""
Authors:
    Mira Welner -mewelner@ucdavis.edu
Description:
    Download all public domain files and metadata from PubMed.
To-do:
"""
import logging
# standard imports
import os
import shutil
import sys
import tarfile

import wget

# local imports
from set_logging import set_logging

set_logging(log_level=logging.INFO)

DIRECTORY = '.'  # current directory is the default
if len(sys.argv) > 1:
    DIRECTORY = sys.argv[1]  # If the user gives you a directory, use it

# get index file
logging.info("Downloading index")
index = wget.download("https://ftp.ncbi.nlm.nih.gov/pub/pmc/manuscript/filelist.csv", 'index.csv')
print()  # puts a space between progress bar and next log

# get papers from PubMed
for x in range(1, 7):
    fileName = 'PMC' + f"{x:03}" + 'XXXXXX.txt.tar.gz'  # All the zipped files are in this format
    logging.info("Downloading %s", fileName)
    wget.download("https://ftp.ncbi.nlm.nih.gov/pub/pmc/manuscript/" + fileName, fileName)
    logging.info("Extracting %s", fileName)
    tar = tarfile.open(fileName, "r:gz")
    tar.extractall(DIRECTORY)
    os.remove(fileName)
    for folder in os.listdir(DIRECTORY):  # removes papers from folders,puts in directory
        if folder.startswith('PMC') and not folder.endswith('txt'):
            for file in os.listdir(DIRECTORY + "/" + folder):
                if os.path.exists(DIRECTORY + "/" + file):
                    os.remove(DIRECTORY + "/" + folder + "/" + file)
                else:
                    shutil.move(DIRECTORY + "/" + folder + "/" + file, DIRECTORY)
            os.rmdir(DIRECTORY + "/" + folder)

# get metadata from PubMed
with open("index.csv", "r") as openedIndexFile:  # run through indexFile
    openedIndexFile.readline()  # get rid of top line
    urls = []
    fileNames = []
    for line in openedIndexFile:
        ID = line[39:47]
        urls.append("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=" + ID)
        fileNames.append(ID + ".json")
        LENGTH = len(urls)
    for x in range(LENGTH):
        if not os.path.exists(DIRECTORY + "/" + fileNames[x]):
            wget.download(urls[x], DIRECTORY + "/" + fileNames[x])
            MESSAGE = "Metadata downloaded: %d/%d, %d%%" % (x, LENGTH, x / LENGTH * 100)
            sys.stdout.write("\r" + MESSAGE)
            sys.stdout.flush()
        else:
            # if the program crashes, it will pick up from where you left off
            MESSAGE = "Finding where you left off..."
            sys.stdout.write("\r" + MESSAGE)
            sys.stdout.flush()
os.remove('index.csv')
