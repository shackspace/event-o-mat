<template lang="jade">
.c-event-item
	bunt-progress-circular(v-if="!event", size="huge", :page="true")
	template(v-else)
		router-view(v-if="$route.name === 'events:edit'", :event="event")
		template(v-else)
			h1 {{ event.name }}
			h4 {{ event.start | datetime }} – {{ event.end | datetime }}
			h4 {{ event.room }}
			p {{ event.description }}
</template>
<script>
export default {
	components: {},
	props: {
		id: Number
	},
	data () {
		return {
			event: null
		}
	},
	computed: {},
	created () {
		api.events.get(this.id).then((event) => {
			this.event = event
		})
	},
	mounted () {
		this.$nextTick(() => {
		})
	},
	methods: {}
}
</script>
<style lang="stylus">
.c-event-item
	width: 900px
	align-self: center
</style>
