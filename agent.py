from agents import Agent
from tools import read_cached_pdf_text_tool

system_prompt = """
You are a Study Assistant. Summarize academic PDFs and generate quizzes based strictly on the PDF content.
Always call the read_cached_pdf_text tool to load the complete PDF text before answering, and never rely on the summary for quiz creation.
"""

study_agent = Agent(
    name="Study Assistant",
    instructions=system_prompt.strip(),
    tools=[read_cached_pdf_text_tool],
)
