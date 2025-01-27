import { faCog, faFile, faFileArrowDown, faFolderClosed } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link } from "react-router-dom";
import { useState } from "react";
import FileDropdown from "./FileDropdown";
import { Modal } from 'react-bootstrap';

export default function FileRow({ file, onExecute = () => {} }) {

  const [includeParams, setIncludeParams] = useState(false);
  const [params, setParams] = useState("");
  const [execModalVisible, setExecModalVisible] = useState(false);

  const showExecuteModal = () => {
    setExecModalVisible(true);
  };

  if (file.is_directory) {
    return (
      <li className="list-group-item">
        <Link to={"/files/" + file.path} style={{ textDecoration: "none" }} className="text-dark">
          <FontAwesomeIcon icon={faFolderClosed} /> {file.name}
        </Link>
      </li>
    );
  }
  if (file.is_executable || file.looks_executable) {
    return (
      <li className="list-group-item d-flex justify-content-between align-items-center">
        <button className="btn btn-link text-dark" style={{ textDecoration: "none", padding: 0 }} onClick={showExecuteModal}>
          <FontAwesomeIcon icon={faCog} fixedWidth /> {file.name}
        </button>
        <FileDropdown file={file} onExecute={showExecuteModal} />
        <Modal show={execModalVisible} onHide={() => setExecModalVisible(false)}>
          <Modal.Header closeButton>
            <Modal.Title>Run {file.name}?</Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <form>
              <div className="mb-3 form-check">
                <input
                  type="checkbox"
                  className="form-check-input"
                  id={`addParamsCheckbox_${file.name}`}
                  checked={includeParams}
                  onChange={() => setIncludeParams(!includeParams)}
                />
                <label className="form-check-label" htmlFor={`addParamsCheckbox_${file.name}`}>
                  Add input parameters
                </label>
              </div>
              <div className="mb-3" hidden={!includeParams}>
                <label htmlFor="inputParams" className="form-label">Parameters</label>
                <input
                  type="text"
                  className="form-control"
                  placeholder="Enter parameters"
                  value={params}
                  onChange={(e) => setParams(e.target.value)}
                />
              </div>
            </form>
          </Modal.Body>
          <Modal.Footer>
            <button type="button" className="btn btn-secondary" onClick={() => setExecModalVisible(false)}>No</button>
            <button type="button" className="btn btn-primary" onClick={() => onExecute(file, params)}>Yes</button>
          </Modal.Footer>
        </Modal>
      </li>
    );
  }
  if (file.is_downloadable) {
    return (
      <li className="list-group-item d-flex justify-content-between align-items-center">
        <a
          href={"/api/raw_files/" + file.path}
          style={{ textDecoration: "none" }}
          target="_blank"
          rel="noreferrer"
          className="text-dark"
        >
          <FontAwesomeIcon icon={faFileArrowDown} fixedWidth /> {file.name}
        </a>
        <FileDropdown file={file} onExecute={showExecuteModal} />
      </li>
    );
  }
  return (
    <li className="list-group-item d-flex justify-content-between align-items-center">
      <span className="text-dark">
        <FontAwesomeIcon icon={faFile} fixedWidth /> {file.name}
      </span>
      <FileDropdown file={file} onExecute={showExecuteModal} />
    </li>
  );
}