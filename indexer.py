import os
import json
import math
import string
from collections import defaultdict

# Folder containing documents
docs_folder = "C:/Users/LENOVO T480/Documents/docs"

documents = {}
doc_id = 1

# TASK 1 – LOAD DOCUMENTS

for filename in os.listdir(docs_folder):
    if filename.endswith(".txt"):
        path = os.path.join(docs_folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            documents[f"doc{doc_id}"] = f.read()
            doc_id += 1

total_docs = len(documents)


# TASK 2 + 3 – TEXT CLEANING & TOKENIZATION

tokenized_docs = {}

for doc, text in documents.items():
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    tokenized_docs[doc] = words


# TASK 4 – TERM FREQUENCY

tf = {}

for doc, words in tokenized_docs.items():
    freq = defaultdict(int)
    for w in words:
        freq[w] += 1
    tf[doc] = dict(freq)


# TASK 5 – INVERTED INDEX

inverted_index = defaultdict(list)

for doc, words in tf.items():
    for word, count in words.items():
        inverted_index[word].append((doc, count))


# TASK 6 – SAVE INVERTED INDEX

with open("inverted_index.json", "w") as f:
    json.dump(inverted_index, f, indent=4)


# TASK 7 – COMPUTE IDF
idf = {}

for word, doc_list in inverted_index.items():
    df = len(doc_list)
    idf[word] = round(math.log(total_docs / df), 3)


# TASK 8 – SAVE IDF
with open("idf.json", "w") as f:
    json.dump(idf, f, indent=4)


# TASK 9 – VALIDATION

print("Number of documents indexed:", total_docs)
print("Number of unique terms:", len(inverted_index))

print("\nSample Inverted Index:")
for i, (word, postings) in enumerate(inverted_index.items()):
    print(word, "->", postings)
    if i == 5:
        break

print("\nSample IDF Values:")
for i, (word, value) in enumerate(idf.items()):
    print(word, "->", value)
    if i == 5:
        break