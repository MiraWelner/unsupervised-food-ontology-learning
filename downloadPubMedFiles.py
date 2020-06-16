import requests
import tarfile
import os
import sys

url = "https://ftp.ncbi.nlm.nih.gov/pub/pmc/manuscript/"  # Location of the files of PubMed

directory = '.'  # current directory is the default
if len(sys.argv) > 1:
    directory = sys.argv[1]  # If the user gives you a directory, use it

x = 1
while True:
    fileName = 'PMC' + f"{x:03}" + 'XXXXXX.txt.tar.gz'  # All the zipped files are in this format
    print("Downloading...")
    zipFile = requests.get(url + fileName)
    if zipFile.status_code != 200:  # If the zipfile doesn't exist, you've reached the end of the PubMed repo
        break
    open(fileName, 'wb').write(zipFile.content)  # Writes to zipfile
    print("Extracting...")
    tar = tarfile.open(fileName, "r:gz")
    tar.extractall(directory)
    os.remove(fileName)
    x += 1
