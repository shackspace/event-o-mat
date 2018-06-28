<template lang="jade">
.c-events-index
	.actions
		bunt-link-button(:to="{name: 'events:calendar'}") view calendar
		bunt-link-button(v-if="user.authenticated && user.hasPermissions", :to="{name: 'events:new'}") new event
	.events-list.list
		.tbody(v-scrollbar.y="")
			event-link.event.item(v-for="event in futureEvents", :event="event")
				.name {{ event.name }}
				.date(v-if="event.start.diff(event.end, 'days') > 0") {{ event.start | humandatetime }} - {{ event.end | humandatetime }}
				.date(v-else) {{ event.start | humandatetime }} - {{ event.end | time }}
				//- .keyholder {{ event.keyholder.username }}
				.room {{ roomsLookup[event.room].name }}
</template>
<script>
import moment from 'moment'
import { mapState } from 'vuex'
import EventLink from 'components/event-link'
export default {
	components: { EventLink },
	data () {
		return {
		}
	},
	computed: {
		...mapState(['events', 'roomsLookup', 'user']),
		futureEvents () {
			return this.events.filter((event) => event.end.diff(moment()) > 0)
		}
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
@import '~_settings'

.c-events-index
	align-self: center
	display: flex
	width: 900px
	max-width: 900px
	flex-direction: column
	overflow: hidden
	.actions
		flex: 0 0 36px
		height: 36px
		padding: 8px 16px
		line-height: @height
		background-color: $clr-grey-200
		border-bottom: border-separator()
		display: flex
		justify-content: space-between
		.bunt-link-button
			link-button-style(color: $clr-primary)
	.events-list
		margin-top: 16px
		overflow: hidden
		.event
			flex: 0 0 auto
			.name
				flex: 1
			.date
				width: 256px
			.keyholder
				width: 96px
				padding-right: 16px
			.room
				width: 92px

</style>
