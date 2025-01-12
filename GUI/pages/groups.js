import React, { useEffect, useState } from "react"
import Link from 'next/link';

export default function MyGroups() {

    const [data, setData] = useState([{}])
    
        useEffect(() => {
            fetch("http://localhost:5001/groups"
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
    <h1>My groups</h1>
    <div>
        {data.message}
    </div>
    <h2>
        <Link href="/">Back to home</Link>
    </h2>
    </>
    );
  }