import React, { useState } from 'react';
import Logo from './images/logo.png';
import { Link } from "react-router-dom";
import Axios from 'axios'
import './Home.css'
import './CreateReview.css'

function InputBox() {
  
  const [Flight, setFlight] = useState('');
  const [Review, setReview] = useState('');
  const [error, setError] = useState(false);

  function handleSubmit(e){
    console.log('entered');
    e.preventDefault();
    if(Flight.length === 0 || Review.length === 0){
      setError(true);
    }
    if(Flight&&Review){
      console.log('flight: ', Flight, '\nReview ', Review);
    }

  }
  

  const url = ""
  const [data, setData]=useState({
    title: "",
    flightNum: "",
    review:""
  })


  function handle(e){
    const newdata={...data}
    newdata[e.target.id]=e.target.value
    setData(newdata)
    console.log(newdata)
  }

  function submit(e){
    e.preventDefault();
    Axios.post(url,{
      title: data.name,
      flightNum: data.flightNum,
      review: data.review
    })
    .then(res=>{
      console.log(res.data)
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
          <form onSubmit={(e)=>{submit(e); handleSubmit(e)}}>
            <div>
            <label>Title: <br/></label>            
            <input onChange={(e)=>handle(e)} id="title" value={data.title} placeholder='Title' type="text" className='input_field Title'></input>
            </div>
            <div>
              <label>Flight Number:</label><span> *</span>
              <br/>
              <input onChange={(e)=>{handle(e); setFlight(e.target.value);}} id="flightNum" value={data.flightNum} placeholder='Flight Number' type="text" pattern='[A-Z]{2}[0-9]{4}' className='input_field Flight' maxLength={6} required></input>
              {Flight.length>0? 
              <label>Flight needs to be specified!</label>:""}
            </div>
            <div>
            <label>Review:</label> <span> *</span>
              <br/>
              <input onChange={(e)=>{handle(e); setReview(e.target.value);}} id="review" value={data.review} placeholder='Review' type="text" className='input_field Review' required></input>
            </div>
            <button className='btn'  > Submit</button>
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