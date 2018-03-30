const getters = {
	ready (state, getters) {
		return !!(state.rooms) && !!(state.events)
	}
}

export default getters
