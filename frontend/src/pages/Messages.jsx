import { useState } from "react";

import API from "../api/axios";

function Messages() {
  const [formData, setFormData] = useState({
    content: "",
    phone: "",
    business_id: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]:
        e.target.name === "business_id"
          ? Number(e.target.value)
          : e.target.value,
    });
  };

  const sendMessage = async (e) => {
    e.preventDefault();

    try {
      await API.post("/api/send-message", formData);

      alert("Message sent");
    } catch (error) {
      console.log(error);

      if (error.response) {
        alert(error.response.data.detail || "Failed to send message");
      } else {
        alert("Server error or network issue");
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-3xl font-bold mb-8">Send Message</h1>

      <form
        onSubmit={sendMessage}
        className="bg-white p-6 rounded-xl shadow w-full max-w-lg"
      >
        <input
          type="text"
          name="phone"
          placeholder="Phone Number"
          className="border p-3 rounded w-full mb-4"
          onChange={handleChange}
        />

        <input
          type="text"
          name="business_id"
          placeholder="Business ID"
          className="border p-3 rounded w-full mb-4"
          onChange={handleChange}
        />

        <textarea
          name="content"
          placeholder="Message"
          className="border p-3 rounded w-full mb-4"
          rows="5"
          onChange={handleChange}
        />

        <button type="submit" className="bg-black text-white px-6 py-3 rounded">
          Send Message
        </button>
      </form>
    </div>
  );
}

export default Messages;
