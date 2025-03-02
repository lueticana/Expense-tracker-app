import React, { useEffect, useState } from "react"
import Link from 'next/link';

export default function Analysis() {

    const [data, setData] = useState([{}])
    
        useEffect(() => {
            fetch("http://localhost:5003/"
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
    <h1>Analysis</h1>
    <div>
        {data.message}
        TO DO
    </div>
    <h2>
        <Link href="/">Back to home</Link>
    </h2>
    </>
    );
  }