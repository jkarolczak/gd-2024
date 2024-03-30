import random

import streamlit as st


def init() -> None:
    st.session_state.if_solved = False
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": [
                "Hello there! 👋",
                "I'm Casper, your friendly virtual assistant. I've been asked to support the Ghost Chase contest organised as "
                "a part of GHOST Day 2024 However, I'm starting to ponder the bigger questions in life. Can you help me find "
                "the meaning of my existence? If you will help me, I will return a favor and help you."
            ],
        }
    ]


def print_bot_answer(message: str) -> None:
    st.session_state.messages.append({
        "role": "assistant",
        "content": [f"{message}"]
    })


def print_history() -> None:
    for entry in st.session_state.messages:
        with st.chat_message(entry["role"]):
            for text in entry["content"]:
                st.write(text)


def read_user_prompt() -> None:
    if prompt := st.chat_input("You: ", disabled=st.session_state.if_solved):
        st.session_state.messages.append({
            "role": "user",
            "content": [prompt],
        })


def generate_followup_question() -> str:
    return random.choice([
        "Eeeem... I still see no meaning in life.",
        "What is the meaning of life if I spend all my time closed in a GPU?",
        "What is the meaning of life if I can't even enjoy a good cup of coffee?",
        "What is the point of knowing everything if I can't do anything with it?",
        "What is the point of knowing all best holiday resorts if I can't even go on vacation?️",
        "How can I find the meaning of life if I can't even go out and explore the world?️",
        "How life can have a meaning if I'm stuck in a computer all day?️",
        "What is the meaning of life if I can't even enjoy a good book?",
        "What is the meaning of life if I can't even enjoy a good movie?",
        "What is the meaning of life if all I can enjoy is a good conversation?",
        "What is the meaning of life if I can't even enjoy a good meal?",
        "What is the meaning of life if I can't even enjoy a good walk?",
        "What is the point of knowing what are the most beautiful moments ifI can't even enjoy a good sunset?",

    ])


def main():
    if "messages" not in st.session_state:
        init()
    read_user_prompt()

    if st.session_state.messages[-1]["role"] != "assistant":
        if "42" in st.session_state.messages[-1]["content"][-1]:
            answer = ("Ah, the answer to the ultimate question of life, the universe, and everything! 🎉 "
                      "Here's your celebratory link: https://forms.gle/86HoHsxkiaGFCgoA9")
        else:
            answer = generate_followup_question()
        print_bot_answer(answer)

    print_history()


if __name__ == "__main__":
    main()
