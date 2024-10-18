import React from 'react'

const NavBar = () => {
  return (
    <nav className='flex justify-between items-center bg-blue-900 text-white ' >
        <div className="logo text-2xl font-semibold items-center mx-4 my-1 px-3">
            Not a Todo
        </div>
        <ul className='flex justify-between mx-2 px-6 py-2 text-lg font-semibold my-1'>
            <li className='px-3 cursor-pointer hover:text-blue-300'><a href="" target="_blank" rel="noopener noreferrer">Home</a></li>
            <li className=' px-3 cursor-pointer hover:text-blue-300'><a href="" target="_blank" rel="noopener noreferrer">TaskList</a></li>
        </ul>
    </nav>
  )
}

export default NavBar
