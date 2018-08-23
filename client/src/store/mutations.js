import moment from 'moment'

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
	},
	ADD_EVENT (state, event) {
		event.start = moment(event.start)
		event.end = moment(event.end)
		state.events.push(event)
		state.events.sort((a, b) => a.start.diff(b.start))
	},
	UPDATE_EVENT (state, event) {
		const existingEvent = state.events.find((e) => e.id === event.id)
		event.start = moment(event.start)
		event.end = moment(event.end)
		Object.assign(existingEvent, event)
	},
	REMOVE_EVENT (state, event) {
		const index = state.events.findIndex((e) => e.id === event.id)
		if (index < 0) return
		state.events.splice(index, 1)
	}
}

export default mutations
