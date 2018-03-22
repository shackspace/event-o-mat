const getters = {
	ready (state, getters) {
		return !!(state.user)
	}
}

export default getters
