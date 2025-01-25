import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

export default function Logs() {
  const { uid } = useParams();

  const [logs, setLogs] = useState('')

  const refreshLogs = () => {
    axios.get(`/api/processes/${uid}/logs`)
        .then(res => setLogs(res.data))
        .catch(err => {
          if (err.response && err.response.status === 404) {
            setLogs('');
          } else {
            console.error(err);
          }
        });
  }

  // refresh logs every 200ms
  useEffect(() => {
    refreshLogs();
    const interval = setInterval(refreshLogs, 200);
    return () => clearInterval(interval);
  }, [uid]);

  

  return (
      <pre style={{fontSize: '0.6em'}}>{logs}</pre>
  );

}