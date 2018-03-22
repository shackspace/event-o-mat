/* global Headers, fetch */
import config from 'config'
import querystring from 'querystring'

const BASE_URL = config.api.baseUrl
let headers = new Headers()
headers.append('Content-Type', 'application/json')

export function cleanQuery (object) {
	Object.keys(object).forEach(key => !object[key] && delete object[key])
	return object
}

let api = {
	auth: {
		authenticated: false,
		login (username, password) {
			return fetch(BASE_URL + 'api-token-auth/', {method: 'POST', headers: headers, body: JSON.stringify({username: username, password: password})}).then((response) => {
				if (!response.ok)
					return Promise.reject(response.statusCode)
				return response.json()
			}).then((json) => {
				localStorage.setItem('user', JSON.stringify(json))
				api.auth.authenticated = true
				headers.set('Authorization', 'Token ' + json.token)
				return Promise.resolve(json)
			})
		},
		getSession () {
			let user = JSON.parse(localStorage.getItem('user'))
			if (!user) return Promise.reject(new Error('no session'))
			headers.set('Authorization', 'Token ' + user.token)
			api.auth.authenticated = true
			return Promise.resolve()
		}
	},
	users: {
		me () {
			return api.fetch(`me/`)
		}
	},
	rooms: {
		list () {
			return api.fetch(`rooms/`)
		}
	},
	events: {
		list () {
			return api.fetch(`events/`)
		},
		get (id) {
			return api.fetch(`events/${id}/`)
		},
		update (event) {
			return api.fetch(`events/${event.id}/`, 'PUT', event)
		},
		create (event) {
			return api.fetch('events/', 'POST', event)
		},
	}
}

api.fetch = function (url, method, body) {
	let options = {
		method: method || 'GET',
		headers,
		body: JSON.stringify(body)
	}
	return window.fetch(url.startsWith('http') ? url : BASE_URL + url, options).then((response) => {
		return response.json().then((json) => {
			if (!response.ok)
				return Promise.reject(json)

			return Promise.resolve(json)
		})
	}).catch((error) => {
		return Promise.reject(error)
	})
}

export default api
