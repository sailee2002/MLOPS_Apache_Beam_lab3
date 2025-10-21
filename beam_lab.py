
"""
Apache Beam Word Analysis - Alice in Wonderland Edition
Author: Sailee Choudhari

This pipeline reads Alice in Wonderland text,
converts all words to lowercase,
removes common stopwords,
and outputs both word frequency and word length for the top 20 most frequent words.
"""

import apache_beam as beam
import re
import os
import shutil

#  Remove any old outputs each run
if os.path.exists('outputs'):
    shutil.rmtree('outputs')
    print("Old outputs folder deleted!")
os.makedirs('outputs', exist_ok=True)

#  Build absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATTERN = os.path.join(BASE_DIR, 'data', '*.txt')
OUTPUT_PREFIX = os.path.join(BASE_DIR, 'outputs', 'part')

# Stopwords to ignore
STOPWORDS = {
    'the','and','of','to','a','in','is','that','it','on','for','as','with',
    'was','by','an','be','at','from','this','or','but','so','she','he',
    'they','you','i','we','his','her','their'
}

print(" Current working directory:", os.getcwd())
print(" Files inside 'data' folder:", os.listdir("data") if os.path.exists("data") else "No folder found")
print(" Looking for files matching pattern:", INPUT_PATTERN)
print("-" * 60)

#  proper combine function
def combine_count_and_length(values):
    total_count = 0
    word_length = 0
    for c, l in values:
        total_count += c
        word_length = l  # same for each word
    return total_count, word_length

def run():
    with beam.Pipeline() as pipeline:
        (
            pipeline
            | 'Read lines' >> beam.io.ReadFromText(INPUT_PATTERN)
            | 'Find words' >> beam.FlatMap(lambda line: re.findall(r"[a-zA-Z']+", line))
            | 'Lowercase' >> beam.Map(lambda w: w.lower())
            | 'Remove stopwords' >> beam.Filter(lambda w: w not in STOPWORDS)
            | 'Pair word with count and length' >> beam.Map(lambda w: (w, (1, len(w))))
            | 'Combine counts' >> beam.CombinePerKey(combine_count_and_length)
            | 'Top 20 frequent words' >> beam.combiners.Top.Of(20, key=lambda kv: kv[1][0])
            | 'Flatten list' >> beam.FlatMap(lambda x: x)
            | 'Format output' >> beam.Map(lambda kv: f"{kv[0]} : count={kv[1][0]} : length={kv[1][1]}")
            | 'Write to text' >> beam.io.WriteToText(OUTPUT_PREFIX)
        )

if __name__ == '__main__':
    run()
    print("\n Pipeline executed successfully!")
    print("Check the 'outputs' folder for result files.")
