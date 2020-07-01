# Framework for collection of domain-specific scientific literature and unsupervised learning of word embeddings.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
In addition to Python 3.6+, following Python library is required.
```
wget==3.2
```
You can optionally use pip3 to install the required Python library.
```
pip3 install -r requirements.txt
```
### Running
Navigate to the repository. The following line downloads all files from PubMed along with their metadata:
```
python3 downloadPubMedFiles.py [path to directory]
```
If you enter no command line arguments, it will default to current directory. This program may take some time (>24 hours)
to run. If something happens such as a wifi error that stops your download in the middle, run it again. You will have
to to through the text downloads again at normal speed, but the metadata downloads which are what take a long time should pick up where you left off.

If you want to search for keywords, edit the ```searchWordFile.txt``` so that it contains the search terms separated by 
line breaks. Multi-word search terms are fine. Then type:
```
python3 searchForKeyWords.py [path to directory]
```
If you enter no command line arguments, it will default to the current directory.

### Results
Running ```downloadPubMedFiles.py``` will give you txt files of all the papers stored on PubMed in the form of .txt 
files as well as their metadata in the form of .json files. The metadata will be labeled after the PMID while the 
papers will be labeled after PMCID.\
Running ```searchForKeyWords.py``` will output the names of filenames of the papers which have metadata containing that
keyword, along with the specific keyword (in case there are multiple keywords)

## Authors
* **Mira Welner** 
* **Jason Youn**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
This code was written in Professor Tagkopoulos's lab at UC Davis
