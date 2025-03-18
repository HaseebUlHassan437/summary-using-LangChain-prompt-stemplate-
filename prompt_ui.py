# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_core.prompts import PromptTemplate,load_prompt

# load_dotenv()
# model = ChatOpenAI()

# st.header('Reasearch Tool')

# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# template = load_prompt('template.json')



# if st.button('Summarize'):
#     chain = template | model
#     result = chain.invoke({
#         'paper_input':paper_input,
#         'style_input':style_input,
#         'length_input':length_input
#     })
#     st.write(result.content)




# # from langchain_google_genai import ChatGoogleGenerativeAI
# # from dotenv import load_dotenv

# # load_dotenv()

# # model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# # result = model.invoke('most popular political Leader of Pakistan')

# # print(result.content)


from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
import os

# Load environment variables from .env
load_dotenv()

# Initialize the Gemini model; this will use the credentials provided via GOOGLE_APPLICATION_CREDENTIALS
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

st.header('Research Tool (Gemini)')

# Select inputs for the research paper, explanation style, and length
paper_input = st.selectbox(
    "Select Research Paper Name", 
    ["Attention Is All You Need", 
     "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", 
     "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Load your prompt template from a JSON file (ensure the template file exists and is correct)
template = load_prompt('template.json')

if st.button('Summarize'):
    # Create a chain that pipes the template into the Gemini model
    chain = template | model
    # Invoke the chain with your inputs
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result.content)
