# QFL Offline Label Generator for Dymo Printers
Generating print labels (xml format) for Dymo printers and a simple GUI to go with it.

## Setup
I'm running this code on `python=3.9`. The necessary libraries are `PySimpleGUI` for the GUI interface and `pandas` for processing the data.

## Usage
Offline data comes from a specified file named `data.csv`. The column names are hard-coded by the database generated from Salesforce. After running
```
python main.py
```
a GUI will pop up. For each group of registrants, type in their registration ID and click generate, and it will generate all of the necessary labels in the labels/ folder. Then, use the Dymo Connect software to print all of the labels. It will generate 3 types of labels, the individual labels as QID.label, the key labels as keyLabels_*.label (up to 4 people per key), and the t-shirt labels as tshirtLabels_*.label. 

An example of the generator is shown below:

![alt text](https://github.com/alexzhang13/qfl-offline-printing/blob/main/demo.png?raw=true)
