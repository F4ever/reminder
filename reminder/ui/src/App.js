import React, {Component} from 'react';
import './App.css';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Login from "./components/login";
import Register from "./components/register";
import NotificationTable from "./components/notification-table";
import 'bootstrap/dist/css/bootstrap.min.css';


class App extends Component {

    render(){
        return (
            <div className="App">
                <BrowserRouter>
                    <Switch>
                        <Route exact path='/' component={NotificationTable}/>
                        <Route exact path='/login/' component={Login}/>
                        <Route exact path='/register/' component={Register}/>
                    </Switch>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;
