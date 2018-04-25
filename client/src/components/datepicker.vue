<template lang="jade">
.c-datetime-picker
	.bunt-input.dense(:class!="{focused, 'floating-label': value !== null, invalid}")
		.label-input-container
			label(:for="name") {{ label }}
			input(ref="input", type="text", :name="name", :value="$options.filters.datetime(value)", :readonly="true", @focus="focused = true", @blur="onBlur")
		.underline
		//- .hint {{ hintText }}
	.picker(v-show="focused", @mousedown="lockFocus = true", @mouseup="lockFocus = false")
		.datepicker
			.actions
				bunt-icon-button(@click="activeMonth = activeMonth.clone().subtract(1, 'month')", tabindex="-1") chevron_left
				.monthlabel {{ activeMonth.format('MMMM YYYY') }}
				bunt-icon-button(@click="activeMonth = activeMonth.clone().add(1, 'month')", tabindex="-1") chevron_right
			.month
				.weekday Mo
				.weekday Di
				.weekday Mi
				.weekday Do
				.weekday Fr
				.weekday Sa
				.weekday So
				.day(v-for="day in Array.from({length: activeMonth.daysInMonth()}, (v, k) => k)", :class="{active: value.isSame(activeMonth.clone().set('date', day + 1), 'day')}", :style="{'grid-column': ((day + startingDay) % 7) || 7, 'grid-row': Math.ceil((day + startingDay) / 7) + 1}", @click="selectDay(day + 1)") {{ day + 1 }}
		.timepicker
			.bunt-input.dense
				input(ref="hours", name="hours", :value="value.format('HH')", @mousedown="yieldToTimeInputs = true", @blur="onTimeBlur")
			span :
			.bunt-input.dense
				input(ref="minutes", name="minutes", :value="value.format('mm')", @mousedown="yieldToTimeInputs = true", @blur="onTimeBlur")
</template>
<script>

export default {
	props: {
		value: Object,
		name: String,
		label: String,
		hint: String,
		validation: Object
	},
	components: {},
	data () {
		return {
			activeMonth: null,
			focused: false,
			lockFocus: false,
			yieldToTimeInputs: false,
			activeDay: null
		}
	},
	computed: {
		startingDay () {
			return this.activeMonth.isoWeekday()
		},
		invalid () {
			return this.validation && this.validation.$error
		},
		hintText () {
			if (this.invalid && this.validation.$params) {
				const errorMessages = Object.keys(this.validation.$params).map((key) => this.validation[key] ? null : this.validation.$params[key].message)
				return errorMessages.filter(Boolean).join()
			}
			return this.hint
		}
	},
	created () {
		this.copyValue()
	},
	mounted () {
		this.$nextTick(() => {
		})
	},
	watch: {
		value: 'copyValue'
	},
	methods: {
		copyValue () {
			this.activeMonth = this.value.clone().startOf('month')
			this.activeDay = this.value.date()
		},
		onBlur () {
			if (this.lockFocus) {
				if (this.yieldToTimeInputs) return
				this.$refs.input.focus()
				return
			}
			this.focused = false
		},
		onTimeBlur (event) {
			this.yieldToTimeInputs = false
			this.onBlur()
			this.emitInput()
		},
		selectDay (day) {
			this.activeDay = day
			this.emitInput()
		},
		emitInput () {
			const date = this.activeMonth.clone()
			date.set('date', this.activeDay)
			date.set('hour', this.$refs.hours.value)
			date.set('minute', this.$refs.minutes.value)
			this.$emit('input', date)
		}
	}
}
</script>
<style lang="stylus">
@import '~_settings'

.c-datetime-picker
	position: relative
	.picker
		card()
		position: absolute
		top: 41px
		height: 264px
		width: 2 * 248px
		display: flex
		z-index: 10
		user-select: none
		.datepicker
			flex: 1
			display: flex
			flex-direction: column
			.actions
				align-self: center
				display: flex
				align-items: center
				justify-content: space-between
				.bunt-icon-button
					icon-button-style(style: 'clear')
			.month
				flex: 1
				display: grid
				grid-template-columns: repeat(7, 1fr)
				grid-template-rows: 32px repeat(6, 1fr)
				padding: 0 16px 16px 16px
				grid-gap: 1px
			.weekday
				grid-row: 1
			.day
				display: flex
				justify-content: center
				align-items: center
				border-radius: 50%
				cursor: pointer
				&:hover
					background-color: $clr-grey-300
				&.active
					background-color: $clr-grey-400
		.timepicker
			flex: 1
			display: flex
			align-items: center
			justify-content: center

			.bunt-input
				width: 2em
				min-width: @width
				margin: 0
				padding: 0
				input
					text-align: center
					font-size: 24px
				.underline
					padding-top: 2px
			span
				padding: 0 4px
				font-size: 32px
</style>
