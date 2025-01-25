import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import Navigation from "../components/Navigation";

export default function Logs() {
  const { uid } = useParams();

  const [logs, setLogs] = useState('')
  const [process, setProcess] = useState(null)
  const [snapEnd, setSnapEnd] = useState(true)

  // refresh logs every 200ms
  useEffect(() => {

    const refreshLogs = () => {
      axios.get(`/api/processes/${uid}/logs`)
          .then(res => setLogs(res.data))
          .catch(err => {
            console.error(err);
          });
    }

    refreshLogs();
    const interval = setInterval(refreshLogs, 200);
    return () => clearInterval(interval);
  }, [uid]);

  useEffect(() => {
    axios.get(`/api/processes/${uid}`)
        .then(res => setProcess(res.data))
        .catch(err => console.error(err));
  }, [uid]);

  // monitor scroll position
  useEffect(() => {
    window.onscroll = () => {
      if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 50) {
        setSnapEnd(true)
      } else {
        setSnapEnd(false)
      }
    }
    return () => window.onscroll = null;
  }, []);

  useEffect(() => {
    if (!snapEnd) return
    setTimeout(() => {
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight
      window.scrollTo(0, maxScroll)
    }, 25)
  }, [logs, snapEnd]);

  return (
    <div className="container" style={{paddingTop: "2em"}}>
      <Navigation locationName={process ? process.name : 'Process'} parentLocation={`/processes/`} />
      <pre style={{fontSize: '0.6em', paddingBottom: '1em'}}>{logs}</pre>
    </div>
  );

}