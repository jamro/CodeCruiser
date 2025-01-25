import { faCog, faFile, faFolderClosed } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link } from "react-router-dom";
import { useState } from "react";

export default function FileRow({ file, onExecute = () => {} }) {

  const [includeParams, setIncludeParams] = useState(false);
  const [params, setParams] = useState("");

  if (file.is_directory) {
    return (
      <li className="list-group-item">
        <Link to={"/files/" + file.path} style={{ textDecoration: "none" }}>
          <FontAwesomeIcon icon={faFolderClosed} /> {file.name}
        </Link>
      </li>
    );
  }
  if (file.is_executable || file.looks_executable) {
    return (
      <li className="list-group-item">
        <button className="btn btn-link" style={{ textDecoration: "none", padding: 0 }} data-bs-toggle="modal" data-bs-target={`#modal_${file.name}`}>
          <FontAwesomeIcon icon={faCog} /> {file.name}
        </button>
        <div className="modal fade" tabIndex="-1" aria-hidden="true" aria-labelledby={`modal_${file.name}`} id={`modal_${file.name}`}>
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h1 className="modal-title fs-5" id={`modal_label_${file.name}`}>Run {file.name}?</h1>
                <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div className="modal-body">
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
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">No</button>
                <button type="button" className="btn btn-primary" onClick={() => onExecute(file, params)} data-bs-dismiss="modal">Yes</button>
              </div>
            </div>
          </div>
        </div>
      </li>
    );
  }
  if (file.is_viewable) {
    return (
      <li className="list-group-item">
        <a href={"/api/raw_files/" + file.path} style={{ textDecoration: "none" }} target="_blank" rel="noreferrer">
          <FontAwesomeIcon icon={faFile} /> {file.name}
        </a>
      </li>
    );
  }
  return (
    <li className="list-group-item">
      <FontAwesomeIcon icon={faFile} /> {file.name}
    </li>
  );
}