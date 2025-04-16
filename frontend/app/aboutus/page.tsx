import React from 'react';
import { Montserrat } from 'next/font/google';
import styles from '../styles/aboutPage.module.css';
import Header from '../components/Header';

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['400', '600'],
});

export default function About() {
  return (
    <main className={`${styles.container} ${montserrat.className}`}>
      <Header />
      <section className={styles.aboutSection}>
        <div className={styles.content}>
          <h1 className={styles.heading}>About Symphony</h1>
          <div className={styles.description}>
            This is where we talk about us.
          </div>
        </div>
      </section>
    </main>
  );
} 