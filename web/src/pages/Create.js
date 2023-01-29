import React, { useState } from 'react';
import Axios from 'axios'
import './CreateReview.css'

function InputBox() {
  
  const url = ""
  const [data, setData]=useState({
    title: "",
    flightNum: "",
    review:""
  })

  const changeLine = (event) =>{
    if(event.target.value.split(" ").length >=20){
      event.target.value = event.target.value + "\n";
    }
    this.setState({inputValue: event.target.value})
  }


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
    <div className='container'>
      <h1 className='header'>
        Write Your Review
      </h1>
      <div className='sub_form'>
        <form onSubmit={(e)=>submit(e)}>
          <div>
          <label>Title: <br/></label>            
          <input onChange={(e)=>handle(e)} id="title" value={data.title} placeholder='Title' type="text" className='input_field Title'></input>
          </div>
          <div>
            <label>Flight Number:</label><span>*</span>
            <br/>
            <input onChange={(e)=>handle(e)} id="flightNum" value={data.flightNum} placeholder='Flight Number' type="text" pattern='[A-Z]{2}[0-9]{4}' className='input_field Flight' maxLength={6} required></input>
          </div>
          <div>
          <label>Review:</label> <span>*</span>
            <br/>
            <input onChange={(e)=>handle(e)} id="review" value={data.review} placeholder='Review' type="text" className='input_field Review' required></input>
          </div>
          <button className='btn'>Submit</button>
        </form>
      </div>
    </div>
  );
}

export default InputBox;