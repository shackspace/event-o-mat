const getters = {
	ready (state, getters) {
		return !!(state.user) && !!(state.rooms) && !!(state.events)
	}
}

export default getters
