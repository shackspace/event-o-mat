const mutations = {
	SET_USER (state, user) {
		state.user = user
	},
	SET_ROOMS (state, rooms) {
		state.rooms = rooms
		state.roomsLookup = rooms.reduce((acc, r) => { acc[r.id] = r; return acc }, {})
	},
	SET_EVENTS (state, events) {
		state.events = events
	},
	SET_SERIES_LIST (state, seriesList) {
		state.seriesList = seriesList
	}
}

export default mutations
