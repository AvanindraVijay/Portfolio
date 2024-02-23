import React from 'react'

const Map = () => {
  return (
    <div
    name="contact"
    className="w-full h-screen bg-gradient-to-b from-black to-gray-800 p-4 text-white"
  >
    <div className="flex flex-col p-4 justify-center max-w-screen-lg mx-auto h-full">
      <div className="pb-8">
        <p className="text-4xl font-bold inline border-b-4 border-gray-500">
          Location
        </p>
        <p className="py-6"></p>
      </div>

          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14432.265610304546!2d81.360711899322!3d25.268351597337528!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3984d04d159e7185%3A0xd177d860b072cd61!2sMau%2C%20Uttar%20Pradesh%20210209!5e0!3m2!1sen!2sin!4v1708684772900!5m2!1sen!2sin"
              width="100%"
              height="500px"
              style={{ border: 0, borderRadius: "1rem" }}
              allowFullScreen
              title="Map of location"
              />

    </div>
  </div>
  )
}

export default Map
