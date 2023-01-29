import React, { useState } from 'react';
import Logo from './images/logo.png';
import { Link } from "react-router-dom";
import Axios from 'axios'
import './Home.css'
import './CreateReview.css'

function InputBox() {

  const [Flight, setFlight] = useState('');
  const [Review, setReview] = useState('');
  let [error, setError] = useState(false);
  let [ReviewError, setReviewError] = useState(false);

  function handleSubmit(e) {
    console.log('entered');
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
    if (Flight && Review) {
      console.log('Flight: ', Flight, '\nReview: ', Review);
    }

  }


  const url = ""
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
    console.log(newdata)
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
        console.log(res.data)
      })
  }
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