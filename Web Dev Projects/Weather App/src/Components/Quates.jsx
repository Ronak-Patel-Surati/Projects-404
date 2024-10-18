import React, { useState } from 'react';

const QuoteGenerator = () => {
  // List of quotes
  const quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "The best way to predict your future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
    "The best revenge is massive success. - Frank Sinatra",
    "We must accept finite disappointment, but never lose infinite hope. - Martin Luther King Jr.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "The harder you work for something, the greater you’ll feel when you achieve it. - Unknown",
    "Dream it. Believe it. Build it. - Unknown",
    "Believe you can and you’re halfway there. - Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. - William James",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
    "Everything you’ve ever wanted is on the other side of fear. - George Addair",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "The secret of success is to do the common thing uncommonly well. - John D. Rockefeller Jr.",
    "If you can dream it, you can achieve it. - Zig Ziglar",
    "You don’t have to be great to start, but you have to start to be great. - Zig Ziglar",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Everything has beauty, but not everyone can see. - Confucius",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "Life is either a daring adventure or nothing at all. - Helen Keller",
    "What we think, we become. - Buddha",
    "It does not do to dwell on dreams and forget to live. - J.K. Rowling",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "The only way to have a friend is to be one. - Ralph Waldo Emerson",
    "You can’t go back and change the beginning, but you can start where you are and change the ending. - C.S. Lewis",
    "The most wasted of days is one without laughter. - E.E. Cummings"
  ];
  

  // State to store the current quote
  const [quote, setQuote] = useState('');

  // Function to get a random quote
  const getRandomQuote = () => {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    setQuote(quotes[randomIndex]);
  };

  // Set an initial quote when the component mounts
  React.useEffect(() => {
    getRandomQuote();
  }, []);

  return (
    <div className="quote-container p-4">
      <p className="quote-text text-3xl text-blue-100 font-300">{quote}</p>
      
    </div>
  );
};

export default QuoteGenerator;
