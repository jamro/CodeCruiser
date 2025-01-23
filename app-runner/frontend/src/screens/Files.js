import React, { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronLeft } from '@fortawesome/free-solid-svg-icons';
import FileRow from '../components/FileRow';

export default function Files() {

  const [files, setFiles] = useState({
    "path": "",
    "files": []
  });

  const location = useLocation();
  let filesPath = location.pathname;
  if (filesPath.startsWith("/files")) {
    filesPath = filesPath.slice(6);
  }

  useEffect(() => {
    axios.get("/api/files" + filesPath)
        .then(res => setFiles(res.data))
        .catch(err => {
          if (err.response && err.response.status === 404) {
            setFiles({ path: filesPath, files: [] });
          } else {
            console.error(err);
          }
        });
  }, [location.pathname]);

  const pathSegments = filesPath.split("/");
  const currentFolderName = pathSegments[pathSegments.length - 1];
  const parentFolder = pathSegments.slice(0, pathSegments.length - 1).join("/");

  let backButton = null;
  if (currentFolderName) {
    backButton = (
      <li className="breadcrumb-item">
        <Link to={"/files" + parentFolder} >
          <FontAwesomeIcon icon={faChevronLeft} />
        </Link>
      </li>
    );
  }

  const execute = (file, args) => {
    axios.post("/api/processes", { path: file.path, args })
        .then(res => console.log(res.data))
        .catch(err => console.error(err));
  }

  return (
    <div className="container">
      <nav aria-label="breadcrumb">
        <ol className="breadcrumb">
          {backButton}
          <li className="breadcrumb-item active" aria-current="page">{currentFolderName || "Home"}</li>
        </ol>
      </nav>
      <ul className="list-group">
        {files.files.map(file => (
          <FileRow key={file.name} file={file} onExecute={(file, params) => execute(file, params)} />
        ))}
      </ul>
    </div>
  );
}