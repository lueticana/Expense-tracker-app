import React, { useEffect, useState } from "react"
import Link from 'next/link';
import styles from '../styles/Home.module.css';

export default function MyExpenses() {

    const [data, setData] = useState([{}])
    
        useEffect(() => {
            fetch("http://localhost:5002/"
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
    <h1>My expenses</h1>
    <div>
        {data.message}
    </div>
    <p className={styles.description}>
        <Link href="/add_expense">
            <button style={{ padding: "10px 20px", cursor: "pointer" }}>
            add expense
            </button>
        </Link>
        </p>
    <h2>
        <Link href="/">Back to home</Link>
    </h2>
    </>
    );
  }