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
    const interval = setInterval(fetchProcesses, 200);
    return () => clearInterval(interval);
  }, []);


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
          />
        ))}
      </ul>
    </div>
  );
}