import React, { useState, useEffect, useRef } from 'react';
import styles from './RoboticsRagChatbot.module.css';

const RoboticsRagChatbot = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [selectedText, setSelectedText] = useState('');
  const messagesEndRef = useRef(null);

  // Function to scroll to the bottom of the chat
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Function to get selected text from the page
  useEffect(() => {
    const handleSelection = () => {
      const selectedText = window.getSelection().toString().trim();
      setSelectedText(selectedText);
    };

    document.addEventListener('mouseup', handleSelection);
    return () => {
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  // Function to send a query to the backend
  const sendQuery = async (queryText) => {
    if (!queryText.trim()) return;

    setIsLoading(true);

    // Add user message to the chat
    const userMessage = {
      id: Date.now(),
      text: queryText,
      sender: 'user',
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);

    try {
      // In a real implementation, this would call the backend API
      // For now, we'll simulate the API response
      const response = await simulateApiCall(queryText);
      
      const botMessage = {
        id: Date.now() + 1,
        text: response.answer,
        sender: 'bot',
        sources: response.sources || [],
        timestamp: new Date()
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        id: Date.now() + 1,
        text: 'Sorry, I encountered an error processing your request. Please try again.',
        sender: 'bot',
        isError: true,
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  // Simulate API call for demonstration purposes
  const simulateApiCall = async (queryText) => {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 1000));

    // For demo purposes, return a simulated response
    return {
      answer: `This is a simulated response to your query: "${queryText}". In a real implementation, this would come from the RAG system based on the Physical AI & Humanoid Robotics book content.`,
      sources: [
        { title: 'Introduction to Physical AI & Humanoid Robotics', section: 'intro' },
        { title: 'The Robotic Nervous System (ROS 2)', section: 'chapter-1' }
      ]
    };
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim()) {
      sendQuery(inputValue);
      setInputValue('');
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className={styles.chatbotContainer}>
      <div className={styles.chatHeader}>
        <h3>Robotics RAG Chatbot</h3>
        <p>Ask questions about the Physical AI & Humanoid Robotics book</p>
      </div>
      
      <div className={styles.chatMessages}>
        {messages.length === 0 ? (
          <div className={styles.welcomeMessage}>
            <p>Hello! I'm your Robotics RAG assistant. Ask me anything about the Physical AI & Humanoid Robotics book.</p>
            <p>Try asking about ROS 2, Gazebo, NVIDIA Isaac, Vision-Language-Action, or any other robotics concept covered in the book.</p>
          </div>
        ) : (
          messages.map((message) => (
            <div 
              key={message.id} 
              className={`${styles.message} ${message.sender === 'user' ? styles.userMessage : styles.botMessage}`}
            >
              <div className={styles.messageContent}>
                <p>{message.text}</p>
                {message.sources && message.sources.length > 0 && (
                  <div className={styles.sources}>
                    <p>Sources:</p>
                    <ul>
                      {message.sources.map((source, index) => (
                        <li key={index}>{source.title} ({source.section})</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          ))
        )}
        {isLoading && (
          <div className={`${styles.message} ${styles.botMessage}`}>
            <div className={styles.messageContent}>
              <p className={styles.typingIndicator}>Thinking...</p>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      
      <form className={styles.chatInputForm} onSubmit={handleSubmit}>
        {selectedText && (
          <div className={styles.selectedTextPreview}>
            <p>Selected text: <em>"{selectedText.substring(0, 100)}{selectedText.length > 100 ? '...' : ''}"</em></p>
          </div>
        )}
        <div className={styles.inputContainer}>
          <textarea
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask a question about the robotics book..."
            disabled={isLoading}
            rows="3"
          />
          <button 
            type="submit" 
            disabled={isLoading || !inputValue.trim()}
            className={styles.sendButton}
          >
            {isLoading ? 'Sending...' : 'Send'}
          </button>
        </div>
        <div className={styles.inputHints}>
          <p>Tip: You can ask about specific robotics concepts like ROS 2, Gazebo, NVIDIA Isaac, or Vision-Language-Action.</p>
        </div>
      </form>
    </div>
  );
};

export default RoboticsRagChatbot;