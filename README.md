# Framework for collection of domain-specific scientific literature and unsupervised learning of word embeddings.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

In addition to Python 3.6+, following Python libraries are required.

```
requests==2.23.0
```

You can optionally use pip3 to install the required Python libraries.

```
pip3 install -r requirements.txt
```

### Running

Navigate to the repository. The following line downloads all files from PubMed along with their metadata:

```
python3 downloadPubMedFiles.py
```

If you want the files to be stored in a directory other than the one that downloadPubMedFiles.py is stored in, type
```
python3 downloadPubMedFiles.py [path to directory]
```
### Results
The output of this code is many folders containing txt files of all the papers stored on pubmed along with their metadata

## Authors
* **Mira Welner** 
* **Jason Youn**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
This code was written in Professor Tagkopoulos's lab at UC Davis
