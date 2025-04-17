import React from 'react';
import Link from 'next/link';
import { Montserrat } from 'next/font/google';
import styles from '../styles/footer.module.css';

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['400', '600'],
});

const Footer = () => (
  <footer className={`${styles.footer} ${montserrat.className}`}>
    <div className={styles.footerContent}>
      <div className={styles.footerSection}>
        <h3 className={styles.footerTitle}>Symphony</h3>
        <p className={styles.footerDescription}>
          Making music accessible to everyone through innovative technology.
        </p>
      </div>
      
      <div className={styles.footerSection}>
        <h4 className={styles.footerSubtitle}>Navigation</h4>
        <nav className={styles.footerNav}>
          <Link href="/" className={styles.footerLink}>Home</Link>
          <Link href="/aboutus" className={styles.footerLink}>About Us</Link>
          <Link href="/" className={styles.footerLink}>Play Music</Link>
        </nav>
      </div>
      
      <div className={styles.footerSection}>
        <h4 className={styles.footerSubtitle}>Contact</h4>
        <div className={styles.footerContact}>
          <a href="mailto:contact@symphony.com" className={styles.footerLink}>contact@symphony.com</a>
          <div className={styles.socialLinks}>
            <a href="#" className={styles.socialLink}>Twitter</a>
            <a href="#" className={styles.socialLink}>Instagram</a>
            <a href="#" className={styles.socialLink}>LinkedIn</a>
          </div>
        </div>
      </div>
    </div>
    <div className={styles.footerBottom}>
      <p className={styles.copyright}>© 2024 Symphony. All rights reserved.</p>
    </div>
  </footer>
);

export default Footer; 