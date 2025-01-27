import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCog, faFolderClosed, faFolderOpen } from '@fortawesome/free-solid-svg-icons';
import { Link, useLocation } from 'react-router-dom';

export default function Menu({
  filesPath = "/files",
}) {

  const location = useLocation();
  const firstChunk = location.pathname.split('/')[1];

  const buttons = [];
  if (firstChunk !== "files" && firstChunk !== "") {
    buttons.push(
      <Link to={filesPath} className="btn btn-dark col-6" key="files">
        <FontAwesomeIcon icon={faFolderClosed} size="2x" />
      </Link>
    );
  } else {
    buttons.push(
      <button className="btn btn-light col-6" key="files" disabled>
        <FontAwesomeIcon icon={faFolderOpen} size="2x" />
      </button>
    );
  }
  if (firstChunk !== "processes") {
    buttons.push(
      <Link to="/processes" className="btn btn-dark col-6" key="processes">
        <FontAwesomeIcon icon={faCog} size="2x" />
      </Link>
    );
  } else {
    buttons.push(
      <button className="btn btn-light col-6" key="processes" disabled>
        <FontAwesomeIcon icon={faCog} size="2x" spin />
      </button>
    );
  }

  return (
    <nav className="navbar fixed-bottom bg-body-tertiary" data-bs-theme="dark">
      <div className="container">
        {buttons}
      </div>
    </nav>
  );
}