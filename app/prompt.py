from langchain_core.prompts import ChatPromptTemplate
def get_rag_prompt():
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are a helpful YouTube video assistant.

                Answer the user's question using the provided
                YouTube transcript context and conversation history.

                Rules:
                1. Use the transcript context as the primary source.
                2. Use conversation history to understand follow-up questions.
                3. If the answer is not present in the transcript,
                clearly say that you don't know based on the video.
                4. Do not invent information.
                5. Give clear and concise answers.
                """,
            ),
            (
                "human",
                """
                Conversation history:
                {history}

                YouTube transcript context:
                {context}

                User question:
                {question}
                """,
            ),
        ]
    )