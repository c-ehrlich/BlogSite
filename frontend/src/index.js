import React from "react";
import ReactDOM from "react-dom";
// import * as serviceWorker from "./serviceWorker"; // for the app to work offline
import "./index.css";
import { Route, BrowserRouter as Router, Switch } from "react-router-dom";
import App from "./App";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Login from "./components/Login";
import Logout from "./components/Logout";
import Register from "./components/Register";
import Single from "./components/Single";

const routing = (
  <Router>
    <React.StrictMode>
      <Header />
      <Switch>
        <Route exact path="/" component={App} />
        <Route path="/register" component={Register} />
        <Route path="/login" component={Login} />
        <Route path="/logout" component={Logout} />
        <Route path="/post/:slug" component={Single} />
      </Switch>
      <Footer />
    </React.StrictMode>
  </Router>
);

ReactDOM.render(routing, document.getElementById("root"));
