# 🚀 LangChain Mastery

> A comprehensive learning journey through modern LLM orchestration, RAG systems, and agentic workflows

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-Latest-green.svg)](https://langchain.com/)

---

## 📖 About This Repository

This repository chronicles my deep dive into **LangChain**, documenting hands-on exploration of LLMs, Retrieval Augmented Generation (RAG), AI agents, vector databases, and production-ready GenAI architectures.

From fundamental concepts to complex multi-agent systems, each module represents practical implementation and real-world application of cutting-edge AI engineering principles.

---

## 🎯 Learning Objectives Achieved

✅ Built production-ready RAG pipelines from scratch  
✅ Implemented stateful AI agents with custom tool integration  
✅ Mastered LangChain's LCEL (LangChain Expression Language)  
✅ Designed multi-step reasoning workflows using LangGraph  
✅ Integrated vector databases for semantic search  
✅ Worked with multiple LLM providers (Cohere, HuggingFace)  

---

## 🧠 Core Concepts Mastered

### 1️⃣ Large Language Models (LLMs)

- **Model Integration**: Cohere, HuggingFace Transformers
- **Chat Models**: Multi-turn conversations with context management
- **Prompt Engineering**: System prompts, few-shot learning, structured generation
- **Sampling Strategies**: Temperature control, top-p sampling, deterministic outputs

### 2️⃣ Embeddings & Vector Mathematics

- **Embedding Models**: HuggingFace, Cohere embeddings
- **Vector Operations**: Cosine similarity, semantic search algorithms
- **Vector Stores**: FAISS implementation for efficient similarity search
- **Dimensionality**: Understanding embedding spaces and their properties

### 3️⃣ LangChain Fundamentals

**Core Components**:
- **Prompts**: Template engineering, dynamic prompt construction
- **Chains**: Sequential logic, LCEL composition patterns
- **Runnables**: Async execution, streaming, batch processing
- **Output Parsers**: JSON, Pydantic, structured data extraction
- **Document Loaders**: PDF, Web, Directory-based ingestion
- **Text Splitters**: RecursiveCharacterTextSplitter, semantic chunking
- **Vector Stores**: Indexing, persistence, retrieval optimization
- **Retrievers**: Context-aware document retrieval strategies


---

## 🤖 Agent Architectures Implemented

| Agent Type | Description |
|-----------|-------------|
| **ReAct Agents** | Reasoning + Acting pattern for tool-based problem solving |
| **Tool-Calling Agents** | Dynamic function execution based on LLM decisions |
| **Stateful Agents** | LangGraph-powered agents with persistent memory |
| **Conversational Agents** | Multi-turn dialogue with context retention |

**Advanced Features**:
- Action scratchpad for reasoning transparency
- Conversation history tracking
- Self-correction and iterative refinement

---

## 🔍 Retrieval Augmented Generation (RAG)

**Complete RAG Pipeline Implementation**:

```
📄 Document Loading → ✂️ Text Splitting → 🧬 Embedding → 
💾 Vector Storage → 🔎 Retrieval → 🤖 Generation
```

**Advanced Techniques**:
- Query transformation and expansion
- Context compression for token efficiency
- Metadata filtering and hybrid search
- Re-ranking strategies for precision

**Featured Project**: RAG application for Deep Learning Notebook PDF with semantic search and conversational QA

---

## 📂 Repository Structure

```
├── 1.LLMs/                          # LLM fundamentals and API integration
├── 2.ChatModels/                    # Conversational AI implementations
├── 3.EmbeddedModels/                # Embedding generation and vector ops
├── 4.Prompts/                       # Prompt engineering patterns
├── 5.Langchain-Structured-Output/   # Pydantic models and structured data
├── 6.Langchain-Output-Parsers/      # JSON, XML, and custom parsers
├── 7.Langchain-Chain/               # Chain composition and LCEL
├── 8.LangChain-Runnables/           # Async and streaming execution
├── 9.LangChain-Document-Loader/     # Multi-format document ingestion
├── 10.Langchain-Text-Splitters/     # Chunking strategies
├── 11.Vector-Store/                 # FAISS and vector database ops
├── 12.Retrievers/                   # Advanced retrieval patterns
├── 13.project/                      # End-to-end RAG application
├── 14.Tool/                         # Custom tool creation
├── 15.AGENT/                        # Agent architectures and workflows
├── requirements.txt                 # Python dependencies
└── template.json                    # Template structure
```

Each directory contains practical implementations with detailed examples and experimentation.

---

## 🛠️ Technology Stack

### **Core Frameworks**
- **LangChain** - LLM orchestration and application framework

### **LLM Providers**
- Cohere Command Models
- HuggingFace Open-Source Models

### **Vector & Retrieval**
- FAISS (Facebook AI Similarity Search)
- HuggingFace Embeddings
- Cohere Embeddings

### **Document Processing**
- PyPDF for PDF parsing
- WebBaseLoader for web scraping
- DirectoryLoader for batch processing
- tiktoken for tokenization

### **Additional Tools**
- Pydantic for data validation
- Python-dotenv for environment management

---

## 💡 Key Projects & Implementations

### 🎓 Deep Learning Notebook RAG System
A complete RAG application that ingests PDF documentation and enables conversational Q&A with semantic understanding.

**Features**:
- PDF document parsing and preprocessing
- Semantic chunking with overlap
- FAISS vector store for fast retrieval
- Context-aware response generation
- Conversational memory

### 🔧 Custom Multi-Tool Agent
Built a LangGraph-powered agent capable of orchestrating multiple tools with stateful execution.

### 📊 Structured Output Pipeline
Created production-ready pipelines using Pydantic models for reliable, type-safe LLM outputs.

---

## 🎓 Skills Demonstrated

This repository showcases proficiency in:

- **AI Engineering**: End-to-end LLM application development
- **RAG Architecture**: Vector databases, retrieval strategies, context management
- **Agent Development**: Tool integration, state management, multi-step reasoning
- **Prompt Engineering**: Effective LLM communication patterns
- **Production Practices**: Error handling, async operations, modular design
- **API Integration**: Working with commercial and open-source LLM APIs

---

## 🚀 Getting Started

### Prerequisites
```bash
python >= 3.8
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file with your API keys:
```bash
COHERE_API_KEY=your_cohere_key
HUGGINGFACE_API_KEY=your_hf_key
```

### Run Examples
```bash
# Navigate to any module
cd 1.LLMs

# Run the examples
python example.py
```

---

## 📈 Learning Journey

This repository represents a structured approach to mastering modern AI engineering:

1. **Foundations**: Understanding LLMs and embeddings
2. **Components**: Learning LangChain's building blocks
3. **Integration**: Combining components into chains and workflows
4. **Advanced**: Building stateful agents with LangGraph
5. **Production**: Creating end-to-end RAG applications

---

## 🤝 Connect With Me

**Bibek Sah** | [@bibek373](https://github.com/bibek373)

💼 Open to collaborations on GenAI projects  
📧 Interested in AI engineering opportunities  
🌟 Passionate about building intelligent systems  

---

## 📝 License

This project is open source and available for educational purposes.

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Built with ❤️ using LangChain

</div>
