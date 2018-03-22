<template lang="jade">
.c-events-index
	router-link(:to="{name: 'events:new'}") new event
	.event(v-for="event in events") {{ event.name }}
</template>
<script>
import { mapState } from 'vuex'

export default {
	components: {},
	data () {
		return {
		}
	},
	computed: {
		...mapState(['events']),
	},
	created () {},
	mounted () {
		this.$nextTick(() => {
		})
	},
	methods: {}
}
</script>
<style lang="stylus">
.c-events-list
	display: flex
</style>
