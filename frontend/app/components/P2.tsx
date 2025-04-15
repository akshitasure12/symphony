import React from "react";
import { Montserrat } from 'next/font/google';
import styles from '../styles/homePage.module.css';
import {PianoIcon, BrainIcon, HeartIcon} from "./icons";

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['400', '600'],
});

const P2 = () => (
  <section className={`${styles.p2Container} ${montserrat.className}`}>
    <div className={styles.p2Content}>
      <h2 className={styles.p2Heading}>Music was never<br />out of reach.</h2>
      <div className={styles.p2Description}>
        <p>Symphony reimagines how we play.</p>
        <p>No instruments. No barriers. Just pure expression.</p>
        <p>In every scale, in every sound.</p>
      </div>
      
      <div className={styles.featureCards}>
        <div className={styles.featureCard}>
          <div className={styles.featureIcon}>
            <PianoIcon />
          </div>
          <h3>Play Freely</h3>
          <p>Choose from X instruments, no skills required.</p>
        </div>
        
        <div className={styles.featureCard}>
          <div className={styles.featureIcon}>
            <BrainIcon />
          </div>
          <h3>Intuitive Feel</h3>
          <p>Built for humans, not musicians.</p>
        </div>
        
        <div className={styles.featureCard}>
          <div className={styles.featureIcon}>
            <HeartIcon />
          </div>
          <h3>Accessible for All</h3>
          <p>Designed for everyone - especially those who can't play traditionally.</p>
        </div>
      </div>
    </div>
  </section>
);

export default P2; 