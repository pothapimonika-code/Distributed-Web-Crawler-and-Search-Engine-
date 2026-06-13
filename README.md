Mini Search Engine using Python and FastAPI

![Python](https://img.shields.io/badge/Python-3.x-blue) 
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green) 
![License](https://img.shields.io/badge/License-MIT-yellow)

Project Overview

A Mini Search Engine built with Python and FastAPI that crawls web pages, processes text data, builds an inverted index, and ranks search results using the TF-IDF algorithm. The project is structured across four milestones, each covering a core component of a real-world search engine pipeline.

---

Technologies Used

| Tool / Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API framework |
| HTML | Frontend search interface |
| JSON | Lightweight data storage |
| Uvicorn | ASGI server to run FastAPI |

 Algorithms & Concepts

- TF-IDF (Term Frequency – Inverse Document Frequency) for document ranking
- Inverted Index for efficient document retrieval
- Tokenization and text preprocessing

 Project Structure

```
mini-search-engine/
│
├── docs/
│   ├── doc1.txt
│   ├── doc2.txt
│   ├── doc3.txt
│   ├── doc4.txt
│   └── doc5.txt
│
├── indexer.py
├── main.py
├── index.html
├── inverted_index.json
└── idf.json
```

---

Milestones

## Milestone 1 – Web Crawling
- Crawled sample web pages from a demo website.
- Saved HTML content locally for further processing.

## Milestone 2 – Data Processing
- Extracted visible text from raw HTML pages.
- Removed unnecessary tags, scripts, and formatting.
- Converted cleaned content into plain text documents.

## Milestone 3 – Indexing
- Tokenized text into individual words.
- Computed Term Frequency (TF) per word per document.
- Built an Inverted Index mapping words to their source documents.
- Calculated Inverse Document Frequency (IDF) across the corpus.
- Stored index and IDF values in JSON files for reuse.

## Milestone 4 – Search Engine Implementation
- Implemented query processing and tokenization.
- Retrieved relevant documents using the inverted index.
- Applied TF-IDF scoring to rank documents by relevance.
- Built a FastAPI backend to handle search queries via REST API.
- Developed a simple HTML interface for user-facing search interaction.

---

How to Run the Project

1. Install dependencies**
```bash
pip install fastapi uvicorn
```

2. Start the server**
```bash
python -m uvicorn main:app --reload
```

3. Open the API documentation**
```
http://127.0.0.1:8000/docs
```

4. Open the search interface**

Open `index.html` directly in your browser.

---

 Example Search

Users can search queries such as `life`, `history`, or `science`. 
The system retrieves matching documents and ranks them based on TF-IDF relevance scores.

---
 Future Improvements

- Support for crawling live websites using `requests` and `BeautifulSoup`
- Add pagination to search results
- Improve UI with a modern frontend framework
- Extend to handle larger document collections

---

 Learning Outcomes

- Web crawling and HTML parsing
- Text preprocessing and tokenization
- Inverted index construction
- TF-IDF-based document ranking
- REST API development with FastAPI
- Basic frontend integration for search queries

---

 License

This project is licensed under the MIT License.
---

Author

**Monika P S**
- GitHub: [@monikareddy14](https://github.com/monikareddy14)
- LinkedIn: [linkedin.com/in/monikaaps](https://www.linkedin.com/in/monikaaps)

> Built as part of an Information Retrieval and Search Engine learning project.
```
