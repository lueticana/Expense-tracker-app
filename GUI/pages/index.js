import Head from 'next/head';
import styles from '../styles/Home.module.css';
import Link from 'next/link';


export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Expense tracker</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1 className={styles.title}>
          Welcome to your expense tracker!
        </h1>

        <p className={styles.description}>
          Go to 
          </p>
          <p className={styles.description}>
          <Link href="/profile">
            <button style={{ padding: "10px 20px", cursor: "pointer" }}>
            my profile
            </button>
        </Link>
        </p>
        <p className={styles.description}>
        <Link href="/groups">
            <button style={{ padding: "10px 20px", cursor: "pointer" }}>
            my groups
            </button>
        </Link>
        </p>
        <p className={styles.description}>
        <Link href="/expenses">
            <button style={{ padding: "10px 20px", cursor: "pointer" }}>
            my expenses
            </button>
        </Link>
        </p>
        <p className={styles.description}>
        <Link href="/analysis">
            <button style={{ padding: "10px 20px", cursor: "pointer" }}>
            analysis
            </button>
        </Link>
        </p>

        
      </main>


      <style jsx>{`
        main {
          padding: 5rem 0;
          flex: 1;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
        }
        footer {
          width: 100%;
          height: 100px;
          border-top: 1px solid #eaeaea;
          display: flex;
          justify-content: center;
          align-items: center;
        }
        footer img {
          margin-left: 0.5rem;
        }
        footer a {
          display: flex;
          justify-content: center;
          align-items: center;
          text-decoration: none;
          color: inherit;
        }
        code {
          background: #fafafa;
          border-radius: 5px;
          padding: 0.75rem;
          font-size: 1.1rem;
          font-family:
            Menlo,
            Monaco,
            Lucida Console,
            Liberation Mono,
            DejaVu Sans Mono,
            Bitstream Vera Sans Mono,
            Courier New,
            monospace;
        }
      `}</style>

      <style jsx global>{`
        html,
        body {
          padding: 0;
          margin: 0;
          font-family:
            -apple-system,
            BlinkMacSystemFont,
            Segoe UI,
            Roboto,
            Oxygen,
            Ubuntu,
            Cantarell,
            Fira Sans,
            Droid Sans,
            Helvetica Neue,
            sans-serif;
        }
        * {
          box-sizing: border-box;
        }
      `}</style>
    </div>
  );
}
