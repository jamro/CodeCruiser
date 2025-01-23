import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

export default function Logs() {
  const { uid } = useParams();

  const [logs, setLogs] = useState('')

  useEffect(() => {
    axios.get(`/api/processes/${uid}/logs`)
        .then(res => setLogs(res.data))
        .catch(err => {
          if (err.response && err.response.status === 404) {
            setLogs('');
          } else {
            console.error(err);
          }
        });
  }, []);

    return (
        <pre style={{fontSize: '0.6em'}}>{logs}</pre>
    );

}