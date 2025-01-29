import React, { useEffect, useState } from "react"
import Link from 'next/link';

export default function MyProfile() {

    const [query, setQuery] = useState("");
    const [photos, setPhotos] = useState([]);

    const fetchPhotos = async () => {
        try {
          const response = await fetch(`http://localhost:5000/profile?query=${query}`);
          if (response.ok) {
            const data = await response.json();
            setPhotos(data.results); // Unsplash API returns results in the 'results' field
          } else {
            alert("Failed to fetch photos");
          }
        } catch (error) {
          console.error("Error fetching photos:", error);
        }
      };

  return (
    <div className="max-w-md mx-auto mt-10 p-4 border rounded-lg shadow-md">
      <h1 className="text-xl font-bold mb-4">Search for a profile picture</h1>
      <input
        type="text"
        placeholder="Enter search term"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="w-full p-2 mb-4 border rounded-lg"
      />
      <button
        onClick={fetchPhotos}
        className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600"
      >
        Search Photos
      </button>
      <div className="mt-4 grid grid-cols-2 gap-2">
        {photos.map((photo) => (
          <img
            key={photo.id}
            src={photo.urls.small}
            alt={photo.alt_description}
            className="w-full rounded-lg"
          />
        ))}
      </div>
      <Link href="/">Back to home</Link>
    </div>
  );
}