import React from "react";
import HeaderOptions from "../layout/HeaderOptions";

export default function Header() {
  return (
    <header id="header">
      <h1 className="title">DBS E-Wallet</h1>
      <HeaderOptions />
    </header>
  );
}