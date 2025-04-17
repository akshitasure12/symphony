import React from "react";
import { Montserrat } from 'next/font/google';
import styles from '../styles/homePage.module.css';
import Header from './Header';

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['600'],
});

const P1 = () => (
  <main className={`${styles.container} ${montserrat.className}`}>
    <Header />
    <section className={styles.mainSection}>
      <div className={styles.contentContainer}>
        <div className="absolute inset-0 overflow-visible" aria-hidden="true">
          {[...Array(5)].map((_, i) => (
            <div
              key={i}
              className={styles.decorativeLine}
              style={{ top: `${i * 100}px` }}
            />
          ))}
        </div>
        <div className={styles.contentWrapper}>
          <div className="relative">
            <h2 className={styles.playText}>play</h2>
            <h2 className={styles.yourOwnText}>your own</h2>
            <h1 className={styles.symphonyText}>symphony</h1>
            <button className={styles.tryNowButton}>try now</button>
          </div>
        </div>
      </div>
    </section>
  </main>
);

export default P1; 