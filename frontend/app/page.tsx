import React from "react";
import { Montserrat } from 'next/font/google';
import P1 from './components/P1';

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['600'],
});

export default function Home() {
  return (
    <P1 />
  );
}
