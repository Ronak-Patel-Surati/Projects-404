// src/components/NavBar.jsx
import React from 'react';
import { TiWeatherStormy } from "react-icons/ti";
import { MdOutlineHistoryToggleOff } from "react-icons/md";
import { FaGithub } from "react-icons/fa";

const NavBar = () => {
  return (
    <nav className='flex flex-wrap items-center justify-between bg-gray-900 text-white p-4 px-8'>
      {/* Logo Section */}
      <div className="logo flex items-center text-2xl">
        Ronak's Weather App
        <TiWeatherStormy className='ml-2 text-3xl' />
      </div>

      {/* Navigation Links */}
      <ul className='flex space-x-4 mt-2 md:mt-0'>
        <li>
          <a 
            href="/history" 
            target='_blank' 
            rel='noopener noreferrer' 
            className='flex items-center px-8 py-1 hover:text-gray-300 transition-colors duration-200'
            aria-label="View History"
          >
            History
            <MdOutlineHistoryToggleOff className='ml-1 text-xl' />
          </a>
        </li>
        |
        <li>
          <a 
            href="https://github.com/Ronak-Patel-Surati/Portfolio/tree/main/Weather%20App" 
            target='_blank' 
            rel='noopener noreferrer' 
            className='flex items-center px-2 py-1 hover:text-gray-300 transition-colors duration-200'
            aria-label="View on GitHub"
          >
            GitHub
            <FaGithub className='ml-1 text-xl' />
          </a>
        </li>
      </ul>
    </nav>
  );
};

export default NavBar;
