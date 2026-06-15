import { useState } from "react";
import { getRecommendations } from "./services/api";

interface Resource {
  id: number;
  name: string;
  category: string;
  description: string;
  city: string;
  state: string;
  phone: string;
  website: string;
}

function App() {
  const [situation, setSituation] = useState("");
  const [categories, setCategories] = useState<string[]>([]);
  const [resources, setResources] = useState<Resource[]>([]);
  const [loading, setLoading] = useState(false);

  const handleGetRecommendations = async () => {
    try {
      setLoading(true);

      const data = await getRecommendations(
        situation
      );

      setCategories(
        data.recommended_categories || []
      );

      setResources(
        data.resources || []
      );
    } catch (error) {
      console.error(error);
      alert("Failed to get recommendations");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100">
      <div className="max-w-5xl mx-auto px-6 py-16">
        <h1 className="text-4xl md:text-5xl font-bold text-slate-900 mb-4">
          Community Resource Navigator
        </h1>

        <p className="text-lg text-slate-600 mb-10">
          Find local resources for housing,
          food, employment, legal aid, and
          mental health.
        </p>

        <div className="bg-white rounded-2xl shadow-lg p-8">
          <textarea
            value={situation}
            onChange={(e) =>
              setSituation(e.target.value)
            }
            placeholder="Describe your situation..."
            rows={4}
            className="
              w-full
              border
              border-slate-300
              rounded-xl
              p-4
              text-slate-800
              focus:outline-none
              focus:ring-2
              focus:ring-blue-500
            "
          />

          <button
            onClick={handleGetRecommendations}
            disabled={loading}
            className="
              mt-5
              bg-blue-600
              text-white
              px-6
              py-3
              rounded-xl
              font-medium
              hover:bg-blue-700
              transition
              disabled:bg-gray-400
            "
          >
            {loading
              ? "Loading..."
              : "Get Recommendations"}
          </button>
        </div>

        {categories.length > 0 && (
          <div className="mt-10">
            <h2 className="text-2xl font-semibold mb-4">
              Recommended Categories
            </h2>

            <div className="flex flex-wrap gap-3">
              {categories.map((category) => (
                <span
                  key={category}
                  className="
                    bg-green-100
                    text-green-800
                    px-4
                    py-2
                    rounded-full
                    font-medium
                  "
                >
                  {category}
                </span>
              ))}
            </div>
          </div>
        )}

        {resources.length > 0 && (
          <div className="mt-10">
            <h2 className="text-2xl font-semibold mb-6">
              Matching Resources
            </h2>

            <div className="grid gap-6">
              {resources.map((resource) => (
                <div
                  key={resource.id}
                  className="
                    bg-white
                    rounded-2xl
                    shadow-lg
                    p-6
                    border
                    border-slate-200
                  "
                >
                  <h3 className="text-xl font-bold text-slate-900">
                    {resource.name}
                  </h3>

                  <p className="text-blue-600 font-medium mt-1">
                    {resource.category}
                  </p>

                  <p className="text-slate-600 mt-4">
                    {resource.description}
                  </p>

                  <div className="mt-4 space-y-2 text-slate-700">
                    <p>
                      📍 {resource.city},{" "}
                      {resource.state}
                    </p>

                    <p>
                      📞 {resource.phone}
                    </p>

                    <a
                      href={resource.website}
                      target="_blank"
                      rel="noreferrer"
                      className="
                        inline-block
                        text-blue-600
                        hover:underline
                      "
                    >
                      🔗 Visit Website
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;