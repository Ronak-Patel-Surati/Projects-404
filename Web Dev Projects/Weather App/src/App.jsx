import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import NavBar from "./Components/NavBar";
import Temp from "./Components/Temp";
import Thumbnail from "./Components/Thumbnail";

function App() {
  return (
    <>
      <div class="absolute top-0 z-[-2] h-screen w-screen bg-[#000000] bg-[radial-gradient(#ffffff33_1px,#00091d_1px)] bg-[size:20px_20px]">
        <NavBar />
        <div className="rounded-xl px-2 py-2">
          <Thumbnail />
          <div className="label px-4 py-4 my-4  mx-auto">
            <span className=" bg-slate-50 rounded-md px-4 py-1 my-4  mx-auto">
              Made with 💗 by Ronak 
            </span>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
