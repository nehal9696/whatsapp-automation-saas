import { useEffect, useState } from "react";

import API from "../api/axios";

function Businesses() {

  const [businesses, setBusinesses] = useState([]);
  const [name, setName] = useState("");

  const fetchBusinesses = async () => {
    try {

      const response = await API.get("/api/businesses");

      setBusinesses(response.data);

    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchBusinesses();
  }, []);

  const createBusiness = async (e) => {
    e.preventDefault();

    try {

      await API.post("/api/business", {
        name,
      });

      setName("");

      fetchBusinesses();

    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-10">

      <h1 className="text-3xl font-bold mb-8">
        Businesses
      </h1>

      <form
        onSubmit={createBusiness}
        className="bg-white p-6 rounded-xl shadow mb-8"
      >

        <input
          type="text"
          placeholder="Business Name"
          className="border p-3 rounded w-full mb-4"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <button
          type="submit"
          className="bg-black text-white px-6 py-3 rounded"
        >
          Create Business
        </button>

      </form>

      <div className="grid grid-cols-3 gap-6">

        {businesses.map((business) => (

          <div
            key={business.id}
            className="bg-white p-6 rounded-xl shadow"
          >

            <h2 className="text-xl font-semibold">
              {business.name}
            </h2>

          </div>

        ))}

      </div>

    </div>
  );
}

export default Businesses;