<template lang="jade">
.c-event-item
	bunt-progress-circular(v-if="!event", size="huge", :page="true")
</template>
<script>
export default {
	components: {},
	props: {
		id: String
	}
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
</style>
