from typing import List
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import streamlit as st
import openai


st.sidebar.title("Model Selection")
model_choice = st.sidebar.selectbox(
    "Select a model:", 
    ("GPT-4o-mini", "Gemini-1.5-Flash")  
)


if model_choice == "GPT-4o-mini":
    f = open("key.txt")
    KEY = f.read()
    model = ChatOpenAI(api_key=KEY,
                   model="gpt-4o-mini",
                   temperature=0)
    
elif model_choice == "Gemini-1.5-Flash":
    f = open(".google_secretkey.txt")
    KEY = f.read()
    model = GoogleGenerativeAI(google_api_key=KEY,
                   model="gemini-1.5-flash",
                   temperature=0) 


class CodeReviwer(BaseModel):
    header: str = Field(description="Display the text '## Code Reviewer' as a level 2 heading (H2 tag).")
    sub_header_1: str = Field(description="Display the text '### Bug Report' as a level 3 heading (H3 tag).")
    bugs: str = Field(description="Provide an introduction stating: 'The bugs in the following code are:'.")
    review: List[str] = Field(description="Analyze the provided code snippet for potential errors, vulnerabilities, or inefficiencies. Identify and list all anticipated issues directly in a comma-separated format, omitting any subheadings or introductory statements.")
    sub_header_2: str = Field(description="Display the text '### Fixed Code' as a level 3 heading (H3 tag).")
    code: str = Field(description="Provide the optimized version of the code after analysis without any comments in it. Ensure the code is wrapped in triple backticks (```) to format it as a code block.")
    
parser = PydanticOutputParser(pydantic_object=CodeReviwer)

prompt = PromptTemplate(
    
    template = "Assume the role of a meticulous Code Reviewer. Your task is to answer the user's query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

chain = prompt | model | parser


st.title("֎ An AI Code Reviewer")

prompt = st.text_area("Enter your Python code here...")

if st.button("Generate"):
    response = chain.invoke({"query": prompt})
    st.write(response.header)
    st.write(response.sub_header_1)
    # st.write(response.bugs, *[f"{i+1}. {review}" for i, review in enumerate(response.review)])
    st.write(response.bugs)
    for i in range(len(response.review)):
        st.write(f"{i+1}. {response.review[i]}")
    st.write(response.sub_header_2)
    st.write(response.code)
    
    