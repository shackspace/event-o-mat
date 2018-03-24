<template lang="jade">
.c-event-item
	bunt-progress-circular(v-if="loading", size="huge", :page="true")
	template(v-else)
		transition(name="edit")
			.edit-pane(v-if="$route.name === 'events:edit' || $route.name === 'events:new'")
				event-form(:event="event")
		.preview
			.heading
				h1 {{ event.name }}
				transition(name="edit-button")
					bunt-link-button(v-if="$route.name !== 'events:edit'", :to="{name: 'events:edit'}") edit
			h4 {{ event.start | datetime }} – {{ event.end | datetime }}
			h4 {{ roomsLookup[event.room].name }}
			.description(v-html="markdown", v-scrollbar.y="")
</template>
<script>
import { mapState } from 'vuex'
import MarkdownIt from 'markdown-it'
import EventForm from './form'

const markdownIt = new MarkdownIt()

export default {
	components: { EventForm },
	props: {
		id: [String, Number]
	},
	data () {
		return {
			event: null,
			loading: true
		}
	},
	computed: {
		...mapState(['roomsLookup']),
		markdown () {
			return markdownIt.render(this.event.description)
		}
	},
	created () {
		if (!this.id) {
			this.loading = false
			this.event = {
				name: '',
				description: '',
				start: '',
				end: '',
				room: null
			}
			return
		}
		api.events.get(this.id).then((event) => {
			this.event = event
			this.loading = false
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
@import '~_settings'
.c-event-item
	width: 100vw
	align-self: center
	display: flex
	justify-content: center
	flex: 1
	position: relative
	.edit-pane
		width: 50vw
		display: flex
	.preview
		flex: 1 1 50vw
		max-width: 50vw
		padding: 0 64px
		display: flex
		flex-direction: column
		.heading
			display: flex
			justify-content: space-between
			align-items: center
			.bunt-link-button
				link-button-style(color: $clr-primary)
		.description
			flex: 1 1 0
			position: relative

	.edit-enter-active, .edit-leave-active
		transition: width .4s ease
		.c-event-form
			transform: translateX(0)
			transition: transform .4s ease
	.edit-enter, .edit-leave-to
		width: 0
		.c-event-form
			transform: translateX(-50vw)

	.edit-button-enter-active, .edit-button-leave-active
		transform: translateX(0)
		transition: transform .4s ease
	.edit-button-enter, .edit-button-leave-to
		transform: translateX(50vw)
</style>
