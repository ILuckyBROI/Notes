import React from 'react'


const TodoItem = ({item}) => {
    return (
        <tr>
            <td>{item.project}</td>
            <td>{item.text}</td>
            <td>{item.create_date}</td>
            <td>{item.edit_date}</td>
            <td>{item.user_name}</td>
            <td>{item.status}</td>
        </tr>
    )
}

const TodoList = ({items}) => {
    return (
        <table>
            <tr>
            <th>Project</th>
            <th>Text</th>
            <th>Create Date</th>
            <th>Edit Date</th>
            <th>User</th>
            <th>Status</th>
            </tr>
            {items.map((item) => <TodoItem item={item} />)}
        </table>
    )
}

export default TodoList