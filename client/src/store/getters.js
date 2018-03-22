const getters = {
	ready (state, getters) {
		return !!(state.rooms)
	}
}

export default getters
