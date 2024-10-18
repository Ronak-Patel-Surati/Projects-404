import React, { useState, useEffect } from "react";
import Weather from "./WeatherData";
import QuoteGenerator from "./Quates";
import img1 from "../assets/1.jpg";
import img2 from "../assets/2.jpg";
import img3 from "../assets/3.jpg";
import img4 from "../assets/4.jpg";
import img5 from "../assets/5.jpg";
import img6 from "../assets/6.jpg";
import img7 from "../assets/7.jpg";
import img8 from "../assets/8.jpg";
import img9 from "../assets/9.jpg";
import img10 from "../assets/10.jpg";
import img11 from "../assets/11.jpg";
import img12 from "../assets/12.jpg";

const Thumbnail = () => {
  const [cdate, setCdate] = useState("");
  const [bgImage, setBgImage] = useState("");

  const images = [
    img1,
    img2,
    img3,
    img4,
    img5,
    img6,
    img7,
    img8,
    img9,
    img10,
    img11,
    img12,
  ];

  const dateBuilder = (d) => {
    let months = [
      "January",
      "February",
      "March",
      "April",
      "May",
      "June",
      "July",
      "August",
      "September",
      "October",
      "November",
      "December",
    ];
    let days = [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ];

    let day = days[d.getDay()];
    let date = d.getDate();
    let month = months[d.getMonth()];
    let year = d.getFullYear();

    return `${day}, ${date} ${month} ${year}`;
  };

  const getRandomImage = () => {
    const randomIndex = Math.floor(Math.random() * images.length);
    return images[randomIndex];
  };

  useEffect(() => {
    const now = new Date();
    setCdate(dateBuilder(now));
    setBgImage(getRandomImage());
  }, []);

  return (
    <div className="flex h-[80vh] my-4 mx-auto w-4/5 p-2 outline-1 rounded-xl border-2 border-white/70 bg-slate-600">
      {/* Left Side */}
      <div
        className="w-3/5 p-4 flex flex-col justify-between h-full bg-cover bg-center relative"
        style={{ backgroundImage: `url(${bgImage})` }}
      >
        <div className="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
        <div className="relative z-10 p-4 flex flex-col h-full">
          <h2 className="text-white text-xl mb-4">Weather</h2>
          <div className="flex-grow"></div>
          <div className="flex flex-col items-start justify-end">
            <div className="text-teal-50">
              <QuoteGenerator />
              <h2 className="px-4">{cdate}</h2>
            </div>
          </div>
        </div>
      </div>

      {/* Right Side */}
      <div className="w-2/5 p-4 bg-white [background:radial-gradient(125%_125%_at_50%_10%,#fff_40%,#63e_100%)]">
        <h2 className="text-white">Right Side Content</h2>
        <Weather />
      </div>
    </div>
 
  );
};

export default Thumbnail;
