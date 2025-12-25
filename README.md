# Physical AI & Humanoid Robotics Book with Embedded RAG Chatbot

This repository contains an interactive book on Physical AI & Humanoid Robotics with an embedded RAG (Retrieval-Augmented Generation) chatbot. The project is built using Docusaurus for the book content, FastAPI for the backend RAG service, and React for the chatbot UI.

## Overview

The Physical AI & Humanoid Robotics Book is designed for CS/engineering students and developers in robotics/AI. It covers:

1. **The Robotic Nervous System (ROS 2)** - How ROS 2 provides the communication backbone for robot systems
2. **The Digital Twin (Gazebo & Unity)** - Using simulation tools for robot testing and validation
3. **The AI-Robot Brain (NVIDIA Isaac™)** - NVIDIA's platform for AI-powered robot control
4. **Vision-Language-Action (VLA)** - How robots integrate perception, understanding, and action

The embedded RAG chatbot allows users to query both full content and selected text, providing contextually relevant answers based on the book content.

## Project Structure

```
my-website/
├── backend/                 # FastAPI backend for RAG functionality
│   ├── src/                 # Backend source code
│   │   ├── models/          # Data models
│   │   ├── services/        # Business logic
│   │   ├── api/             # API endpoints
│   │   └── core/            # Core utilities
│   ├── requirements.txt     # Python dependencies
│   └── .env.example        # Environment variables example
├── frontend/                # React frontend for RAG chatbot
│   ├── src/                 # Frontend source code
│   │   ├── components/      # React components
│   │   ├── services/        # API services
│   │   └── css/            # Styles
│   ├── package.json         # Node.js dependencies
│   └── README.md           # Frontend documentation
├── docs/                    # Docusaurus book content
│   ├── intro.md            # Introduction
│   ├── chapter-1-robotic-nervous-system.md
│   ├── chapter-2-digital-twin.md
│   ├── chapter-3-ai-robot-brain.md
│   ├── chapter-4-vision-language-action.md
│   └── conclusion.md
├── src/                     # Docusaurus custom components
├── docusaurus.config.ts     # Docusaurus configuration
├── sidebars.ts              # Navigation sidebar configuration
└── package.json            # Docusaurus dependencies
```

## Getting Started

### Prerequisites

- Node.js (version 18 or higher)
- Python (version 3.11 or higher)
- Access to OpenAI API
- Access to Neon Postgres (free tier)
- Access to Qdrant Cloud (free tier)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and database URLs
   ```

5. Start the backend server:
   ```bash
   python -m src.main
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

### Docusaurus Book Setup

1. At the project root, install dependencies:
   ```bash
   npm install
   ```

2. Start the Docusaurus development server:
   ```bash
   npm start
   ```

The book will be available at `http://localhost:3000`.

## Environment Variables

### Backend (.env)
```
OPENAI_API_KEY=your_openai_api_key
NEON_DATABASE_URL=your_neon_database_url
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
SECRET_KEY=your_secret_key
```

### Frontend (.env)
```
REACT_APP_API_BASE_URL=http://localhost:8000/api/v1
```

## API Endpoints

The backend provides the following API endpoints:

- `POST /api/v1/robotics/query` - Submit a query about robotics concepts
- `GET /api/v1/robotics/topics` - Get available robotics topics
- `GET /api/v1/health` - Check the health status of the API

## Deployment

The frontend is designed to be deployed to GitHub Pages, while the backend can be deployed to any Python-compatible hosting service.

1. Build the Docusaurus site: `npm run build`
2. Deploy the backend to a cloud service (e.g., Heroku, AWS, GCP)
3. Update the API endpoint in the frontend configuration
4. Deploy the Docusaurus build to GitHub Pages

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Docusaurus](https://docusaurus.io/)
- Backend powered by [FastAPI](https://fastapi.tiangolo.com/)
- Frontend using [React](https://reactjs.org/)
- RAG functionality powered by [OpenAI](https://openai.com/) and [Qdrant](https://qdrant.tech/)