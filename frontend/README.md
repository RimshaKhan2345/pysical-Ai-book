# Physical AI & Humanoid Robotics Frontend

This is the frontend for the Physical AI & Humanoid Robotics Book with Embedded RAG Chatbot. It provides an interactive interface for users to read the book content and ask questions using the RAG (Retrieval-Augmented Generation) chatbot.

## Features

- Interactive RAG chatbot for querying robotics book content
- Responsive design for various screen sizes
- Integration with the backend API for RAG functionality
- Ability to query both full content and selected text

## Tech Stack

- React.js for the user interface
- CSS for styling
- REST API integration for backend communication

## Getting Started

### Prerequisites

- Node.js (version 18 or higher)
- npm or yarn package manager

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd physical-ai-robotics-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file in the frontend directory with the following content:
   ```
   REACT_APP_API_BASE_URL=http://localhost:8000/api/v1
   ```
   Adjust the API URL if your backend is running on a different address.

4. Start the development server:
   ```bash
   npm start
   ```

The application will be available at `http://localhost:3000`.

## Project Structure

```
frontend/
├── public/              # Public assets
├── src/                 # Source code
│   ├── components/      # React components
│   │   └── RoboticsRagChatbot.js  # Main chatbot component
│   ├── services/        # API services
│   │   └── roboticsRagApi.js      # API service for RAG functionality
│   ├── css/            # CSS styles
│   │   ├── App.css     # Main application styles
│   │   └── RoboticsRagChatbot.css # Chatbot component styles
│   ├── App.js          # Main application component
│   └── index.js        # Entry point
├── package.json        # Dependencies and scripts
└── README.md           # This file
```

## API Integration

The frontend communicates with the backend API at the following endpoints:

- `POST /api/v1/robotics/query` - Submit a query about robotics concepts
- `GET /api/v1/robotics/topics` - Get available robotics topics
- `POST /api/v1/robotics/feedback` - Submit feedback on responses

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is part of the Physical AI & Humanoid Robotics Book and follows the project's licensing terms.