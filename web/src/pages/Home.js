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
            <div>
                <h2 className="nav-btn shadow"><Link to="/">Home</Link></h2>
                
                {/* route to Statistics page */}
                <h2 className="nav-btn shadow"><Link to="/statistics">Statistics</Link></h2>
            
                {/* route to Create Review page */}
                <h2 className="nav-btn shadow"><Link to="/create">Create Review</Link></h2>
            </div>
			</nav>

            <div className="review-container">
                <div className="innerWhiteBox">
                    <h1>Review</h1>
                </div>
            </div>


            <h2>All Posts</h2>
				
            {messages && messages.map((post) => {
                return (
                    <div className="post-card" key={post.title}>
                        <h2 className="post-title"> {post.message}</h2>
                        <h3 className="body">{post.flight_number}</h3>
                        <h3 className="body">{post.created_at}</h3>
                    </div>
                );
            })}
            
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

export default Home;