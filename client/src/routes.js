import App from './App'
import Login from 'views/login'

import EventsList from 'views/events'
import NewEvent from 'views/events/new'
import Event from 'views/events/item'

let routes = [{
	path: '/',
	component: App,
	meta: {requiresAuth: true},
	name: 'home',
	children: [{
		path: '/',
		name: 'events:list',
		component: EventsList
	}, {
		path: 'events/new',
		name: 'events:new',
		component: NewEvent
	}, {
		path: 'events/:id',
		name: 'events:item',
		component: Event,
		props: true
	}]
}, {
	path: '/login',
	component: Login
}]

export default routes
