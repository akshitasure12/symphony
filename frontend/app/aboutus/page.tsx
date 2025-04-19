import React from 'react';
import { Montserrat } from 'next/font/google';
import styles from '../styles/aboutPage.module.css';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { AboutUsBackdrop } from '../components/icons';

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['400', '600'],
});

export default function About() {
  return (
    <main className={`${styles.container} ${montserrat.className}`}>
      <Header />
      <section className={styles.aboutSection}>
        <div className={styles.backdropContainer}>
          <AboutUsBackdrop />
        </div>
        <div className={styles.content}>
          <h1 className={styles.heading}>About Us</h1>
          <div className={styles.description}>
            <p>Symphony reimagines how we interact with music. Our innovative platform breaks down traditional barriers to musical expression, making it accessible to everyone.</p>
          </div>
        </div>
      </section>
      <Footer />
    </main>
  );
} 