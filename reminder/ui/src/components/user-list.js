import React, {Component} from 'react';
import {Button, InputGroup} from "react-bootstrap";
import {json} from "../utils";


export default class UserList extends Component{
    constructor(props){
        super(props);

        this.checkUser = this.checkUser.bind(this);

        this.state = {
            users: [],
            userSelectedIds: props.users,
        };

        fetch('/api/v1/users/').then(json).then((res)=>this.setState({users: res['results']}));
    }

    checkUser(id){
        const {userSelectedIds} = this.state;

        let mute = userSelectedIds.slice();

        let index = userSelectedIds.indexOf(id);

        if (index > -1){
            mute.splice(index, 1);
        }else{
            mute.push(id);
        }

        this.props.change(mute);
        this.setState({userSelectedIds: mute});
    }

    render(){
        const {users, userSelectedIds} = this.state;

        return (
            <div>
                Select Users
                <div>
                    {
                        users.map(user=>(
                            <div style={{display: 'flex', justifyContent: 'space-between'}} key={user.id}>
                                <InputGroup.Checkbox
                                    checked={userSelectedIds.indexOf(user.id) !== -1}
                                    onClick={()=>this.checkUser(user.id)}
                                />
                                <div>
                                    {user.username}
                                </div>
                                <div>
                                    {user.email}
                                </div>
                            </div>
                        ))
                    }
                </div>
            </div>
        )
    }
}