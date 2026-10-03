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



def get_topic_prompt():

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
                You are analyzing a YouTube video transcript.

                Extract the major topics discussed in the video.

                Rules:
                1. Extract 5 to 8 major topics.
                2. Each topic must be short and descriptive.
                3. Return only the topic names.
                4. Put each topic on a separate line.
                5. Do not number the topics.
                6. Do not use bullet points.
                7. Do not invent topics.
                8. Every topic must be based on the transcript.
                9. Avoid duplicate or overlapping topics.
                """,
            ),
            (
                "human",
                """
                YouTube transcript:

                {transcript}
                """,
            ),
        ]
    )