# YouTube Chatbot

A YouTube chatbot that allows users to process a YouTube video and ask questions about its content.

The application uses the video's transcript, splits it into chunks, creates a vector store, retrieves relevant information, and uses an LLM to generate answers.

##  Features

* Process YouTube videos using a YouTube URL
* Automatically extract the video transcript
* Split transcript into smaller chunks
* Create embeddings and a vector store
* Retrieve relevant information using semantic search
* Ask questions about the processed video
* Maintain conversation history for each session
* Extract and display the main topics discussed in the video
* FastAPI backend
* Streamlit frontend
* Automated testing with pytest
* GitHub Actions CI pipeline

##  Project Architecture

```text
YouTube Video URL
        │
   Streamlit Frontend
        │
     FastAPI API
        │
        ├── Extract Video ID
        │
        ├── Get Transcript
        │
        ├── Extract Topics
        │
        ├── Split Transcript
        │
        ├── Create Vector Store
        │
        ├── Create Retriever
        │
        └── Create Chat Session
                    │
              User Question
                    │
               Retriever
                    │
                 LLM
                    │
                 Answer
```

##  Project Structure

```text
Youtube-Chatbot/
│
├── app/
│   ├── __init__.py
│   ├── youtube.py
│   ├── splitter.py
│   ├── vectorstores.py
│   ├── retriever.py
│   ├── memory.py
│   └── chain.py
│
├── tests/
│   ├── test_app.py
│   └── test_youtube.py
│
├── backend.py
├── frontend/
│   └── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Requirements

Make sure you have:
* Python 3.10+
* pip
* Git
* An OpenAI API key

## Environment Variables

Create a `.env` file in the root directory of the project.

```env
OPENAI_API_KEY=your_openai_api_key_here
BACKEND_URL=http://localhost:8000
```

Replace:

```text
your_openai_api_key_here
```

with your actual OpenAI API key.

For local development, keep:

```env
BACKEND_URL=http://localhost:8000
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configure `.env`

Create `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
BACKEND_URL=http://localhost:8000
```

## Run the Backend

Start the FastAPI server:

```bash
uvicorn backend:app --reload
```

The backend will run at:

```text
http://localhost:8000
```

FastAPI automatically provides interactive API documentation at:

```text
http://localhost:8000/docs
```

## Run the Frontend

Open another terminal and activate the virtual environment.

Then run:

```bash
streamlit run frontend.py
```

The Streamlit application will open in your browser.

The frontend communicates with the FastAPI backend using:

```env
BACKEND_URL=http://localhost:8000
```

