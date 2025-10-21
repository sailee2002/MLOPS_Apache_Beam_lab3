# MLOPS_Apache_Beam_lab3
# Apache Beam Word Analysis - Alice in Wonderland Edition

## Project Overview
This project is part of an Apache Beam lab exercise demonstrating the use of data pipelines for text processing. The goal is to read a text dataset, extract words, clean and transform them, and compute word frequency statistics using Beam’s parallel processing capabilities.

In the original lab, the provided example used "King Lear" and printed all words with their frequencies. For my version, I customized the pipeline to:
- Use a different dataset — "Alice in Wonderland".
- Perform stopword filtering.
- Count both word frequency and word length.
- Output only the top 20 most frequent words for cleaner insights.
- Automatically clean the output folder before each run.

## Key Features
- Automatic cleanup: Deletes previous output files before each run.
- Flexible input: Reads any `.txt` file placed in the `data/` folder.
- Text normalization: Extracts alphabetic words using regex and converts them to lowercase.
- Stopword removal: Removes common filler words (e.g., "the", "and", "of").
- Word statistics: For each unique word, computes:
  - Count: how many times it appears.
  - Length: number of characters in the word.
- Ranking: Displays the top 20 most frequent words.
- Clean output: Writes results neatly to the `outputs/` folder.

## Folder Structure
Apache_Beam_Labs/
│
├── beam_lab.py                # Main Apache Beam pipeline script
├── README.md                  # Project documentation
│
├── data/                      # Input text files
│   └── alice.txt              # Dataset used for this run
│
└── outputs/                   # Automatically generated output files
    └── part-00000-of-00001

## Setup & Execution

1. Install Dependencies
Create a virtual environment (recommended) and install Apache Beam:

python -m venv venv
venv\Scripts\activate          # On Windows
# or: source venv/bin/activate # On macOS/Linux

pip install apache-beam

2. Add Dataset
Place your desired text file inside the `data/` folder.
For this project, I used "Alice in Wonderland" from Project Gutenberg (https://www.gutenberg.org/ebooks/11).

3. Run the Pipeline
From the project directory:

python beam_lab.py

4. View the Output
Check the generated file inside the `outputs/` folder:

type outputs\part-00000-of-00001*
(On macOS/Linux use `cat` instead of `type`)

## Example Output
alice : count=370 : length=5
queen : count=250 : length=5
rabbit : count=220 : length=6
time : count=180 : length=4
king : count=160 : length=4
hatter : count=120 : length=6
door : count=100 : length=4

## My Modifications Summary
Aspect | Original Professor Code | My Version
-------|--------------------------|------------
Dataset | King Lear | Alice in Wonderland
Output | All words | Top 20 most frequent
Features | Basic count | Stopword removal, word length
Output handling | Manual cleanup | Automated cleanup before run

## Learnings
Through this lab, I learned how to:
- Build a data processing pipeline using Apache Beam.
- Chain multiple transformations like FlatMap, Map, Filter, and CombinePerKey.
- Handle text data efficiently for frequency and pattern analysis.
- Use combiners such as Top.Of() for ranking.

## Author
Sailee Choudhari  
Master’s in Data Analytics Engineering, Northeastern University  
Boston, MA  
"Every dataset tells a story — Beam helps process it efficiently."
