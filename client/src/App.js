// import logo from './logo.svg';
// import './App.css';
import React, { useState, useEffect } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Home from "./components/pages/Home";
import Login from "./components/pages/Login";
import Transfer from "./components/pages/Transfer";
import TransactionHistory from "./components/pages/TransactionHistory"
import Balance from "./components/pages/Balance"
import Header from "./components/layout/Header"
import UserContext from './context/UserContext.js'

export default function App() {
  const [userData, setUserData] = useState({                  
    token: undefined,       //store the JWT Token
    user: undefined        //store the user's data
  });

  return (
    <>
      <BrowserRouter>
      <UserContext.Provider value={{ userData, setUserData }}>
        <Header/>
        <div className="container">
          <Switch>
              <Route exact path ="/" component ={Home} />
              <Route path="/login" component={Login} />
          </Switch>
        </div>
        </UserContext.Provider> 
      </BrowserRouter>
      </>
  );
}
