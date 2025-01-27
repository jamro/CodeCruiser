import React, { useEffect, useState } from "react";
import Menu from "./components/Menu";
import { Routes, Route, Navigate, useLocation } from "react-router-dom";
import Files from "./screens/Files";
import Processes from "./screens/Processes";
import Logs from "./screens/Logs";

function App() {

  const location = useLocation();
  const [lastFilesPath, setLastFilesPath] = useState(localStorage.getItem("lastFilesPath") || "/");

  useEffect(() => {
    setLastFilesPath(localStorage.getItem("lastFilesPath") || "/");
  }, [location.pathname]);

  return (
      <div style={{ marginTop: "20px", paddingBottom: "3em" }}> 
        <Routes>
          <Route path="/" element={<Navigate to="/files" replace />} />
          <Route path="/files/*" element={<Files />} />
          <Route path="/processes" element={<Processes />} />
          <Route path="/processes/:uid/logs" element={<Logs />} />
        </Routes>
        <Menu filesPath={"/files" + lastFilesPath} />
      </div>
  );

}

export default App;