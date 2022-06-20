import './App.css';
import React from 'react'
import {BrowserRouter, Route, Switch, Redirect, Link} from 'react-router-dom'
import LoginForm from './components/Auth.js'
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TodoList from './components/Todo.js'
import Footer from './components/Footer.js'
import axios from 'axios'
import Cookies from 'universal-cookie';



const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token})
    }
    is_authenticated() {
        return this.state.token !== ''
    }
    logout() {
        this.set_token('')
    }
    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token})
    }
    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

     constructor(props) {
        super(props)
            this.state = {
                'users': [],
                'projects': [],
                'tods': [],
                'token': ''
            }
    }
    load_data() {
        axios.get('http://127.0.0.1:8000/api/user/')
            .then(response => {
            const users = response.data
                this.setState({'users': users['results']})
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/project/')
            .then(response => {
            const projects = response.data
                this.setState({'projects': projects['results']})
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
            const tods = response.data
                this.setState({'tods': tods['results']})
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
        this.load_data()
    }


    render() {
        return (
            <div className="App">
                <BrowserRouter>
                <nav>
                    <ul id="navbar">
                        <li><Link to='/'>Главная</Link></li>
                        <li>
                            {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                        </li>
                        <li>Записки
                            <ul>
                                <li><Link to='/users'>Пользователи</Link></li>
                                <li><Link to='/projects'>Проекты</Link></li>
                                <li><Link to='/todo'>Список задач</Link></li>
                            </ul>
                        </li>
                    </ul>
                </nav>
                <Switch>
                    <Route exact path='/' />
                    <Route exact path='/users' component={() => <UserList items={this.state.users} />} />
                    <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} />} />
                    <Route exact path='/todo' component={() => <TodoList items={this.state.tods} />} />
                    <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                    <Redirect from='/tods' to='/todo' />
                    <Route component={NotFound404} />
                </Switch>
                </BrowserRouter>
                <Footer />
            </div>
        )
    }
}

export default App;
