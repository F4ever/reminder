import React, {Component} from "react";
import {Button, Form} from "react-bootstrap";
import {withRouter} from "react-router-dom";
import {getCookie} from '../utils';


class Register extends Component {

    constructor(props){
        super(props);

        this.state = {
            email: '',
            password: '',
            username: '',
        }
    }

    async register(){
        const { history } = this.props;
        const { email, password, username } = this.state;

        const response = await fetch(
            '/api-auth/register/',
            {
                method: 'POST',
                body: JSON.stringify({
                    email: email,
                    password: password,
                    username: username,
                }),
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            }
        );

        if (response.status >= 200 && response.status < 300){
            history.push('/')
        }else{
            const body = await response.json();
            window.alert(JSON.stringify(body));
        }
    }

    render() {
        const { history } = this.props;
        const { email, password, username } = this.state;

        return (
            <div className="Login">
                <b>Register Form</b>
                <br/>
                <br/>
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control
                        type="email"
                        placeholder="Enter email"
                        value={email}
                        onChange={(e)=>this.setState({'email': e.target.value})}
                    />
                </Form.Group>

                <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e)=>this.setState({'password': e.target.value})}
                    />
                </Form.Group>

                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Name</Form.Label>
                    <Form.Control
                        placeholder="Enter nickname"
                        value={username}
                        onChange={(e)=>this.setState({'username': e.target.value})}
                    />
                </Form.Group>

                <Button variant="primary" type="submit" onClick={this.register.bind(this)}>
                    Register
                </Button>
                <div style={{margin: '10px'}}>
                    <a style={{cursor: 'pointer'}} onClick={() => history.push("/login/")}>Login</a>
                </div>
            </div>
        );
    }
}


export default withRouter(Register);
