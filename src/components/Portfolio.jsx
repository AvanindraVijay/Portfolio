import React from "react";
import KiitHospitality from "../assets/portfolio/KIIT-Hospitality.jpg";
import AlgoFitness from "../assets/portfolio/AlgoFitness.jpg";
import RestaurantRecipeMenu from "../assets/portfolio/RESTAURANT-RECIPE-MENU.jpg";
import Calculator from "../assets/portfolio/Calculator.jpg";
import ToDoList from "../assets/portfolio/T0D0-List.jpg";
import WeatherForecast from "../assets/portfolio/WeatherForecast.jpg";

const Portfolio = () => {
  const portfolios = [
    {
      id: 1,
      Name: "Kiit Hospitality",
      src: KiitHospitality,
      href: "https://github.com/AvanindraVijay/KIIT-Hospitality.git"
    },
    {
      id: 2,
      Name: "Algo Fitness",
      src: AlgoFitness,
      href: "https://github.com/AvanindraVijay/AlgoFitness.git"
    },
    {
      id: 3,
      Name: "Restaurant Recipe Menu",
      src: RestaurantRecipeMenu,
      href: "https://github.com/AvanindraVijay/RESTAURANT-RECIPE-MENU.git"
    },
    {
      id: 4,
      Name: "Weather Forecast",
      src: WeatherForecast ,
      href: "https://github.com/AvanindraVijay/WeatherForecast.git"
    },
    {
      id: 5,
      Name: "Calculator",
      src: Calculator,
      href: "https://github.com/AvanindraVijay/Calculator.git"
    },
    {
      id: 6,
      Name: "ToDo List",
      src: ToDoList,
      href: "https://github.com/AvanindraVijay/T0D0-List.git"
    },
  ];

  return (
    <div
      name="portfolio"
      className="bg-gradient-to-b from-black to-gray-800 w-full text-white md:h-screen"
    >
      <div className="max-w-screen-lg p-4 mx-auto flex flex-col justify-center w-full h-full">
        <div className="pb-8">
          <p className="text-4xl font-bold inline border-b-4 border-gray-500">
            Portfolio
          </p>
          <p className="py-6">Check out some of my work right here</p>
        </div>

        <div className="grid sm:grid-cols-2 md:grid-cols-3 gap-8 px-12 sm:px-0">
          {portfolios.map(({ id, src,Name,href }) => (
            <div key={id} className="shadow-md shadow-gray-600 rounded-lg">
              <img
                src={src}
                alt=""
                className="rounded-md duration-200 hover:scale-105"
              />
              <div key={id} className="flex items-center justify-center">
                <a href={href} target="_blank" rel="noopener noreferrer">
                  <button className="w-1/2 px-6 py-3 m-4 duration-200 hover:scale-105">
                    Code
                  </button>
                </a>
               </div>
               <div key={id}>
                    {Name && (
                        <h3 className="text-xl font-semibold text-center mt-2">{Name}</h3>
                    )}
                </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Portfolio;