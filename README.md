Project Title
AI Medical Assistant using AWS Bedrock
________________________________________
Description

This project is a document-based medical question-answering system that uses Retrieval-Augmented Generation. Users can upload medical PDFs and ask questions based on their content. The system retrieves relevant information and generates answers using AWS Bedrock.
________________________________________
Features

•	Upload and analyze medical PDF documents

•	Ask questions based on document content

•	Context-aware responses using RAG

•	Integration with AWS Bedrock for embeddings and LLM

•	Fast retrieval using FAISS
________________________________________
Tech Stack

•	Python

•	FastAPI

•	Streamlit

•	AWS Bedrock

•	FAISS
________________________________________
Project Structure

AI_MEDICAL_ASSISTANCE/

│── backend/

│   ├── app/

│   │   ├── config.py

│   │   ├── document_loader.py

│   │   ├── embeddings.py

│   │   ├── llm.py

│   │   ├── main.py

│   │   ├── rag_pipeline.py

│   │   ├── routes.py

│   │   ├── vector_store.py

│   │

│   ├── data/

│   ├── db/

│

│── frontend/

│   ├── app.py

│

│── requirements.txt

│── .env
________________________________________
Prerequisites

•	Python 3.8 or above

•	AWS account with Bedrock access

•	AWS credentials (Access Key and Secret Key)
________________________________________
Installation

pip install -r requirements.txt
________________________________________
Configuration

Create a .env file:

AWS_ACCESS_KEY_ID=your_key

AWS_SECRET_ACCESS_KEY=your_secret

AWS_REGION=your_region

BEDROCK_MODEL_ID=your_model_id

EMBEDDING_MODEL_ID=your_embedding_model
________________________________________
Running the Application

Start Backend

uvicorn app.main:app --reload

Start Frontend

streamlit run frontend/app.py
________________________________________
Usage

1.	Upload a medical PDF document

2.	Wait for indexing to complete

3.	Enter a query

4.	Receive an answer based on document context
________________________________________
How It Works

•	PDF is loaded and converted into text

•	Text is embedded using Bedrock embeddings

•	Stored in FAISS vector database

•	Query retrieves relevant chunks

•	LLM generates response from context
If you want next step, I can combine all your projects into a single strong portfolio document or resume section, which will help you explain everything clearly in interviews.

