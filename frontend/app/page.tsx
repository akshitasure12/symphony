import React from 'react';
import { Montserrat } from 'next/font/google';
import P1 from './components/P1';
import P2 from './components/P2';
import P3 from './components/P3';

const montserrat = Montserrat({ 
  subsets: ['latin'], 
  weight: ['600'],
});

export default function Home() {
  return (
    <div className="min-h-screen w-full">
      <P1 />
      <P2 />
      <P3 />
    </div>
  );
}
