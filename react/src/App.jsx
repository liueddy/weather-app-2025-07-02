import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [data, setData] = useState("");
  const [loading, setLoading] = useState(true);
  const [city, setCity] = useState("boston");
  const [units, setUnits] = useState("standard");

  useEffect(() => {
    fetchSetData();
    setLoading(false)
  }, [city,units])

  async function fetchSetData() {
    const res = await fetch(`http://localhost:5000/weather?city=${city}&units=${units}`);
    const result = await res.json();
    setData(result["data"])
  }

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name === 'city') {
      setCity(value);
    } else if (name === 'units') {
      setUnits(value);
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault(); // Prevents default form submission (page reload)
    // Your custom logic for handling form submission
    console.log(`city:${city}, units:${units}`);
    // Access form data, perform validation, make API calls, etc.
  };

  if (loading) return <p>Loading data...</p>;
  return (
    <>
      <h1>weather</h1>
      <form onSubmit={handleSubmit}>
        <label>City:</label><br />
        <input type="text" id="city" name="city" value={city} onChange={handleChange} /><br />
        <label>Units:</label><br />
        <select name="units" id="units" onChange={handleChange}>
          <option value="standard">Standard</option>
          <option value="metric">Metric</option>
          <option value="imperial">Imperial</option>
        </select>
        <br /><br />
        {/* <input type="submit" value="Submit" /> */}
      </form>
      <p>{JSON.stringify(data, null, 2)}</p>
    </>
  )
}

export default App
