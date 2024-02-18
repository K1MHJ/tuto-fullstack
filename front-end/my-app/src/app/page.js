"use client";

import Cookies from 'js-cookie';
import { useState, useEffect } from 'react';

export default function Home() {
  const [csrfToken, setCsrfToken] = useState('');

  // 서버에서 CSRF 토큰을 가져옵니다.
  async function fetchCsrfToken(){
    let response = await fetch('http://127.0.0.1:8000/csrf/',{
      method: 'GET',
      headers:{
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      credentials: 'include',
      mode: 'cors'
    });
    let parseResponse = await response.json();
    setCsrfToken(parseResponse.token);
  } 

  useEffect(() => {
    fetchCsrfToken();
  }, [])

  async function postData(){
    const url = 'http://127.0.0.1:8000/api/index/';
    let data = {
      // Your POST request data
      a:1,
      b:2,
    };
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(data),
        credentials: 'include',
      }).then((res)=>res.json()).then(console.log).catch(console.error);
    } catch (error) {
      // Handle error
    }
  };
  return (
    <main>
      <div>
        <button onClick={postData}>Submit</button>
      </div>
    </main>
  );
}
