import React from "react";
import { Montserrat } from 'next/font/google';
import styles from '../styles/homePage.module.css';
import {Guitar, Scale, Tap, Camera, BackgroundDetail} from "./icons";

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['400', '600'],
});

const P3 = () => (
  <section className={`${styles.p3Container} ${montserrat.className}`}>
    <div className={styles.backgroundDetails}>
      {[...Array(6)].map((_, index) => (
        <div 
          key={index} 
          className={styles.backgroundDetail} 
          style={{ left: `calc(98px + (80vw - 40px) / 5 * ${index})` }}
        >
          <BackgroundDetail />
          {index === 3 && (
            <div 
              className={styles.overlappingDetail}
              style={{ 
                position: 'absolute',
                left: '890.88px',
                width: '126.82px',
                height: '862.13px',
                transform: 'rotate(-7deg)',
                border: '5px solid',
                borderImage: 'linear-gradient(to bottom, #84592B 0%, #9D9167 100%) 1'
              }}
            >
              <BackgroundDetail />
            </div>
          )}
        </div>
      ))}
    </div>
    <div className={styles.p3Content}>
      <div className={styles.p3TextContent}>
        <h2 className={styles.p3Heading}>How it works?</h2>
        <p className={styles.p3Description}>
          Symphony is aimed at making music fun for everyone. Here are a few easy steps to follow to experience this new musical dimension:
        </p>
      </div>
      
      <div className={styles.stepsContainer}>
        <div className={styles.step}>
          <div className={styles.stepIconContainer}>
            <div className={styles.stepIcon}>
              <Guitar />
            </div>
          </div>
          <div className={styles.stepContent}>
            <h3>1. Choose an Instrument</h3>
            <p>Explore a curated collection of X+ expressive musical instruments.</p>
          </div>
        </div>

        <div className={styles.step}>
          <div className={styles.stepIconContainer}>
            <div className={styles.stepIcon}>
              <Scale />
            </div>
          </div>
          <div className={styles.stepContent}>
            <h3>2. Pick a Scale</h3>
            <p>Explore preset scales, adapted for hand-tracking.</p>
          </div>
        </div>

        <div className={styles.step}>
          <div className={styles.stepIconContainer}>
            <div className={styles.stepIcon}>
              <Tap />
            </div>
          </div>
          <div className={styles.stepContent}>
            <h3>3. See the Hand Gesture Guide</h3>
            <p>Learn chords - finger combinations with right- and left-hand diagrams.</p>
          </div>
        </div>

        <div className={styles.step}>
          <div className={styles.stepIconContainer}>
            <div className={styles.stepIcon}>
              <Camera />
            </div>
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