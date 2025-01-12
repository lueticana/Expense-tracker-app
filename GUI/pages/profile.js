import React, { useEffect, useState } from "react"
import Link from 'next/link';

export default function MyProfile() {

    const [data, setData] = useState([{}])
    
        useEffect(() => {
            fetch("http://localhost:5000/profile"
            ).then(
                res => res.json()
            ).then(
                data => {
                    setData(data)
                    console.log(data)
                }
            )
        }, [])


    return (
    <>
    <h1>My profile</h1>
    <div>
        {data.message}
    </div>
    <h2>
        <Link href="/">Back to home</Link>
    </h2>
    </>
    );
  }