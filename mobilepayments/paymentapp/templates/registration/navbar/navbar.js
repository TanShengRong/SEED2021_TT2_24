import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
    return (
        <nav className = 'navbar'>
            <ul>
                <li>
                    <Link className = 'a' to='/'>Login Page</Link>
                </li>
                <li>
                    <Link className = 'a' to='/'>Home Page</Link>
                </li>
                <li>
                    <Link className = 'a' to='/'>Payment Page</Link>
                </li>
                <li>
                    <Link className = 'a' to='/'>Balance Page</Link>
                </li>
                <li>
                    <Link className = 'a' to='/'>History Page</Link>
                </li>
            </ul>
        </nav>
    );
};

export default NavBar;