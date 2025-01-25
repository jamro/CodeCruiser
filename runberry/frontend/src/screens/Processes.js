import React, { useEffect, useState } from "react";
import axios from "axios";
import ProcessItem from "../components/ProcessItem";

export default function Processes() {

  const [processes, setProcesses] = useState([])

  useEffect(() => {

    const fetchProcesses = () => {
      axios.get("/api/processes")
          .then(res => setProcesses(res.data))
          .catch(err => {
            if (err.response && err.response.status === 404) {
              setProcesses([]);
            } else {
              console.error(err);
            }
          });
    }
    
    fetchProcesses();
    const interval = setInterval(fetchProcesses, 2000);
    return () => clearInterval(interval);
  }, []);


  const kill = (uid) => {

    const fetchProcesses = () => {
      axios.get("/api/processes")
          .then(res => setProcesses(res.data))
          .catch(err => {
            if (err.response && err.response.status === 404) {
              setProcesses([]);
            } else {
              console.error(err);
            }
          });
    }

    axios.delete(`/api/processes/${uid}`)
      .then(() => fetchProcesses())
      .catch(err => console.error(err));
  }

  return (
    <div className="container">
      <ul className="list-group">
        {processes.map(p => (
          <ProcessItem 
            key={p.uid} 
            uid={p.uid}
            name={p.name} 
            start_timestamp={p.start_timestamp}
            stop_timestamp={p.stop_timestamp}
            onKill={() => kill(p.uid)}
          />
        ))}
      </ul>
    </div>
  );
}