import React, { useState } from 'react';
import Axios from 'axios'
function InputBox() {
  
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
      <h1>
        Write Your Review
      </h1>
      <div>
        <form onSubmit={(e)=>submit(e)}>
          <div>
          <input onChange={(e)=>handle(e)} id="title" value={data.title} placeholder='Title' type="text"></input>
          </div>
          <div>
            <input onChange={(e)=>handle(e)} id="flightNum" value={data.flightNum} placeholder='Flight Number' type="text"></input>
          </div>
          <div>
            <input onChange={(e)=>handle(e)} id="review" value={data.review} placeholder='Review' type="text"></input>
          </div>
          <button>Submit</button>
        </form>
      </div>
    </div>
  );
}

export default InputBox;