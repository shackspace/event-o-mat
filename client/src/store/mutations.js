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
	}
}

export default mutations
