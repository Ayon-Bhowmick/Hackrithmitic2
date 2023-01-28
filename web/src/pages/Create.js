import React, { useState } from 'react';

function InputBox() {
  const [value, setValue] = useState('');

  function handleChange(event) {
    setValue(event.target.value);
  }

  return (
    <div>
      <h1>
        Submit Review
      </h1>
      <div>
        <form>
          <input placeholder='Title' type="text"></input>
        </form>
        <form>
          <input placeholder='flight Number' type="text"></input>
        </form>
        <form>
          <input placeholder='review' type="text"></input>
        </form>
      </div>
    </div>
  );
}

export default InputBox;