import os

import requests
import streamlit as st


BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000",
)

st.set_page_config(
    page_title="YouTube Chatbot",
    page_icon="",
    layout="centered",
)


st.title("🤖 YOUTUBE CHATBOT")

st.caption(
    "Chat with any YouTube video here"
)


if "session_id" not in st.session_state:

    st.session_state.session_id = None


if "messages" not in st.session_state:

    st.session_state.messages = []


if "topics" not in st.session_state:

    st.session_state.topics = []

############ Process the video ##############################

st.subheader(
    "🎬 Process YouTube Video"
)


col1, col2 = st.columns(
    [5, 1],
    vertical_alignment="bottom",
)


with col1:

    youtube_url = st.text_input(
        "YouTube URL",
        placeholder=(
            "Paste YouTube video link..."
        ),
        label_visibility="collapsed",
        icon="🔗",
    )


with col2:

    process_video = st.button(
        "Process",
        use_container_width=True,
    )

####################### Process Video Request ###############################

if process_video:

    if not youtube_url:

        st.warning(
            "Please paste a YouTube URL first."
        )

    else:

        with st.spinner(
            "Processing video..."
        ):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/process-video",
                    json={
                        "url": youtube_url
                    },
                    timeout=300,
                )

                response.raise_for_status()

                data = response.json()

                # Save session ID
                st.session_state.session_id = (
                    data["session_id"]
                )

                st.session_state.messages = []

                st.session_state.topics = (
                    data.get("topics", [])
                )

                st.success(
                    "Video processed successfully!"
                )

            except requests.RequestException as exc:

                st.error(
                    f"Could not process video: {exc}"
                )
                if exc.response is not None:

                    try:

                        error_data = (
                            exc.response.json()
                        )

                        st.error(
                            "Backend error: "
                            f"{error_data.get('detail', error_data)}"
                        )

                    except ValueError:

                        st.error(
                            "Backend response: "
                            f"{exc.response.text}"
                        )


################# Topics Discussed ####################################


if st.session_state.topics:

    st.divider()

    st.subheader(
        "📚 Topics Discussed"
    )

    st.caption(
        "The following topics are discussed in this video."
    )

    for index, topic in enumerate(
        st.session_state.topics[:8],
        start=1,
    ):

        st.markdown(
            f"**{index}. {topic}**"
        )


######################### Chat Section ##############

st.divider()

st.subheader(
    "Ask Something About The Video"
)

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

################### Chat Input #################

question = st.chat_input(
    "➤ Ask something about the video..."
)


############################## Chat Request ##############

if question:

    if st.session_state.session_id is None:

        st.warning(
            "Please process a YouTube video first."
        )

    else:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )
        with st.chat_message("user"):

            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner(
                "Thinking..."
            ):

                try:

                    response = requests.post(
                        f"{BACKEND_URL}/chat",
                        json={
                            "session_id": (
                                st.session_state.session_id
                            ),
                            "question": question,
                        },
                        timeout=120,
                    )

                    response.raise_for_status()

                    data = response.json()

                    answer = data["answer"]

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                        }
                    )

                except requests.RequestException as exc:

                    st.error(
                        f"Chat request failed: {exc}"
                    )

                    if exc.response is not None:

                        try:

                            error_data = (
                                exc.response.json()
                            )

                            st.error(
                                "Backend error: "
                                f"{error_data.get('detail', error_data)}"
                            )

                        except ValueError:

                            st.error(
                                "Backend response: "
                                f"{exc.response.text}"
                            )
