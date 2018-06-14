import App from './App'
import Login from 'views/login'

import EventsList from 'views/events'
import Event from 'views/events/item'
import Calendar from 'views/calendar'

import SeriesList from 'views/series'
import Series from 'views/series/item'

let routes = [{
	path: '/',
	component: App,
	children: [{
		path: '/',
		name: 'events',
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
		meta: {requiresAuth: true}
	}, {
		path: 'calendar',
		name: 'events:calendar',
		component: Calendar
	}, {
		path: 'series',
		name: 'series',
		component: SeriesList,
		meta: {requiresAuth: true}
	}, {
		path: 'series/new',
		name: 'series:new',
		component: Series,
		meta: {requiresAuth: true}
	}, {
		path: 'series/:id',
		name: 'series:item',
		component: Series,
		props: true,
	}, {
		path: 'series/:id/edit',
		name: 'series:edit',
		component: Series,
		props: true,
		meta: {requiresAuth: true}
	}]
}, {
	path: '/login',
	component: Login,
	name: 'login'
}]

export default routes
