import React from 'react'


const UserItem = ({item}) => {
    return (
        <tr>
            <td>{item.username}</td>
            <td>{item.first_name}</td>
            <td>{item.last_name}</td>
            <td>{item.email}</td>
        </tr>
    )
}

const UserList = ({items}) => {
    return (
        <table>
            <tr>
            <th>NICK</th>
            <th>FIRST NAME</th>
            <th>LAST NAME</th>
            <th>EMAIL</th>
            </tr>
            {items.map((item) => <UserItem item={item} />)}
        </table>
    )
}

export default UserList