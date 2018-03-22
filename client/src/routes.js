import App from './App'
import Login from 'views/login'

let routes = [{
	path: '/',
	component: App,
	meta: {requiresAuth: true},
	name: 'home',
	children: []
}, {
	path: '/login',
	component: Login
}]

export default routes
