import React from 'react';
import './App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Login from "./components/login";
import Register from "./components/register";
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
      <div className="App">
        <BrowserRouter>
          <Switch>
            <Route path='/login' component={Login}/>
            <Route path='/register' component={Register}/>
            {/**/}
            {/*<Route exact path='/' component={NotificationTabel}/>*/}
            {/*<Route path='/notification' component={Notification}/>*/}
            {/*<Route path='/notification/:number' component={Notification}/>*/}
          </Switch>
        </BrowserRouter>
      </div>
  );
}

export default App;
