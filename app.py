import os

import streamlit as st
from agents import Runner

from agent import study_agent
from run_config import config
from tools import extract_pdf_text

st.title("Study Notes Summarizer + Quiz Generator")

# PDF Upload Section
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

def run_agent_task(prompt: str) -> str:
    result = Runner.run_sync(
        starting_agent=study_agent,
        input=prompt,
        run_config=config,
    )
    output = result.final_output
    return output if isinstance(output, str) else str(output)


if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text from the PDF and cache it
    st.info("Extracting text from PDF...")
    extracted_text = extract_pdf_text("temp.pdf")
    st.success("Text extracted and cached.")
    st.write(extracted_text)

    # Summarization Button
    if st.button("Summarize PDF"):
        st.info("Summarizing the PDF...")
        summary = run_agent_task("Summarize the extracted PDF text.")
        st.subheader("Summary")
        st.write(summary)

    # Quiz Generator Button
    if st.button("Create Quiz"):
        st.info("Creating a quiz...")
        quiz = run_agent_task(
            "Based strictly on the full PDF text, generate 5–10 quiz questions (MCQs or mixed)."
        )
        st.subheader("Quiz")
        st.write(quiz)

    # Clean up the temporary file
    if os.path.exists("temp.pdf"):
        os.remove("temp.pdf")
