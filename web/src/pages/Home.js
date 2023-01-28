import React from 'react';
import { Link } from "react-router-dom";
import "./Home.css";
import Logo from './images/logo.png';

const Home = () => {
    return (
		<div className="app">
			<nav>
            <img src={Logo} alt="SkyScout" />

            {/* route to Home page */}
            <h2 class="nav-btn"><Link to="/">Home</Link></h2>
            
            {/* route to Statistics page */}
            <h2 class="nav-btn"><Link to="/statistics">Statistics</Link></h2>
        
            {/* route to Create Review page */}
            <h2 class="nav-btn"><Link to="/create">Create Review</Link></h2>
			</nav>
		</div>
	);
}

export default Home;