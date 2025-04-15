import React from 'react';
import styles from '../styles/homePage.module.css';

const Header = () => (
  <header className={styles.header}>
    <h1 className="text-xl font-light">symphony</h1>
    <nav className={styles.nav}>
      <a href="#" className={styles.navLink}>play music</a>
      <a href="#" className={styles.navLink}>about us</a>
    </nav>
  </header>
);

export default Header;