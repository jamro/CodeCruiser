import React from "react";
import Menu from "./components/Menu";
import { Routes, Route, Navigate } from "react-router-dom";
import Files from "./screens/Files";
import Processes from "./screens/Processes";
import Logs from "./screens/Logs";

function App() {
  
    // use bootstrap for styling
    return (
        <div style={{ marginTop: "20px" }}> 
          <Routes>
            <Route path="/" element={<Navigate to="/files" replace />} />
            <Route path="/files/*" element={<Files />} />
            <Route path="/processes" element={<Processes />} />
            <Route path="/processes/:uid/logs" element={<Logs />} />
          </Routes>
          <Menu />
        </div>
    );

}

export default App;