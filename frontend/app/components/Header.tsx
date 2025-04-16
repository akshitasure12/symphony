import React from 'react';
import Link from 'next/link';
import styles from '../styles/homePage.module.css';

const Header = () => (
  <header className={styles.header}>
    <Link href="/" className={styles.logo}>symphony</Link>
    <nav className={styles.nav}>
      <Link href="/" className={styles.navLink}>play music</Link>
      <Link href="/aboutus" className={styles.navLink}>about us</Link>
    </nav>
  </header>
);

export default Header;