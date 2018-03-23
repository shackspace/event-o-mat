<template lang="jade">
#v-app
	app-bar
	router-view(v-if="ready")
	bunt-progress-circular(v-else, size="huge", :page="true")
</template>
<script>
import AppBar from 'components/app-bar'
import { mapState, mapGetters } from 'vuex'

import 'styles/style.styl'

const STATIC_TITLES = {
}

export default {
	components: { AppBar },
	computed: {
		...mapGetters(['ready']),
		title () {
			if (this.$route.name in STATIC_TITLES)
				return STATIC_TITLES[this.$route.name]
		}
	},
	watch: {
		'title': 'changeTitle'
	},
	created () {
		this.$store.dispatch('fetch-all')
	},
	mounted () {
		this.changeTitle()
	},
	methods: {
		changeTitle () {
			document.title = this.title ? this.title + ' – event-o-mat' : 'shack event-o-mat'
		},
		loadEvents () {
			this.$store.dispatch('fetch-events')
		}
	}
}
</script>
<style lang="stylus">
#v-app
	background-color: $clr-white
	> .failing
		display: flex
		flex-direction: column
		align-items: center
		h1
			font-size: 128px
		h2
			font-size: 52px
</style>
