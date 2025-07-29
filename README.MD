# RAG-Practical: Langchain-Based RAG System

A comprehensive Retrieval-Augmented Generation (RAG) system built with Langchain, featuring PDF processing, LLM integration, voice features, and adaptive learning capabilities.

## 🚀 Features

### Core Functionality
- **PDF Processing**: Extract and process text from PDF documents
- **Question Generation**: AI-powered question generation from document content
- **RAG System**: Retrieval-Augmented Generation for intelligent question answering
- **Voice Integration**: Text-to-speech and speech-to-text capabilities
- **Adaptive Learning**: Personalized learning paths based on student performance
- **Progress Tracking**: Comprehensive analytics and progress monitoring

### Advanced Features
- **Multi-language Support**: Translation capabilities for multiple languages
- **Teacher Mode**: Classroom management and question paper generation
- **Vector Database**: Efficient document storage and retrieval
- **Real-time Processing**: Fast and responsive document analysis
- **Export Functionality**: CSV export of generated questions

## 🛠️ Technology Stack

- **Backend**: FastAPI, Python
- **AI/ML**: Langchain, OpenAI, Hugging Face Transformers
- **Document Processing**: PyPDF2, pdfplumber
- **Vector Database**: ChromaDB, FAISS
- **Voice Processing**: SpeechRecognition, pyttsx3
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: SQLite, JSON

## 📁 Project Structure

```
Langchain Projects/
├── app.py                 # Main FastAPI application
├── requirements.txt       # Python dependencies
├── setup.py              # Package configuration
├── README.MD             # Project documentation
├── .gitignore            # Git ignore rules
├── src/                  # Core source code
│   ├── __init__.py
│   ├── helper.py         # LLM pipeline and utilities
│   └── prompt.py         # Prompt templates
├── templates/            # HTML templates
│   ├── index.html        # Main interface
│   ├── script.js         # Frontend JavaScript
│   └── style.css         # Styling
├── static/               # Static files
│   ├── docs/            # Document storage
│   └── output/          # Generated outputs
├── Data/                # Sample PDF documents
│   ├── Python Programming.pdf
│   ├── DSA notes.pdf
│   └── ...
├── research/            # Research and experiments
│   └── interview.ipynb  # Research notebooks
└── venv/               # Virtual environment (ignored)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/fli-09/RAG-Practical.git
   cd RAG-Practical
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file with your API keys
   echo "OPENAI_API_KEY=your_openai_key_here" > .env
   echo "HUGGINGFACE_API_KEY=your_huggingface_key_here" >> .env
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and go to `http://localhost:8000`
   - Upload a PDF document
   - Generate questions or ask questions about the content

## 📖 Usage Guide

### Basic Usage

1. **Upload PDF Document**
   - Navigate to the upload page
   - Select a PDF file from your computer
   - Click "Upload and Process"

2. **Generate Questions**
   - After upload, the system will extract text
   - Choose question type (MCQ, True/False, etc.)
   - Select number of questions
   - Click "Generate Questions"

3. **Ask Questions**
   - Use the RAG system to ask questions about the document
   - Get AI-powered answers with source references
   - Use voice input/output for hands-free interaction

### Advanced Features

#### Voice Integration
- **Text-to-Speech**: Convert generated questions to audio
- **Speech-to-Text**: Ask questions using voice input
- **Multi-language**: Support for multiple languages

#### Adaptive Learning
- **Progress Tracking**: Monitor learning progress
- **Personalized Questions**: Questions adapted to skill level
- **Performance Analytics**: Detailed performance insights

#### Teacher Mode
- **Class Management**: Create and manage classes
- **Question Paper Generation**: Generate custom question papers
- **Student Analytics**: Track student performance

## 🔧 Configuration

### Environment Variables
```bash
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
GOOGLE_API_KEY=your_google_api_key
```

### API Configuration
The system supports multiple LLM providers:
- OpenAI GPT models
- Google Gemini models
- Hugging Face models
- Local models

## 📊 Features in Detail

### PDF Processing
- **Text Extraction**: Extract text from PDF documents
- **Structure Analysis**: Identify headings, sections, and content hierarchy
- **Metadata Extraction**: Extract document metadata
- **Multi-page Support**: Handle documents with multiple pages

### Question Generation
- **Multiple Types**: MCQ, True/False, Short Answer, Essay
- **Difficulty Levels**: Easy, Medium, Hard
- **Topic-based**: Generate questions for specific topics
- **Custom Prompts**: Use custom prompt templates

### RAG System
- **Document Indexing**: Create vector embeddings of documents
- **Semantic Search**: Find relevant content for questions
- **Context Retrieval**: Retrieve relevant context chunks
- **Answer Generation**: Generate answers with source references

### Voice Features
- **Offline TTS**: Text-to-speech without internet
- **Online TTS**: High-quality cloud-based TTS
- **Speech Recognition**: Convert speech to text
- **Multi-language**: Support for multiple languages

## 🧪 Testing

### Run Tests
```bash
# Run basic tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=src tests/
```

### Manual Testing
1. Upload a sample PDF document
2. Test question generation
3. Test RAG question answering
4. Test voice features
5. Test export functionality

## 📈 Performance

### Optimization Features
- **Caching**: Cache generated questions and embeddings
- **Batch Processing**: Process multiple documents efficiently
- **Memory Management**: Optimized memory usage for large documents
- **Async Processing**: Non-blocking operations for better UX

### Benchmarks
- **PDF Processing**: ~2-5 seconds per page
- **Question Generation**: ~10-30 seconds for 10 questions
- **RAG Response**: ~1-3 seconds per question
- **Voice Processing**: ~2-5 seconds for speech recognition

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Add tests for new features**
5. **Commit your changes**
   ```bash
   git commit -m "Add: your feature description"
   ```
6. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run linting
flake8 src/
black src/

# Run tests
pytest tests/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Langchain**: For the excellent framework
- **OpenAI**: For GPT models and API
- **Hugging Face**: For transformers and models
- **FastAPI**: For the web framework
- **Community**: For contributions and feedback

## 📞 Support

If you encounter any issues or have questions:

1. **Check the documentation** in this README
2. **Search existing issues** on GitHub
3. **Create a new issue** with detailed information
4. **Contact the maintainers** for urgent issues

## 🔮 Roadmap

### Upcoming Features
- [ ] **Multi-modal Support**: Image and video processing
- [ ] **Real-time Collaboration**: Multi-user editing
- [ ] **Advanced Analytics**: Detailed learning insights
- [ ] **Mobile App**: Native mobile application
- [ ] **API Documentation**: Comprehensive API docs
- [ ] **Plugin System**: Extensible architecture

### Version History
- **v1.0.0**: Initial release with core RAG functionality
- **v1.1.0**: Added voice features and adaptive learning
- **v1.2.0**: Enhanced PDF processing and teacher mode

---

**Made with ❤️ for the AI/ML community**

*This project demonstrates practical applications of RAG systems in educational technology.*
