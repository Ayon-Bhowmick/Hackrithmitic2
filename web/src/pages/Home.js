import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";
import "./Home.css";
import Logo from './images/logo.png';
<style>
  @import url('https://fonts.googleapis.com/css2?family=Itim&family=Montserrat:wght@100;500;600;700&display=swap');
</style>

const Home = () => {
	const [messages, setMessages] = useState(null);
	const [title, setTitle] = useState('');
	const [body, setBody] = useState('');

	/**
	 * GET request to retieve message from database using fetch
	 */
	useEffect(() => {
		fetch("https://sky-scout.onrender.com/display").then(response => {
			return response.json();
		}).then(data => {
		    setMessages(data);
            return data;
		})


	}, [messages]);



    return (
        
		<div className="app">
			<nav>
            <img  id="logo" src={Logo} alt="SkyScout" />

            {/* route to Home page */}
            <div className='nav-btn-container'>
                <h2 className="nav-btn shadow"><Link to="/">Home</Link></h2>
                
                {/* route to Statistics page */}
                <h2 className="nav-btn shadow"><Link to="/statistics">Statistics</Link></h2>
            
                {/* route to Create Review page */}
                <h2 className="nav-btn shadow"><Link to="/create">Create Review</Link></h2>
            </div>
			</nav>

            {/* <div className="review-container">
                <div className="innerWhiteBox">
                    <h1>Review</h1>
                </div>
            </div> */}
            <h1 id="home-reviews-title">Reviews:</h1>
				
            {messages && messages.map((review) => {
                return (
                    <div className="review-container" key={review.title}>
                        <div className="review-header" style={{ display: 'flex', flexWrap: 'nowrap', flexDirection: 'row', justifyContent: "space-between"}}>
                            <h3 className="review-num">Flight Number: {review.flight_number}</h3>
                            <h2 className="review-title"> {review.title}</h2>
                            <h3 className="review-message"> {review.created_at}</h3>
                        </div>
                        <h3 className="review-message"> {review.message}</h3>
                    </div>
                );
            })}

            {/* <div className="footer-container">
                <footer>
                    <div id="copyright">
                        <p>© 2023 SkyScout Hackrithimic 2 Hackathon Team</p>
                    </div>
                </footer>
            </div> */}

            {/* <div className="footer-container">
                <footer>
                    <div id="copyright">
                        <p>© 2023 SkyScout Hackrithimic 2 Hackathon Team</p>
                    </div>
                </footer>
            </div> */}
		</div>
	);
}

export default Home;