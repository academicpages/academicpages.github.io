# Import necessary packages
import ollama  # Enables interaction with local large language models (LLMs)
import gradio as gr  # Provides an easy-to-use web interface for the chatbot

# Document processing and retrieval  
from langchain_community.document_loaders import PyMuPDFLoader  # Extracts text from PDF files for processing
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Splits text into smaller chunks for better embedding and retrieval
from langchain.vectorstores import Chroma  # Handles storage and retrieval of vector embeddings using ChromaDB

# Embedding generation  
from langchain_community.embeddings import OllamaEmbeddings  # Converts text into numerical vectors using Ollama's embedding model

import re  # Provides tools for working with regular expressions, useful for text cleaning and pattern matching

# Define the function that processes the PDF
def process_pdf(pdf_bytes):
    # If PDF files are empty, return None — This prevents errors from trying to process an empty input.
    if pdf_bytes is None:
        return None, None, None
    # PyMuPDFLoader initializes the PDF file
    loader = PyMuPDFLoader(pdf_bytes) 
    # .load() method reads the content of the PDF and extracts its text
    data = loader.load()
    # RecursiveCharacterTextSplitter splits the PDF into chunks of 500 characters, keeping 100 characters overlap to keep context 
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    # Splits the documents into chunks and stores them in chunks object
    chunks = text_splitter.split_documents(data)
    # Create embeddings using OllamaEmbeddings 
    embeddings = OllamaEmbeddings(model="deepseek-r1:8b")
    # Create a vector database which allows us to store the chunks and their embeddings
    vectorstore=Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="./chroma_db")  # Example directory
    # This creates a retriever that enables searching through the vectorstore.
    retriever = vectorstore.as_retriever()
    """
    The function returns 3 objects
        text_splitter → (Used to split new text in the same way as before)
        vectorstore → (Holds the processed document chunks)
        retriever → (Used to fetch relevant document chunks when answering questions)
    """
    
    return text_splitter, vectorstore, retriever

def ollama_llm(question, context):

    # Format the prompt with the question and context to provide structured input for the AI
    formatted_prompt = f"Question: {question}\n\nContext: {context}"
    # Send the structured prompt to the Ollama model for processing
    response = ollama.chat(
        model="deepseek-r1:8b",  # Specifies the AI model to use
        messages=[{'role': 'user', 'content': formatted_prompt}]  # Formats the user input
    )
    # Extract the AI-generated response content
    response_content = response['message']['content']
    # Remove content inside <think>...</think> tags to clean up AI reasoning traces
    final_answer = re.sub(r'<think>.*?</think>', # We're searching for think tags
                          '', # We'll replace them with empty spaces
                          response_content, # In response_content
                          flags=re.DOTALL).strip() # (dot) should match newlines (\n) as well.
    # Return the final cleaned response
    return final_answer

def combine_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Define rag_chain function for Retrieval Augmented Generation
def rag_chain(question, text_splitter, vectorstore, retriever):
    """
    This function takes as input:
        - The question we want to ask the model
        - The text_splitter object to split the PDF and read into chunks
        - The vectorstore for retrieving embeddings 
        - The retriever objects which retrieves data from the vectorstore
    """
    retrieved_docs = retriever.invoke(question) # In this step, we will find the part of the document most relevant to the question
    formatted_content = combine_docs(retrieved_docs) # We will then combine the retrieved parts of the document 
    return ollama_llm(question, formatted_content) # Run the model on the question, and the relevant context from the document 

# Put it all together — Create a function that performs the logic expected by the Chatbot  
def ask_question(pdf_bytes, question): 
    text_splitter, vectorstore, retriever = process_pdf(pdf_bytes) # Process the PDF
    if text_splitter is None:
        return None  # No PDF uploaded    
    result = rag_chain(question, text_splitter, vectorstore, retriever) # Return the results with RAG
    return {result}

if __name__ == '__main__':
    # Define a Gradio interface
    interface = gr.Interface(
        fn=ask_question,  # The function that processes user input and generates a response (logic of the app)
        inputs=[
            gr.File(label="Upload PDF (optional)"),  # Optional file upload input for a PDF document
            gr.Textbox(label="Ask a question")  # Text input where the user types their question
        ],
        outputs="text",  # The function returns a text response
        title="Ask questions about your PDF",  # The title displayed on the interface
        description="Use DeepSeek-R1 8B to answer your questions about the uploaded PDF document.",  # Brief description of the interface's functionality
    )

    # Launch the Gradio interface to start the web-based app
    interface.launch()