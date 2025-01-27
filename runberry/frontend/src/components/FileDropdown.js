import { faCog, faDownload, faEllipsisV } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";


export default function FileDropdown({ file, onExecute = () => {} }) {  

  const options = []

  if(file.is_executable || file.looks_executable) {
    options.push({ id: "execute", icon: faCog, label: "Execute", onClick: () => onExecute(file) });
  }
  if(file.is_downloadable) {
    options.push({ id: "download", icon: faDownload, label: "Download", onClick: () => window.open("/api/raw_files/" + file.path) });
  }

  const optionElements = options.map(option => (
    <li key={option.id}>
      <button className="dropdown-item" onClick={option.onClick}>
        <FontAwesomeIcon icon={option.icon} /> {option.label}
      </button>
    </li>
  ))

  if (options.length === 0) {
    return null;
  }

  return <div className="dropdown p-0 m-0">
    <button
      className="btn btn-link text-dark p-0 m-0"
      type="button"
      id={"dropdownMenuButton" + file.uid}
      data-bs-toggle="dropdown"
      aria-expanded="false"
      style={{border: "none"}}
    >
      <FontAwesomeIcon icon={faEllipsisV} />
    </button>
    <ul className="dropdown-menu" aria-labelledby={"dropdownMenuButton" + file.uid}>
      {optionElements}
    </ul>
  </div>;

}
