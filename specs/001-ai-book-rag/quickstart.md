# Quickstart Guide: AI/Spec-Driven Book with Embedded RAG Chatbot

## Prerequisites
- Python 3.11+
- Node.js 18+
- Git
- Access to OpenAI API
- Access to Neon Serverless Postgres (free tier)
- Access to Qdrant Cloud (free tier)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your API keys and database URLs
```

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Set environment variables
cp .env.example .env
# Edit .env with your API endpoints
```

### 4. Environment Variables
Create `.env` files in both backend and frontend with the following:

**Backend (.env):**
```
OPENAI_API_KEY=your_openai_api_key
NEON_DATABASE_URL=your_neon_database_url
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
SECRET_KEY=your_secret_key
```

**Frontend (.env):**
```
REACT_APP_API_BASE_URL=http://localhost:8000/api/v1
```

### 5. Initialize Database
```bash
# In backend directory
python -m src.core.init_db
```

### 6. Load Book Content
```bash
# In backend directory
python -m src.core.load_content
```

### 7. Run the Applications

**Backend:**
```bash
# In backend directory
uvicorn src.main:app --reload --port 8000
```

**Frontend:**
```bash
# In frontend directory
npm start
```

## Running Tests
```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

## Building for Production
```bash
# Backend
cd backend
pip install -r requirements-prod.txt

# Frontend
cd frontend
npm run build
```

## Deployment
The frontend is designed to be deployed to GitHub Pages, while the backend can be deployed to any Python-compatible hosting service.

1. Build the frontend: `npm run build`
2. Deploy the backend to a cloud service
3. Update the API endpoint in the frontend configuration
4. Push the frontend build to the `gh-pages` branch