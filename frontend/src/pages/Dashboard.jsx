import { Link } from "react-router-dom";

function Dashboard() {

  const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  return (
    <div className="min-h-screen bg-gray-100 p-10">

      <div className="flex justify-between items-center mb-8">

        <h1 className="text-3xl font-bold">
          WhatsApp SaaS Dashboard
        </h1>

        <button
          onClick={logout}
          className="bg-red-500 text-white px-4 py-2 rounded"
        >
          Logout
        </button>

      </div>

      <div className="grid grid-cols-2 gap-6">

        <Link
          to="/businesses"
          className="bg-white p-8 rounded-xl shadow hover:shadow-lg"
        >
          <h2 className="text-2xl font-bold">
            Businesses
          </h2>

          <p className="mt-4 text-gray-600">
            Manage businesses
          </p>
        </Link>

        <Link
          to="/messages"
          className="bg-white p-8 rounded-xl shadow hover:shadow-lg"
        >
          <h2 className="text-2xl font-bold">
            Messages
          </h2>

          <p className="mt-4 text-gray-600">
            Send WhatsApp messages
          </p>
        </Link>

      </div>

    </div>
  );
}

export default Dashboard;