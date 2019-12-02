import React, { Component } from "react";
import {Button, Form, FormControl, InputGroup} from "react-bootstrap";
import {useHistory, withRouter} from "react-router-dom";


class Register extends Component {

  constructor(props){
    super(props);

    this.state = {
      email: '',
      password: ''
    }
  }

  render() {
    const { history } = this.props;

    return (
        <div className="Login">
          <b>Register Form</b>
          <br/>
          <br/>
          <Form>
            <Form.Group controlId="formBasicEmail">
              <Form.Label>Email address</Form.Label>
              <Form.Control type="email" placeholder="Enter email" />
            </Form.Group>

            <Form.Group controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" placeholder="Password" />
            </Form.Group>

            <Form.Group controlId="formBasicEmail">
              <Form.Label>Nickname</Form.Label>
              <Form.Control placeholder="Enter nickname" />
            </Form.Group>

            <Button variant="primary" type="submit">
              Submit
            </Button>
            <div style={{margin: '10px'}}>
              <a style={{cursor: 'pointer'}} onClick={() => history.push("/login")}>Login</a>
            </div>
          </Form>
        </div>
    );
  }
}


export default withRouter(Register);
