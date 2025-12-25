import React from 'react';
import RoboticsRagChatbot from './components/RoboticsRagChatbot';
import './css/RoboticsRagChatbot.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Physical AI & Humanoid Robotics Book</h1>
        <p>Interactive learning with RAG-powered assistance</p>
      </header>
      <main>
        <section className="chatbot-section">
          <RoboticsRagChatbot />
        </section>
      </main>
    </div>
  );
}

export default App;