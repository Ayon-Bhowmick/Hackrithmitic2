
import React, { useState, useEffect } from 'react';
import { FaTrash , FaHeart, FaArrowCircleLeft } from "react-icons/fa";
import {Link, Routes, Route, useNavigate} from 'react-router-dom';
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
		// navigate('/');
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
				body: JSON.stringify({ title: title, message: BodySubmit, flight_number: num, phonenumber: ""})
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
	

  const url = "https://sky-scout.onrender.com/postreview";
  const [data, setData] = useState({
    title: "",
    flightNum: "",
    review: "",
    phoneNum: "",
  })


  function handle(e) {
    const newdata = { ...data }
    newdata[e.target.id] = e.target.value
    setData(newdata)
    // console.log(newdata)
  }

  function submit(e) {
    e.preventDefault();
    Axios.post(url, {
      title: data.name,
      flightNum: data.flightNum,
      review: data.review,
      phoneNum: data.phoneNum
    })
      .then(res => {
        console.log(res.data);
      })
  }
  return (
    <div>
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

      <div className='container'>

        <h1 className='header'>
          Write Your Review
        </h1>
        <div className='sub_form'>
          <form onSubmit={(e) => { handleSubmit(e); submit(e); }}>
            <div>
              <label>Title: <br /></label>
              <input onChange={(e) => handle(e)} id="title" value={data.title} placeholder='Title' type="text" className='input_field Title'></input>
            </div>
            <div>
              <label>Phone Number:</label>
              <br />
              <input onChange={(e) => { handle(e); }} id="phonenum" value={data.phonenum} placeholder='xxx-xxx-xxxx' type="text" pattern='[0-9]{3}[0-9]{3}[0-9]{4}' className='input_field Phone' maxLength={10} ></input>
            </div>
            <div>
              <label>Flight Number:</label><span> *</span>
              <br />
              <input onChange={(e) => { handle(e); setFlight(e.target.value); }} id="flightNum" value={data.flightNum} placeholder='Flight Number' type="text" pattern='[A-Z]{2}[0-9]{4}' className='input_field Flight' maxLength={6} required></input>
              {(error === true) ?
                <label className='error'>Flight needs to be specified! <br />Example: AA1234</label> : ""}
            </div>
            <div>
              <label>Review:</label> <span> *</span>
              <br />
              <input onChange={(e) => { handle(e); setReview(e.target.value); }} id="review" value={data.review} placeholder='Review' type="text" className='input_field Review' required></input>
              {ReviewError && Review.length <= 0 ?
                <label className='error'>Review needs to be entered!</label> : ""}
            </div>
            <button className='btn' onChange={(e) => handleSubmit(e)} onClick={(e) => { handleSubmit(e) }}> Submit</button>
            {/* {error&&Flight?"hello":"no error"} */}
          </form>
        </div>
				</form>
			</div>
		</div>
	);
};

export default Create;

	