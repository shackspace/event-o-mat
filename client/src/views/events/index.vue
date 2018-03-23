<template lang="jade">
.c-events-index
	.toolbar
		router-link(:to="{name: 'events:new'}") new event
	.events-list.list
		.tbody(v-scrollbar.y="")
			router-link.event.item(v-for="event in events", :to="{name: 'events:item', params: {id: event.id}}")
				.name {{ event.name }}
				.start {{ event.start | datetime }}
				.end {{ event.end | datetime }}
				.keyholder {{ event.keyholder }}
				.room {{ event.room.name }}
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
.c-events-index
	align-self: center
	display: flex
	width: 900px
	max-width: 900px
	flex-direction: column
	.toolbar
		height: 36px
		line-height: @height
	.events-list
		.event
			.name
				flex: 1
			.start, .end
				width: 10em

</style>
