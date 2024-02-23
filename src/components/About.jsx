import React from "react";

const About = () => {
  return (
    <div
      name="about"
      className="w-full h-screen bg-gradient-to-b from-gray-800 to-black text-white"
    >
      <div className="max-w-screen-lg p-4 mx-auto flex flex-col justify-center w-full h-full">
        <div className="pb-8">
          <p className="text-4xl font-bold inline border-b-4 border-gray-500">
            About
          </p>
        </div>

        <p className="text-xl mt-20">
        Hello! I am Avanindra Vijay, a passionate and results-driven individual with a diverse background in computer science and cybersecurity. Currently, I am exploring the intersection of technology and business as a Salesforce Developer Intern at Deloitte SCJ.
        </p>

        <br />

        <p className="text-xl">
        I am enthusiastic about leveraging technology to solve complex problems, and I am always eager to take on new challenges. Let's connect and explore the endless possibilities in the world of technology!
        </p>
      </div>
    </div>
  );
};

export default About;