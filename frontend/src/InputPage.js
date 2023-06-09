import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './InputPage.css'

const InputPage = () => {
    const [responseData, setResponseData] = useState(null);
    const [prompt, setPrompt] = useState()
    const [loading, setIsLoading] = useState()


const handleCreateArt = async (e) => {
    e.preventDefault()
  try {
    const response = await axios.post(
      '/create-art', // Replace with your Flask backend URL
      {
        prompt
      }
    );

    setResponseData(response.data);
    await setIsLoading(true)


    if (response.status == 200) {
        await setIsLoading(false)
    }

  } catch (error) {
    console.error('Error:', error);
  }
};


console.log(loading)


  return (
    <div className='page-wrapper'>
        <h1>Generate an image.</h1>
        <h2>Save it forever.</h2>
        <form className='text-input-form'>
            <textarea id='prompt-input' placeholder='Enter prompt...'
            onChange={(e) => setPrompt(e.target.value)}
            value={prompt}
            />

             <input

            type="submit"
            value={"Generate"}
            onClick={handleCreateArt}
          />
        </form>
        {!loading ? <img src={responseData?.output[0]} alt=''/> : <h3>Image loading</h3>}
    </div>
  )
}

export default InputPage