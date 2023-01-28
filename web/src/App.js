
import React, { useState, useEffect } from 'react';
import { FaTrash , FaHeart, FaPlusCircle, FaThumbsUp, FaThumbsDown} from "react-icons/fa";
import {
	BrowserRouter,
	Routes,
	Route,
	Link
  } from "react-router-dom";
import Home from "./pages/Home";
import Stats from "./pages/Stats";
import Create from "./pages/Create";



/**
 * 
 * @returns //sets up messages, title and body
 */
function App() {

	return(
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<Home />} />
				<Route path="/statistics" element={<Stats />} />
				<Route path="/create" element={<Create />} />
			</Routes>
		</BrowserRouter>
	)
}

export default App;

	