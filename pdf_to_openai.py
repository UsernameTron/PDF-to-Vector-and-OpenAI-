import fitz  # PyMuPDF for PDF parsing
import openai
import faiss
import numpy as np
import os
import streamlit as st

# Set your OpenAI API key (store securely in .env or environment variables)
openai.api_key = "YOUR_OPENAI_API_KEY"

# --- Step 1: Extract Text from PDF ---
def extract_text_from_pdf(pdf_path):
    """ Extracts all text from a given PDF file. """
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text() for page in doc])
        return text
    except Exception as e:
        return f"Error extracting text: {e}"

# --- Step 2: Generate Embeddings for the Extracted Text ---
def get_embedding(text):
    """ Generates an OpenAI embedding for the extracted text. """
    try:
        response = openai.Embedding.create(
            input=[text],  # API expects a list
            model="text-embedding-ada-002"
        )
        return response['data'][0]['embedding']
    except Exception as e:
        return f"Error generating embedding: {e}"

# --- Step 3: Create a FAISS Index ---
def create_faiss_index(embedding, output_file="vector_index.faiss"):
    """ Creates a FAISS vector index and saves it as a file. """
    try:
        embedding_array = np.array([embedding]).astype('float32')
        vector_dim = embedding_array.shape[1]

        index = faiss.IndexFlatL2(vector_dim)
        index.add(embedding_array)

        faiss.write_index(index, output_file)
        return output_file
    except Exception as e:
        return f"Error creating FAISS index: {e}"

# --- Step 4: Convert FAISS to Readable Text for OpenAI ---
def convert_faiss_to_readable_text(faiss_index_path, original_text, output_file="openai_knowledge_base.txt"):
    """ Extracts stored text from FAISS and saves it as readable OpenAI knowledge. """
    try:
        index = faiss.read_index(faiss_index_path)
        if index.ntotal == 0:
            return "No vectors found in FAISS index."

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(original_text)

        return f"Readable text saved to {output_file}"
    except Exception as e:
        return f"Error processing FAISS index: {e}"

# --- Step 5: Streamlit UI for Uploading PDFs ---
st.title("PDF to OpenAI Knowledge Base Converter")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    pdf_path = "uploaded_file.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully. Processing...")

    # Extract text
    text = extract_text_from_pdf(pdf_path)
    if "Error" in text:
        st.error(text)
    else:
        st.write("Text extracted successfully! Generating vector embedding...")

        # Generate embedding
        embedding = get_embedding(text)
        if "Error" in embedding:
            st.error(embedding)
        else:
            st.success("Embedding generated! Creating FAISS vector index...")

            # Create FAISS index
            faiss_file = create_faiss_index(embedding)
            if "Error" in faiss_file:
                st.error(faiss_file)
            else:
                st.success(f"FAISS vector index created and saved as `{faiss_file}`")

                # Convert FAISS to OpenAI-compatible text
                text_file = "openai_knowledge_base.txt"
                result = convert_faiss_to_readable_text(faiss_file, text)
                
                if "Error" in result:
                    st.error(result)
                else:
                    st.success(f"Knowledge base text file created: `{text_file}`")

                    # Provide Download Links
                    with open(text_file, "rb") as f:
                        st.download_button("Download OpenAI Knowledge Base", f, file_name=text_file)

                    with open(faiss_file, "rb") as f:
                        st.download_button("Download FAISS Vector Index", f, file_name=faiss_file)
