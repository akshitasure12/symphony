import React from 'react';
import { Montserrat } from 'next/font/google';
import styles from '../styles/aboutPage.module.css';
import Header from '../components/Header';
import Footer from '../components/Footer';

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['400', '600'],
});

export default function About() {
  return (
    <main className={`${styles.container} ${montserrat.className}`}>
      <Header />
      <Footer />
    </main>
  );
} 