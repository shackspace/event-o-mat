import App from './App'
import Login from 'views/login'

import EventsList from 'views/events'
import Event from 'views/events/item'
import Calendar from 'views/calendar'

let routes = [{
	path: '/',
	component: App,
	children: [{
		path: '/',
		name: 'events:list',
		component: EventsList
	}, {
		path: 'events/new',
		name: 'events:new',
		component: Event,
		meta: {requiresAuth: true},
	}, {
		path: 'events/:id',
		name: 'events:item',
		component: Event,
		props: true,
	}, {
		path: 'events/:id/edit',
		name: 'events:edit',
		component: Event,
		props: true,
		meta: {requiresAuth: true},
	}, {
		path: 'calendar',
		name: 'events:calendar',
		component: Calendar
	}]
}, {
	path: '/login',
	component: Login,
	name: 'login'
}]

export default routes
