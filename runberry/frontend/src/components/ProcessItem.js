import { faBug, faCheckCircle, faClock, faClose, faCog, faList, faSkull } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link } from "react-router-dom";
import TimeAgo from "./TimeAgo";

export default function ProcessItem({ 
  uid,
  name="Process",
  start_timestamp=null,
  stop_timestamp=null,
  exit_code=null,
  onKill=()=>{console.log("Kill button clicked")}
 }) {

  const killButton = <button className="btn btn-danger btn-sm float-end" style={{marginRight: '0.5em'}} onClick={onKill}>
      <FontAwesomeIcon icon={faClose} />
    </button>;

  let statusLabel = null;
  let statusIcon = null;
  let statusBg = null;
  if (stop_timestamp && exit_code === 0) {
    statusLabel = "Completed";
    statusIcon = faCheckCircle
    statusBg = "list-group-item-info"
  } else if (stop_timestamp && exit_code == 137) {
    statusLabel = "Killed";
    statusIcon = faSkull
    statusBg = "list-group-item-danger"
  } else if (stop_timestamp) {
    statusLabel = "Failed";
    statusIcon = faBug
    statusBg = "list-group-item-danger"
  } else {
    statusLabel = "Running for";
    statusIcon = faCog
    statusBg = ""
  }

  return (
    <li className={"list-group-item d-flex justify-content-between align-items-center " + statusBg}>
      <div>
        <div>
          <FontAwesomeIcon icon={statusIcon} spin={statusLabel == "Running for"} />
          <strong style={{paddingLeft: '0.5em'}} >{name}</strong>
        </div>
        <div>
          <small style={{fontSize: '0.7em'}} className="text-muted">
            <i>
              {statusLabel} <span><TimeAgo timestamp={stop_timestamp || start_timestamp}/>{statusLabel === 'Running for' ? "" : " ago"}</span>
            </i>
          </small>
        </div>
      </div>
      <div>
        <Link to={`/processes/${uid}/logs`} className="btn btn-primary btn-sm float-end" style={{marginRight: '0.5em'}}>
          <FontAwesomeIcon icon={faList} />
        </Link>
        {stop_timestamp ? null : killButton}
      </div>
    </li>
  );

}