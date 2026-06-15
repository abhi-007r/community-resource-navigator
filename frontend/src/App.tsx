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
      alert("Failed to connect to backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "50px auto",
        padding: "20px",
        fontFamily: "Arial",
      }}
    >
      <h1>Community Resource Navigator</h1>

      <p>
        Find local resources for housing,
        food, employment, legal aid,
        and mental health.
      </p>

      <textarea
        placeholder="Describe your situation..."
        rows={6}
        value={situation}
        onChange={(e) =>
          setSituation(e.target.value)
        }
        style={{
          width: "100%",
          padding: "10px",
        }}
      />

      <br />
      <br />

      <button
        onClick={handleGetRecommendations}
        disabled={loading}
      >
        {loading
          ? "Loading..."
          : "Get Recommendations"}
      </button>

      {categories.length > 0 && (
        <div style={{ marginTop: "30px" }}>
          <h2>Recommended Categories</h2>

          <ul>
            {categories.map((category) => (
              <li key={category}>
                {category}
              </li>
            ))}
          </ul>
        </div>
      )}

      {resources.length > 0 && (
        <div style={{ marginTop: "30px" }}>
          <h2>Matching Resources</h2>

          {resources.map((resource) => (
            <div
              key={resource.id}
              style={{
                border: "1px solid #ccc",
                borderRadius: "8px",
                padding: "15px",
                marginBottom: "15px",
              }}
            >
              <h3>{resource.name}</h3>

              <p>
                <strong>Category:</strong>{" "}
                {resource.category}
              </p>

              <p>
                {resource.description}
              </p>

              <p>
                <strong>Location:</strong>{" "}
                {resource.city}, {resource.state}
              </p>

              <p>
                <strong>Phone:</strong>{" "}
                {resource.phone}
              </p>

              <p>
                <strong>Website:</strong>{" "}
                <a
                  href={resource.website}
                  target="_blank"
                  rel="noreferrer"
                >
                  {resource.website}
                </a>
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;