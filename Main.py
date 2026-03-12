from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import re

# Create FastAPI app
app = FastAPI()

# Enable CORS (allows HTML page to call the API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load inverted index
with open("inverted_index.json", "r") as f:
    inverted_index = json.load(f)

# Load IDF values
with open("idf.json", "r") as f:
    idf = json.load(f)

# Tokenize query
def tokenize(query):
    query = query.lower()
    query = re.sub(r"[^\w\s]", "", query)
    tokens = query.split()
    return tokens

# Search function
def search(query):

    tokens = tokenize(query)

    scores = {}

    for word in tokens:

        if word in inverted_index:

            for doc, tf in inverted_index[word]:

                score = tf * idf[word]

                if doc in scores:
                    scores[doc] += score
                else:
                    scores[doc] = score

    ranked_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return ranked_results

# FastAPI search endpoint
@app.get("/search")
def search_api(q: str):

    results = search(q)

    return {
        "query": q,
        "results": results
    }