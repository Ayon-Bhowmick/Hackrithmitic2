import React from 'react';
import { Link } from "react-router-dom";

const Home = () => {
    return (
		<div className="app">
			<nav>
            <h1> SkyScout </ h1>
                {/* route to Home page */}
                <h2><Link to="/">Home</Link></h2>
               
                {/* route to Statistics page */}
                <h2><Link to="/Stats">Statistics</Link></h2>
            
                {/* route to Create Review page */}
                <h2><Link to="/Create">Create Review</Link></h2>
			</nav>
		</div>
	);
}

export default Home;