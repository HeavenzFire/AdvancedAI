import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [mood, setMood] = useState('');
  const [moodHistory, setMoodHistory] = useState([]);

  useEffect(() => {
    axios.get('/moodHistory')
      .then((response) => {
        setMoodHistory(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const handleTrackMood = () => {
    axios.post('/trackMood', { mood })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Mood Tracker</h1>
      <input
        type="text"
        value={mood}
        onChange={(e) => setMood(e.target.value)}
        placeholder="Enter mood"
      />
      <button onClick={handleTrackMood}>Track Mood</button>
      <ul>
        {moodHistory.map((moodEntry) => (
          <li key={moodEntry._id}>{moodEntry.mood}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
