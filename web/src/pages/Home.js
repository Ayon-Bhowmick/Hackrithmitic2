import React from 'react';
import { Link } from "react-router-dom";
import "./Home.css";
import Logo from './images/logo.png';

const Home = () => {
    return (
		<div className="app">
			<nav>
            <img  id="logo" src={Logo} alt="SkyScout" />

            {/* route to Home page */}
            <div>
                <h2 class="nav-btn shadow"><Link to="/">Home</Link></h2>
                
                {/* route to Statistics page */}
                <h2 class="nav-btn shadow"><Link to="/statistics">Statistics</Link></h2>
            
                {/* route to Create Review page */}
                <h2 class="nav-btn shadow"><Link to="/create">Create Review</Link></h2>
            </div>
			</nav>
		</div>
	);
}

export default Home;