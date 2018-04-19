<template lang="jade">
.c-calendar
	.actions
		bunt-icon-button(@click="activeMonth = activeMonth.clone().subtract(1, 'month')") chevron_left
		.monthlabel {{ activeMonth.format('MMMM YYYY') }}
		bunt-icon-button(@click="activeMonth = activeMonth.clone().add(1, 'month')") chevron_right
		bunt-button(@click="backToCurrentMonth") to current month
	.month(v-scrollbar.y="")
		.weekday Montag
		.weekday Dienstag
		.weekday Mittwoch
		.weekday Donnerstag
		.weekday Freitag
		.weekday Samstag
		.weekday Sonntag
		.day(v-for="day in Array.from({length: activeMonth.daysInMonth()}, (v, k) => k)", :style="{'grid-column': ((day + startingDay) % 7) || 7, 'grid-row': Math.ceil((day + startingDay) / 7) + 1, '--events-count': eventsPerDay[day] ? eventsPerDay[day].length : 0}", :class="{today: isToday(day + 1)}")
			.label {{ day + 1 }}
			.events
				event-link.event(v-for="event of eventsPerDay[day]", :event="event")
					span.time {{ event.start | time }}
					span.name {{ event.name }}
</template>
<script>
import moment from 'moment'
import { mapState } from 'vuex'
import EventLink from 'components/event-link'

export default {
	components: { EventLink },
	data () {
		return {
			activeMonth: moment().startOf('month')
		}
	},
	computed: {
		...mapState(['events', 'roomsLookup']),
		startingDay () {
			return this.activeMonth.isoWeekday()
		},
		eventsPerDay () {
			const eventsPerDay = {}
			for (const event of this.events) {
				const start = moment(event.start)
				if (!start.isSame(this.activeMonth, 'month')) continue
				const startDay = start.date() - 1
				if (!eventsPerDay[startDay]) {
					eventsPerDay[startDay] = []
				}
				eventsPerDay[startDay].push(event)
			}
			return eventsPerDay
		}
	},
	created () {},
	mounted () {
		this.$nextTick(() => {
		})
	},
	methods: {
		backToCurrentMonth () {
			this.activeMonth = moment().startOf('month')
		},
		isToday (date) {
			return this.activeMonth.clone().set('date', date).isSame(moment(), 'date')
		}
	}
}
</script>
<style lang="stylus">
@import '~_settings'

.c-calendar
	flex: 1
	display: flex
	flex-direction: column
	min-height: 0
	.actions
		height: 52px
		display: flex
		align-items: center
		width: 360px
		justify-content: space-between

		.bunt-button
			button-style(style: 'clear')
	.month
		position: relative
		flex: 1
		display: grid
		grid-template-columns: repeat(7, 1fr)
		grid-template-rows: 32px repeat(6, 1fr)
		padding: 0 16px
		grid-gap: 1px
	.weekday
		grid-row: 1event-link
	.day
		outline: 1px solid $clr-grey-300
		min-width: 0
		overflow-x: hidden
		// height: fit-content no FF support
		height: calc(var(--events-count) *  36px + 35px)
		min-height: 100%
		.label
			color: $clr-secondary-text-light
			padding: 6px 0
			margin: 2px
			text-align: center
			width: 28px
			height: @width
			box-sizing: border-box
		&.today
			background-color: $clr-grey-200
			.label
				font-weight: 600
				background-color: $clr-primary
				color: $clr-primary-text-dark

				border-radius: 50%
	.events
		display: flex
		flex-direction: column
		margin-top: 4px
	.event
		display: block
		color: $clr-primary-text-dark
		background-color: $clr-primary
		font-weight: 600
		border-radius: 2px
		grid-column: 5 / span 2
		grid-row: 3
		margin: 0 8px 4px 8px
		height: 24px
		line-height: @height
		padding: 4px 16px
		text-overflow: ellipsis
		white-space: nowrap
		overflow: hidden
		.time
			padding-right: 8px
</style>
