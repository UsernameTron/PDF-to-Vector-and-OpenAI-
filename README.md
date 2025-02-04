
# 📄 PDF to OpenAI Knowledge Base Converter

🚀 **A streamlined pipeline that extracts text from PDFs, generates OpenAI embeddings, and creates a FAISS index—all in one step.**  
Easily converts PDFs into a structured `.txt` file for **uploading to OpenAI Custom GPT** or other AI applications.  

---

## 🎯 **Features**
✅ **PDF Text Extraction** – Uses `PyMuPDF` to parse and extract readable text.  
✅ **OpenAI Embeddings** – Converts extracted text into a high-dimensional vector representation.  
✅ **FAISS Indexing** – Stores embeddings in FAISS for fast similarity searches.  
✅ **Text Conversion for OpenAI** – Saves extracted text as a `.txt` file for easy upload to OpenAI Custom GPT.  
✅ **User-Friendly Web Interface** – Uses `Streamlit` to allow **drag-and-drop PDF uploads & downloads**.  

---

## 🚀 **Installation**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/pdf-to-openai
cd pdf-to-openai
```

### 2️⃣ **Set Up a Virtual Environment (Recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 📄 **Usage**
### 🖥️ **Run in Streamlit (Web UI)**
```bash
streamlit run pdf_to_openai.py
```
- **Upload a PDF file**  
- The script will **process the file automatically**  
- **Download** the OpenAI `.txt` file and FAISS index  

### 🖥️ **Run from Command Line (CLI)**
```bash
python pdf_to_openai.py myfile.pdf
```
*(Modify the script to accept `sys.argv` input for CLI-only use.)*  

---

## 📂 **Project Structure**
```
📦 pdf-to-openai
 ┣ 📜 pdf_to_openai.py          # Main script
 ┣ 📜 requirements.txt          # Dependencies
 ┣ 📜 README.md                 # Documentation
 ┗ 📂 data                      # Folder for storing processed files
```

---

## 🔥 **How It Works**
1️⃣ **Extracts text from a PDF** using `PyMuPDF`  
2️⃣ **Generates OpenAI embeddings** using `text-embedding-ada-002`  
3️⃣ **Creates a FAISS index** for vector-based searching  
4️⃣ **Saves extracted text** as `openai_knowledge_base.txt`  
5️⃣ **Allows downloading results** for OpenAI Custom GPT upload  

---

## 🎯 **Example Output**
After running the script, you’ll get:  
✅ **`vector_index.faiss`** – FAISS-stored vector embeddings  
✅ **`openai_knowledge_base.txt`** – Clean text file for OpenAI upload  

---

## 🛠️ **Requirements**
- Python 3.8+
- OpenAI API Key (store securely in `.env` or environment variables)
- Dependencies in `requirements.txt`

---

## 📢 **Contributing**
Feel free to fork, submit issues, or contribute! PRs are welcome.  

---

## 📜 **License**
This project is open-source and available under the **MIT License**.  

