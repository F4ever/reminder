import React, {Component} from 'react';
import {Form, Button} from "react-bootstrap";
import UserList from "./user-list";
import {getCookie} from '../utils';


class NotificationForm extends Component {
    constructor(props) {
        super(props);

        const {notification} = this.props;

        if (notification){
            this.state = {
                id: notification.id,
                head: notification.head,
                body: notification.body,
                place: notification.place,
                date: notification.date,
                participators: notification.participators
            }
        }
        else{
            this.state = {
                id: null,
                head: '',
                body: '',
                place: '',
                date: '',
                participators: []
            }
        }
    }

    async saveAndClose() {
        const {close} = this.props;
        const {
            id,
            head,
            body,
            place,
            date,
            participators,
        } = this.state;

        // Save
        const response = await fetch(
            `/api/v1/notifications/${ id ? id + '/': '' }`,
            {
                method: id?'PATCH':'POST',
                body: JSON.stringify({
                    head: head,
                    body: body,
                    place: place,
                    date: date,
                    participators: participators,
                }),
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            }
        );

        if (response.status >= 200 && response.status < 300){
            close();
        }else{
            const body = await response.json();
            window.alert(JSON.stringify(body));
        }
    }

    choose(ids){
        this.setState({
            participators: ids
        })
    }

    render(){
        const {close} = this.props;
        const {head, body, place, date, participators} = this.state;

        return (
            <div className={'popup'}>
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Head</Form.Label>
                    <Form.Control
                        placeholder="Head"
                        value={head}
                        onChange={(e)=>this.setState({'head': e.target.value})}
                    />
                </Form.Group>
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Body</Form.Label>
                    <Form.Control
                        placeholder="Body"
                        value={body}
                        onChange={(e)=>this.setState({'body': e.target.value})}
                    />
                </Form.Group>
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Place</Form.Label>
                    <Form.Control
                        placeholder="Place"
                        value={place}
                        onChange={(e)=>this.setState({'place': e.target.value})}
                    />
                </Form.Group>
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Date YYYY-MM-DDTHH:MM<br/>(example 2019-11-25T13:33)</Form.Label>
                    <Form.Control
                        placeholder="DateTime"
                        value={date}
                        onChange={(e)=>this.setState({'date': e.target.value})}
                    />
                </Form.Group>
                <br/>
                <UserList users={participators} change={(ids)=>this.choose(ids)}/>
                <br/>
                <Button onClick={()=>close()}>Close</Button>
                <br/>
                <br/>
                <Button onClick={()=>this.saveAndClose()}>Save</Button>
            </div>
        )
    }
}


export default NotificationForm;