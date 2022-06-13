import React from 'react'

function Menu(props) {
    return (
    <div>
    <ul id="navbar">
        <li><a href="#">Главная</a></li>
        <li><a href="#">Записки</a>
            <ul>
                <li><a href="#">Список задач</a></li>
                <li><a href="#">Авторы</a></li>
            </ul>
        </li>
    </ul>
    </div>
    )
}


export default Menu