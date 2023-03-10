import React, { useState, useEffect } from 'react';
import { FaTrash, FaHeart, FaArrowCircleLeft } from "react-icons/fa";
import { Link, Routes, Route, useNavigate } from 'react-router-dom';
import Logo from './images/logo.png';
import "./Home.css";
import "./CreateReview.css";

/**
 * 
 * @returns //sets up messages, title and body
 */
const Create = () => {
  const [title, setTitle] = useState('');
  const [flights, setFlights] = useState('');
  const [body, setBody] = useState('');

  // handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(flights);
    console.log(title);
    console.log(body);

    addPosts(title, flights, body);
    navigate('/');
  };

  const navigate = useNavigate();


  /**
   * POST request to post to database using title and body boxes
   * @param {text} title 
   * @param {text} body 
   */
  const addPosts = async (titleSubmit, num, BodySubmit) => {
    try {
      const requestOptions = {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        },
        body: JSON.stringify({ title: title, message: BodySubmit, flight_number: num, phonenumber: "" })
      };
      fetch('https://sky-scout.onrender.com/postreview', requestOptions)
      setTitle('');
      setFlights('');
      setBody('');
      console.log(title);
    } catch (error) {
      console.log(error);
    }
  };


  // 	const navigation = this.props.navigation;


  // 	const handleFormSubmit = event => {
  //     event.preventDefault();

  // 	navigation.navigate('/Home')
  //   };

  //html with the wepage ui: structred the same order as the web is displayed
  return (
    <div className="app">
      <nav>
        <img id="logo" src={Logo} alt="SkyScout" />

        {/* route to Home page */}
        <div className='nav-btn-container'>
          <h2 className="nav-btn shadow"><Link to="/">Home</Link></h2>

          {/* route to Statistics page */}
          <h2 className="nav-btn shadow"><Link to="/statistics">Statistics</Link></h2>

          {/* route to Create Review page */}
          <h2 className="nav-btn shadow"><Link to="/create">Create Review</Link></h2>
        </div>
      </nav>
      <div className='container'>


        {/* <div  className="my-element"> */}
        <h1 className='header'>Create Review</h1>
        {/* </div> */}
        {/* <div className="add-post-container"> */}
        <div className='sub_form'>
        <form onSubmit={handleSubmit}>
          <h2> Flight Number </h2>

          <input
            type="text"
            className="input_field Flight"
            name="flights"
            value={flights}
            onChange={(e) => setFlights(e.target.value)}
          />
          <h2> Title </h2>

          <input
            type="text"
            className="input_field Title"
            name="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
          <h2> Message </h2>
          <textarea
            name=""
            className="input_field Review"
            id=""
            cols="10"
            rows="8"
            value={body}
            onChange={(e) => setBody(e.target.value)}
          ></textarea>

          {/* <input
					type="text"
					className="form-control"
					name="title"
					value={body}
					onChange={(e) => setBody(e.target.value)}
				    /> */}
          {/* <div> */}
          <button className='btn' type="submit" id="submit"  ><b><font size="+3"> Submit </font> </b></button>
          {/* </div> */}
        </form>
        </div>
        {/* </div> */}
      </div>
    </div>
  );
};

export default Create;