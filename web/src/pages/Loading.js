import React from 'react'
import "./Home.css";

function Loading() {

    return (
        <div className='load_container'>
        <div class="loader"></div>
        <div className='marker'> 
            Waiting to Load...
        </div>
        </div>
    )
}

export default Loading;
