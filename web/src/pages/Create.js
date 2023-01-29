import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Logo from './images/logo.png';
import { Link } from "react-router-dom";
import Axios from 'axios'
import './Home.css'
import './CreateReview.css'
import axios from 'axios';

function InputBox() {

  const [Flight, setFlight] = useState('');
  const [Review, setReview] = useState('');
  let [error, setError] = useState(false);
  let [ReviewError, setReviewError] = useState(false);

  function handleSubmit(e) {
    e.preventDefault();
    let regex = /^[A-Z]{2}[0-9]{4}$/g;
    let found = Flight.match(regex);
    console.log('Found: ', found);

    if (found == null) {
      setError(true);
    }
    if (Review.length === 0) {
      setReviewError(true);
    }
    else {
      setError(false);
    }
    // if (Flight && Review) {
      // console.log('Flight: ', Flight, '\nReview: ', Review);
    // }

  }


  const url = "https://sky-scout.onrender.com/postreview";
  // const [data, setData] = useState({
  //   title: "",
  //   // flight_number: "",
  //   // message: "",
  //   // phonenumber: "",
  // })
////////////////////////////////////////////////////////////////
  const [title, setTitle] = useState();
  const [message, setMessage] = useState();
  const [flightnumber, setFlightNumber] = useState();
  const [phonenumber, setPhonenumber] = useState();

  const doFetech = async(e)=>{
    e.preventDefault();
    await axios.post("https://127.0.0.1:8000/postreview",{
      title,
      message,
      flightnumber,
      phonenumber,
    })
    .then(response=>{
      console.log(response.data);
    })
    .catch(error =>{
      console.log(error);
    });

  }

  let navigate = useNavigate();
  const routeChange = ()=>{
    let path = '/';
    navigate(path);
  }
  

///////////////////////////////////////////


  // function handle(e) {
  //   const newdata = { ...data }
  //   newdata[e.target.id] = e.target.value
  //   setData(newdata)
  //   // console.log(newdata)
  // }

  // function submit(e) {
  //   e.preventDefault();
  //   Axios.post(url, {
  //     title: data.name,
  //     flight_number: data.flight_number,
  //     message: data.message,
  //     phone_number: data.phonenumber,
  //   })
  //     .then(res => {
  //       console.log(res.data);
  //     })
  // }
  
  return (
    <div>
      <nav>
        <img id="logo" src={Logo} alt="SkyScout" />

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
          <form onSubmit={(e) => doFetech}>
            <div>
              <label>Title: <br /></label>
              <input onChange={(e) => setTitle(e.target.value)} id="title" placeholder='Title' type="text" className='input_field Title'></input>
            </div>
            <div>
              <label>Phone Number:</label>
              <br />
              <input onChange={(e) => setPhonenumber(e.target.value)} id="phonenum"  placeholder='xxx-xxx-xxxx' type="text" pattern='[0-9]{3}[0-9]{3}[0-9]{4}' className='input_field Phone' maxLength={10} ></input>
            </div>
            <div>
              <label>Flight Number:</label><span> *</span>
              <br />
              <input onChange={(e) => setFlightNumber(e.target.value)} id="flightNum"  placeholder='Flight Number' type="text" pattern='[A-Z]{2}[0-9]{4}' className='input_field Flight' maxLength={6} required></input>
              {(error === true) ?
                <label className='error'>Flight needs to be specified! <br />Example: AA1234</label> : ""}
            </div>
            <div>
              <label>Review:</label> <span> *</span>
              <br />
              <input onChange={(e) => setMessage(e.target.value)} id="review"  placeholder='Review' type="text" className='input_field Review' required></input>
              {ReviewError && Review.length <= 0 ?
                <label className='error'>Review needs to be entered!</label> : ""}
            </div>
            <button className='btn' onChange={(e) => handleSubmit(e)} onClick={(e) => { doFetech(e); routeChange(); }}> Submit</button>
            {/* {error&&Flight?"hello":"no error"} */}
          </form>
        </div>
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

export default InputBox;