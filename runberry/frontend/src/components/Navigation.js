import React from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronLeft, faHome } from '@fortawesome/free-solid-svg-icons';

export default function Navigation({locationName = "Home", parentLocation = null, children=null}) {

  if (parentLocation === null) {
    return <nav className="navbar fixed-top bg-body-tertiary p-2">
      <p className='p-0 m-0'>
        <FontAwesomeIcon icon={faHome} fixedWidth /> {locationName}
      </p>
    </nav>
  }
  
  return <nav className="navbar fixed-top bg-body-tertiary p-2">
      <Link to={parentLocation}  style={{textDecoration: "none"}} className="text-dark">
        <FontAwesomeIcon icon={faChevronLeft} fixedWidth/>  {locationName}
      </Link>
      {children}
    </nav>
}