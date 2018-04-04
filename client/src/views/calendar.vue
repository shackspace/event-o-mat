<template lang="jade">
.c-calendar
	.actions
		bunt-icon-button(@click="month--") chevron_left
		.monthlabel {{ monthMoment.format('MMMM') }}
		bunt-icon-button(@click="month++") chevron_right
	.month
		.weekday Monday
		.weekday Tuesday
		.weekday Wednesday
		.weekday Thursday
		.weekday Friday
		.weekday Saturday
		.weekday Sunday
		.day(v-for="day in Array.from({length: monthMoment.daysInMonth()}, (v, k) => k)", :style="{'grid-column': ((day + startingDay) % 7) || 7, 'grid-row': Math.ceil((day + startingDay) / 7) + 1}")
			.label {{ day + 1 }}
			.events
				.event(v-for="event of eventsPerDay[day]")
					span.time {{ event.start | time }}
					span.name {{ event.name }}
</template>
<script>
import moment from 'moment'
import { mapState } from 'vuex'

export default {
	components: {},
	data () {
		return {
			month: 3
		}
	},
	computed: {
		...mapState(['events', 'roomsLookup']),
		monthMoment () {
			return moment({month: this.month - 1})
		},
		startingDay () {
			return this.monthMoment.isoWeekday()
		},
		eventsPerDay () {
			const eventsPerDay = {}
			for (const event of this.events) {
				const start = moment(event.start)
				if (start.month() !== this.month - 1) continue
				if (!eventsPerDay[start.date()]) {
					eventsPerDay[start.date()] = []
				}
				eventsPerDay[start.date()].push(event)
			}
			return eventsPerDay
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

.c-calendar
	flex: 1
	display: flex
	flex-direction: column
	.actions
		display: flex
		align-items: center
		width: 128px
		justify-content: space-between
	.month
		flex: 1
		display: grid
		grid-template-columns: repeat(7, 1fr)
		grid-template-rows: 32px repeat(6, 1fr)
		padding: 0 16px
		grid-gap: 1px
	.weekday
		grid-row: 1
	.day
		outline: 1px solid $clr-grey-300
		.label
			color: $clr-secondary-text-light
			padding: 4px 0 0 4px
	.event
		display: block
		background-color: $clr-primary
		border: 1px solid $clr-green
		border-radius: 2px
		grid-column: 5 / span 2
		grid-row: 3
		margin: 24px 8px
		height: 24px
		line-height: @height
		padding: 8px 16px

		.time
			padding-right: 8px
</style>
