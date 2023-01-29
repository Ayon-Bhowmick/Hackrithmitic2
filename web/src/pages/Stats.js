import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";
import "./Home.css";
import Logo from './images/logo.png';
import Loading from './Loading.js';
<style>
@import url('https://fonts.googleapis.com/css2?family=Itim&display=swap');
</style>

const Stats = () => {
    const [imageUrl, setImageUrl] = useState(null);
    const [loading, setLoading] = useState(true);


    const fetchImage = async () => {
      setLoading(true);
    try{
      const response = await fetch('https://sky-scout.onrender.com/graph');
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      setLoading(false);
      setImageUrl(url);
    }catch(e){
        setLoading(true);
        console.log(e);
    }
    }
    
    

    useEffect(() => {
      fetchImage();
    }, []);

    if(loading){
        return (
            <div className="app">
                <nav>
            <img  id="logo" src={Logo} alt="SkyScout" />

            {/* route to Home page */}
            <div>
                <h2 className="nav-btn shadow"><Link to="/">Home</Link></h2>
                
                {/* route to Statistics page */}
                <h2 className="nav-btn shadow"><Link to="/statistics">Statistics</Link></h2>
            
                {/* route to Create Review page */}
                <h2 className="nav-btn shadow"><Link to="/create">Create Review</Link></h2>
            </div>
			</nav>

            <Loading />

            <div className="footer-container">
                <footer>
                    <div id="copyright">
                        <p>© 2023 SkyScout Hackrithimic 2 Hackathon Team</p>
                    </div>
                </footer>
            </div>

            </div>
        );
    }

    return (
        
		<div className="app">
			<nav>
            <img  id="logo" src={Logo} alt="SkyScout" />

            {/* route to Home page */}
            <div>
                <h2 className="nav-btn shadow"><Link to="/">Home</Link></h2>
                
                {/* route to Statistics page */}
                <h2 className="nav-btn shadow"><Link to="/statistics">Statistics</Link></h2>
            
                {/* route to Create Review page */}
                <h2 className="nav-btn shadow"><Link to="/create">Create Review</Link></h2>
            </div>
			</nav>

            <h1>Statistics</h1>
            <div>
                {imageUrl && <img src={imageUrl} alt="My Image" />}
            </div>

            <div className="footer-container">
                <footer>
                    <div id="copyright">
                        <p>© 2023 SkyScout Hackrithimic 2 Hackathon Team</p>
                    </div>
                </footer>
            </div>

		</div>
	);
}

export default Stats;