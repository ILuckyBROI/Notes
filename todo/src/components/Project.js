import React from 'react'


const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>{item.title}</td>
            <td>{item.project_url}</td>
            <td>{item.user_name}</td>
        </tr>
    )
}
const ProjectList = ({items}) => {
    return (
        <table>
            <tr>
            <th>Title</th>
            <th>Project URL</th>
            <th>Users</th>
            </tr>
            {items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}
export default ProjectList
