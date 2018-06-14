<template lang="jade">
.c-series-item
	bunt-progress-circular(v-if="loading", size="huge", :page="true")
	template(v-else)
		transition(name="edit")
			.edit-pane(v-if="$route.name === 'series:edit' || $route.name === 'series:new'", key="edit")
				series-form(:series="series", :creation="$route.name === 'series:new'")
		.preview
			.heading
				h1 {{ series.name }}
				transition(name="edit-button")
					bunt-link-button(v-if="user.authenticated && $route.name !== 'series:edit' && $route.name !== 'series:new'", :to="{name: 'series:edit'}") edit
			h4 {{ series.start }} – {{ series.end }}
			h4 {{ series.room ? roomsLookup[series.room].name : '–' }}
			.description(v-html="markdown", v-scrollbar.y="")
</template>
<script>
import api from 'lib/api'
import { mapState } from 'vuex'
import MarkdownIt from 'markdown-it'
import SeriesForm from './form'

const markdownIt = new MarkdownIt({
	html: true,
	linkify: true,
	typographer: true
})

export default {
	components: { SeriesForm },
	props: {
		id: [String, Number]
	},
	data () {
		return {
			series: null,
			loading: true
		}
	},
	computed: {
		...mapState(['roomsLookup', 'user']),
		markdown () {
			return markdownIt.render(this.series.description)
		}
	},
	created () {
		this.routeUpdated()
	},
	mounted () {
		this.$nextTick(() => {
		})
	},
	watch: {
		'id': 'routeUpdated'
	},
	methods: {
		routeUpdated () {
			if (!this.id) {
				this.loading = false
				this.series = {
					name: '',
					description: '',
					start: '00:00',
					end: '00:00',
					room: null,
					rrule: ''
				}
				return
			}
			this.loading = true
			api.series.get(this.id).then((series) => {
				series.start = series.start
				series.end = series.end
				this.series = series
				this.loading = false
			})
		}
	}
}
</script>
<style lang="stylus">
@import '~_settings'
.c-series-item
	width: 100vw
	align-self: center
	display: flex
	justify-content: center
	flex: 1 0 0
	overflow: hidden
	position: relative
	.edit-pane
		width: 50vw
		display: flex
		order: 1
	.preview
		flex: 1 1 50vw
		max-width: 50vw
		padding: 0 64px
		display: flex
		flex-direction: column
		order: 2
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
		.c-series-form
			transform: translateX(0)
			transition: transform .4s ease
	.edit-enter, .edit-leave-to
		width: 0
		.c-series-form
			transform: translateX(-50vw)

	.edit-button-enter-active, .edit-button-leave-active
		transform: translateX(0)
		transition: transform .4s ease
	.edit-button-enter, .edit-button-leave-to
		transform: translateX(50vw)
</style>
