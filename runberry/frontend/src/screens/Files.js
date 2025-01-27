import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import axios from 'axios';
import FileRow from '../components/FileRow';
import Navigation from '../components/Navigation';

export default function Files() {

  const [files, setFiles] = useState({
    "path": "",
    "files": []
  });

  const location = useLocation();
  const navigate = useNavigate();
  let filesPath = location.pathname;
  if (filesPath.startsWith("/files")) {
    filesPath = filesPath.slice(6);
  }

  // refresh files every 200ms
  useEffect(() => {
    const refreshFiles = () => {
      axios.get("/api/files" + filesPath)
          .then(res => setFiles(res.data))
          .catch(err => {
            if (err.response && err.response.status === 404) {
              setFiles({ path: filesPath, files: [] });
            } else {
              console.error(err);
            }
          });
    }

    refreshFiles();
    const interval = setInterval(refreshFiles, 200);
    return () => clearInterval(interval);
  }, [filesPath]);

  useEffect(() => {
    localStorage.setItem("lastFilesPath", location.pathname.replace(/^\/files\/?/, "/"));
  }, [filesPath]);

  const pathSegments = filesPath.split("/");
  const currentFolderName = pathSegments[pathSegments.length - 1];
  const parentFolder = pathSegments.slice(0, pathSegments.length - 1).join("/");

  const execute = (file, args) => {
    axios.post("/api/processes", { path: file.path, args })
        .then(res => {
          const {uid} = res.data
          navigate(`/processes/${uid}/logs`)
        })
        .catch(err => console.error(err));
  }

  return (
    <div className="container" style={{paddingTop: "2em"}}>
      <Navigation locationName={currentFolderName || "Home"} parentLocation={currentFolderName ? "/files" + parentFolder : null} />
      <ul className="list-group">
        {files.files.map(file => (
          <FileRow key={file.name} file={file} onExecute={(file, params) => execute(file, params)} />
        ))}
      </ul>
    </div>
  );
}