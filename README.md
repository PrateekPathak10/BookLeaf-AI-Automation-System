# BookLeaf AI Automation System

AI-powered multi-channel customer support automation system built for BookLeaf Publishing.

This project automates repetitive author support queries related to:
- Publishing timelines
- Royalty status
- Dashboard access
- Book live status
- Add-on services
- Author copy tracking

The system uses:
- Open-source LLMs
- RAG (Retrieval-Augmented Generation)
- Supabase/PostgreSQL
- FastAPI
- Streamlit
- n8n automation workflows

---

# Problem Statement

BookLeaf receives hundreds of repetitive author queries daily across:
- Email
- WhatsApp
- Instagram DMs
- Dashboard support

Handling these manually:
- Increases support workload
- Delays response time
- Reduces operational efficiency

This project automates these workflows using scalable AI systems.

---

# Features

## AI Query Understanding

The system classifies user queries into:
- Royalty queries
- Book live status
- Dashboard access
- Add-on status
- Author copy tracking
- General publishing questions

---

## RAG Knowledge Base

The system uses the FAQ knowledge base document provided by BookLeaf Publishing.

The Google Docs knowledge base was converted into PDF format and indexed using:
- LangChain
- Nomic Embeddings
- FAISS Vector Database

This allows semantic retrieval for publishing-related author queries.

---

## Supabase Integration

Stores and retrieves:
- Author details
- Book status
- Royalty information
- Add-on services

---

## Human Escalation

If confidence score is below 80%, the query is escalated automatically.

---

## Identity Unification

Matches author identities across:
- Email
- Phone
- Instagram
- Dashboard names

using:
- Fuzzy matching
- Confidence scoring

---

## Logging System

All interactions are logged with:
- Query
- Response
- Confidence
- Escalation status

---

# Tech Stack

| Component | Technology |
|---|---|
| Backend | FastAPI |
| Frontend | Streamlit |
| Database | Supabase |
| LLM | Llama 3 |
| Embeddings | Nomic Embed |
| Vector DB | FAISS |
| Automation | n8n |
| Identity Matching | RapidFuzz |
| RAG | LangChain |

---

# Folder Structure

```text
bookleaf-ai-bot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── rag.py
│   ├── logger.py
│   ├── identity_match.py
│   ├── prompts.py
│   └── utils.py
│
├── data/
│   ├── mocked_data.csv
│   └── knowledge_base.pdf
│
├── faiss_index/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

# Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPO
cd bookleaf-ai-bot
```

---

# Create Virtual Environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

# Pull Models

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

---

# Run Ollama

```bash
ollama serve
```

---

# Run Backend

```bash
uvicorn app.main:app --reload
```

---

# Run Frontend

```bash
streamlit run app.py
```

---

# API Endpoint

## POST /query

### Request

```json
{
  "query": "when will i get royalty",
  "email": "rahul@gmail.com"
}
```

---

### Response

```json
{
  "response": "Your royalty status is Paid",
  "confidence": 92,
  "escalated": false
}
```

---

# Planned n8n Workflow Architecture

For workflow orchestration, I designed a planned n8n automation architecture to support scalable multi-channel support operations.

The workflow is designed to:
- Receive incoming user queries
- Forward requests to the FastAPI backend
- Check confidence scores
- Trigger escalation workflows
- Store interaction logs

---

# Planned Workflow

```text
Webhook Trigger
      ↓
Receive User Query
      ↓
HTTP Request → FastAPI Backend
      ↓
Confidence Evaluation
      ↓
IF confidence < 80
      ↓
Slack/Gmail Escalation
      ↓
Store Logs
```

---

# Planned n8n Nodes

| Node | Purpose |
|---|---|
| Webhook | Receive incoming user queries |
| HTTP Request | Call FastAPI backend |
| IF Node | Check confidence threshold |
| Slack/Gmail | Human escalation |
| Google Sheets/CSV | Logging |

---

# Why n8n?

I selected n8n because:
- Open-source workflow orchestration
- Easy API integrations
- Better flexibility compared to Zapier
- Self-hosting support
- AI workflow compatibility

The architecture is designed for future scalability across:
- WhatsApp
- Email
- Instagram
- Dashboard support systems
# RAG Workflow

```text
Google Docs FAQ
        ↓
PDF Conversion
        ↓
Chunking
        ↓
Embeddings
        ↓
FAISS Vector Store
        ↓
Semantic Retrieval
        ↓
Llama3 Response Generation
```

---

# Identity Matching Logic

The system matches users across platforms using:
- Exact email matching
- Phone matching
- Fuzzy name matching
- Instagram similarity

---

# Example Queries

## Query

```text
Is my book live yet?
```

### Response

```text
Your book 'Whispers of Rain' will go live on 2026-05-20
```

---

## Query

```text
Where is my author copy?
```

### Response

```text
Author copy status: Dispatched
```

---

# Error Handling

Implemented:
- DB failure handling
- No match handling
- Multiple match handling
- Low confidence escalation

---

# Future Improvements

- Voice AI support
- Multi-language support
- Fine-tuned publishing model
- Sentiment analysis
- Advanced analytics dashboard

---

# Self Rating

| Skill | Rating |
|---|---|
| n8n / Automation | 8/10 |
| LangChain / LLMs | 9/10 |
| System Design | 8.5/10 |

---

# Author

Prateek Pathak

---

# Screenshots
![Response][screenshots/ss1.png]
