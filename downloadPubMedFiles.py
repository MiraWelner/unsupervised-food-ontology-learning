import os
import shutil
import sys
import tarfile
import logging
import requests

url = "https://ftp.ncbi.nlm.nih.gov/pub/pmc/manuscript/"  # Location of the files of PubMed

directory = '.'  # current directory is the default
if len(sys.argv) > 1:
    directory = sys.argv[1]  # If the user gives you a directory, use it
# get index file
indexFile = requests.get("https://ftp.ncbi.nlm.nih.gov/pub/pmc/manuscript/filelist.csv")
open('indexFile.csv', 'wb').write(indexFile.content)
# get metadata from PubMed
with open("indexFile.csv", "r") as openedIndexFile:  # run through indexFile
    openedIndexFile.readline()  # get rid of top line
    for line in openedIndexFile:
        metadata = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=" + line[39:47])
        open(directory + "/" + line[39:47] + '.json', 'wb').write(metadata.content)
        logging.info("Downloaded metadata " + line[39:47])
# get papers from PubMed
x = 1
while True:
    fileName = 'PMC' + f"{x:03}" + 'XXXXXX.txt.tar.gz'  # All the zipped files are in this format
    logging.info("Attempting to download " + fileName)
    zipFile = requests.get(url + fileName)
    if zipFile.status_code != 200:  # If the zipfile doesn't exist, you've reached the end of the PubMed repo
        break
    open(fileName, 'wb').write(zipFile.content)  # Writes to zipfile
    logging.info("Extracting " + fileName)
    tar = tarfile.open(fileName, "r:gz")
    tar.extractall(directory)
    logging.info("Extracted " + fileName)
    os.remove(fileName)
    for folder in os.listdir(directory):  # removes papers from folders,puts in directory
        if folder.startswith('PMC') and not folder.endswith('txt'):
            for file in os.listdir(directory + "/" + folder):
                shutil.move(directory + "/" + folder + "/" + file, directory)
            os.rmdir(directory + "/" + folder)
    logging.info("Removed contents of " + fileName + " from individual folders")
    x += 1
