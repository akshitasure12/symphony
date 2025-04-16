import React from "react";
import { Montserrat } from 'next/font/google';
import styles from '../styles/homePage.module.css';
import {Guitar, Scale, Tap, Camera} from "./icons";

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['400', '600'],
});

const P3 = () => (
  <section className={`${styles.p3Container} ${montserrat.className}`}>
    <div className={styles.p3Content}>
      <div className={styles.p3TextContent}>
        <h2 className={styles.p3Heading}>How it works?</h2>
        <p className={styles.p3Description}>
          Symphony is aimed at making music fun for everyone. Here are a few easy steps to follow to experience this new musical dimension:
        </p>
      </div>
      
      <div className={styles.stepsContainer}>
        <div className={styles.step}>
          <div className={styles.stepIcon}>
            <Guitar />
          </div>
          <div className={styles.stepContent}>
            <h3>1. Choose an Instrument</h3>
            <p>Explore a curated collection of X+ expressive musical instruments.</p>
          </div>
        </div>

        <div className={styles.step}>
          <div className={styles.stepIcon}>
            <Scale />
          </div>
          <div className={styles.stepContent}>
            <h3>2. Pick a Scale</h3>
            <p>Explore preset scales, adapted for hand-tracking.</p>
          </div>
        </div>

        <div className={styles.step}>
          <div className={styles.stepIcon}>
            <Tap />
          </div>
          <div className={styles.stepContent}>
            <h3>3. See the Hand Gesture Guide</h3>
            <p>Learn chords - finger combinations with right- and left-hand diagrams.</p>
          </div>
        </div>

        <div className={styles.step}>
          <div className={styles.stepIcon}>
            <Camera />
          </div>
          <div className={styles.stepContent}>
            <h3>4. Show your Gestures</h3>
            <p>Grant camera permission and begin playing.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
);

export default P3; 