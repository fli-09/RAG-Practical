from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.text_splitter import TokenTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import LLMChain
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from src.prompt import *



def file_processing(file_path):
    
#file_path = "D:\Gen ai\Langchain\Langchain Projects\Data\my.pdf"
  loader =PyPDFLoader(file_path)
  data = loader.load()

  question_gen = ""
  for page in data:
    question_gen += page.page_content

    from langchain.text_splitter import TokenTextSplitter
  splitter_ques  = TokenTextSplitter(
    model_name= "gpt-3.5-turbo",
    chunk_size = 1000,
    chunk_overlap = 200
)
  chunk_ques_gen = splitter_ques.split_text(question_gen)


  doc_ques = [Document(page_content = t ) for t in chunk_ques_gen]

  return question_gen,doc_ques





def llm_pipeline(file_path):
    """
    Processes a document and extracts questions only (no answers).
    """
    # 1. Process the file to get chunks and combined text
    question_gen, doc_ques = file_processing(file_path)

    # Load environment variables
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")

    # Set up Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=google_api_key,
        temperature=0.2
    )

    # 3. Create and run a chain to generate questions from the full text
    prompt_ques = PromptTemplate(
        template=prompt_generate_questions,
        input_variables=['text']
    )
    question_chain = LLMChain(llm=llm, prompt=prompt_ques)
    result = question_chain.invoke({"text": question_gen})
    output_text = result.get("text", "")
    
    # Clean the generated questions into a list
    ques_list = [q.strip() for q in output_text.split("\n") if q.strip()]

    return ques_list


def summarize_docx(file_path):
    """Summarize a .docx file using a summarization chain."""
    loader = UnstructuredWordDocumentLoader(file_path)
    docs = loader.load()
    llm = ChatGoogleGenerativeAI( 
        model="gemini-pro",
        google_api_key=google_api_key,
        temperature=0.2
    )
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)
    return summary
