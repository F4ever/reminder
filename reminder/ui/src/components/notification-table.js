import React, {Component} from 'react';
import {withRouter} from "react-router-dom";
import {json, processResponse, getCookie} from "../utils";
import Button from "react-bootstrap/Button";
import NotificationForm from "./notification-form";


class NotificationTable extends Component {
    constructor(props){
        super(props);

        this.state = {
            notifications: [],
            addNotification: false,
            notification: {},
        };

        this.getNotifications = this.getNotifications.bind(this);

        this.getNotifications();
    }

    notificationPopup(notification){
        this.setState({
            notification: notification,
            addNotification: true,
        })
    }

    closePopup(){
        this.setState({addNotification: false});
        this.getNotifications();
    }

    getNotifications(){
        const { history } = this.props;

        console.log('asd')

        fetch('/api/v1/notifications/')
            .then(processResponse)
            .then(json)
            .then((response)=>this.setState({notifications: response.results}))
            .catch(()=>history.push('/login/'))
    }

    async delete(id){
        const response = await fetch(
            `/api/v1/notifications/${id}/`,
            {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json;charset=utf-8',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            }
        );

        if (response.status >= 200 && response.status < 300){
            this.getNotifications()
        }else{
            const body = await response.json();
            window.alert(JSON.stringify(body));
        }
    }

    edit(notification){
        this.setState({
            notification: notification,
            addNotification: true,
        })
    }

    render(){
        const {notifications, addNotification, notification} = this.state;

        return (
            <div className={"notify-table"}>
                {/*<div>Notifications</div>*/}
                <Button variant="primary" style={{margin: '30px'}} onClick={()=>this.notificationPopup(null)}>Add notification</Button>
                <table style={{width: '800px'}}>
                    <thead>
                    <tr>
                        <td>
                            head
                        </td>
                        <td>
                            body
                        </td>
                        <td>
                            date
                        </td>
                        <td>
                            edit
                        </td>
                        <td>
                            delete
                        </td>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        notifications.map((notify)=>
                            <tr>
                                <td>{notify.head}</td>
                                <td>{notify.body}</td>
                                <td>{notify.date}</td>
                                <td onClick={()=>this.edit(notify)} style={{cursor: 'pointer'}}>Edit</td>
                                <td onClick={()=>this.delete(notify.id)} style={{cursor: 'pointer'}}>Delete</td>
                            </tr>
                        )
                    }
                    </tbody>
                </table>
                {
                    addNotification&&<NotificationForm notification={notification} close={this.closePopup.bind(this)}/>
                }
            </div>
        )
    }
}


export default withRouter(NotificationTable);