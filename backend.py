from uuid import uuid4

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.youtube import (
    extract_video_id,
    get_transcript,
)

from app.splitter import (
    split_transcript,
)

from app.vectorstores import (
    create_vectorstore,
)

from app.retriever import (
    get_retriever,
)

from app.memory import (
    create_memory,
    add_message,
)

from app.chain import (
    answer_question,
    extract_topics
)



load_dotenv()

app = FastAPI(
    title="YouTube Chatbot API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



################ Active Sessions create

sessions = {}

class VideoRequest(BaseModel):
    url: str


class ChatRequest(BaseModel):
    session_id: str
    question: str

@app.get("/")
def root():

    return {
        "message": "YouTube Chatbot is running...."
    }

@app.get("/health")
def health():

    return {
        "status": "OK"
    }



################### Process Video #################
@app.post("/process-video")
def process_video(
    request: VideoRequest,
):

    try:

        video_id = extract_video_id(
            request.url
        )

        transcript = get_transcript(
            video_id
        )
        topics = extract_topics(
            transcript
        )
        documents = split_transcript(
            transcript
        )
        vectorstore = create_vectorstore(
            documents,
            video_id,
        )
        retriever = get_retriever(
            vectorstore
        )

        session_id = str(
            uuid4()
        )

        sessions[session_id] = {

            "video_id": video_id,

            "retriever": retriever,

            "history": create_memory(),

            "topics": topics,
        }

        return {

            "session_id": session_id,

            "video_id": video_id,

            "chunks": len(documents),

            "topics": topics,

            "message":
                "Video processed successfully!",
        }

    except Exception as e:

        print(
            f"PROCESS VIDEO ERROR: {e}"
        )

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


########################### Chat ################

@app.post("/chat")
def chat(
    request: ChatRequest,
):

    # Find session
    session = sessions.get(
        request.session_id
    )

    if session is None:

        raise HTTPException(
            status_code=404,
            detail=(
                "Session not found. "
                "Process a video first."
            ),
        )

    try:

        history = session["history"]
        answer = answer_question(

            retriever=session["retriever"],
            history=history,
            question=request.question,
        )

        add_message(
            history,
            "user",
            request.question,
        )

        add_message(
            history,
            "assistant",
            answer,
        )

        return {

            "answer": answer,

            "session_id":
                request.session_id,
        }

    except Exception as e:

        print(
            f"CHAT ERROR: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )