import React from "react";
import { Montserrat } from 'next/font/google';
import styles from '../styles/homePage.module.css';
import { LeftSquiggle, RightSquiggle, Headphones } from "./icons";

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['400', '600'],
});

const P4 = () => (
  <section className={`${styles.p4Container} ${montserrat.className}`}>
    <div className={styles.p4Content}>
      <h2 className={styles.p4Heading}>Ready to Create?</h2>
      <div className={styles.p4Description}>
        <p>Unlock a new way to connect with music.</p>
        <p>Join a growing movement of creators, hobbyists, and dreamers.</p>
      </div>
      
      <div className={styles.soundWaveContainer}>
        <LeftSquiggle />
        <button className={styles.startButton}>
        <Headphones />
          <span>start your </span>
          <span className={styles.p4symphonyText}>Symphony</span>
        </button>
        <RightSquiggle />
      </div>
    </div>
  </section>
);

export default P4; 