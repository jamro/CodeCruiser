import { faClose, faCog, faList, faSkull } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link } from "react-router-dom";

export default function ProcessItem({ 
  uid,
  name="Process",
  start_timestamp=null,
  stop_timestamp=null,
  onKill=()=>{console.log("Kill button clicked")}
 }) {


  const killButton = <button className="btn btn-danger btn-sm float-end" style={{marginRight: '0.5em'}} onClick={onKill}>
      <FontAwesomeIcon icon={faClose} />
    </button>;

  return (
    <li className={"list-group-item " + (stop_timestamp ? "list-group-item-danger" : "")}>
      <FontAwesomeIcon icon={stop_timestamp ? faSkull : faCog} spin={!stop_timestamp} />
      <strong style={{paddingLeft: '0.5em'}} >{name}</strong>
      <Link to={`/processes/${uid}/logs`} className="btn btn-primary btn-sm float-end" style={{marginRight: '0.5em'}}>
        <FontAwesomeIcon icon={faList} />
      </Link>
      {stop_timestamp ? null : killButton}
    </li>
  );

}