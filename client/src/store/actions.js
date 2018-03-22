import api from 'lib/api'

const actions = {
	'fetch-all' ({dispatch}) {
		return Promise.all([dispatch('fetch-user'), dispatch('fetch-rooms'), dispatch('fetch-events')])
	},
	'fetch-user' ({commit}) {
		return api.users.me().then((user) => {
			commit('SET_USER', user)
			return Promise.resolve()
		})
	},
	'fetch-rooms' ({commit}) {
		return api.rooms.list().then((rooms) => {
			commit('SET_ROOMS', rooms)
			return Promise.resolve()
		})
	},
	'fetch-events' ({commit}) {
		return api.events.list().then((events) => {
			commit('SET_EVENTS', events)
			return Promise.resolve()
		})
	}
}

export default actions
