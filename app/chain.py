from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from app.memory import format_history
from app.prompt import (
    get_rag_prompt,
    get_topic_prompt,
)


def get_llm():

    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
    )


def create_chain():

    prompt = get_rag_prompt()

    llm = get_llm()

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    return chain


def answer_question(
    retriever,
    history: list,
    question: str,
):

    documents = retriever.invoke(
        question
    )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    chain = create_chain()

    response = chain.invoke(
        {
            "history": format_history(history),
            "context": context,
            "question": question,
        }
    )

    return response


def extract_topics(transcript):

    prompt = get_topic_prompt()

    llm = get_llm()

    chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    response = chain.invoke(
        {
            "transcript": transcript
        }
    )

    topics = [
        topic.strip()
        for topic in response.splitlines()
        if topic.strip()
    ]

    return topics[:8]