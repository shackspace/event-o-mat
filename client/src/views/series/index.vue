<template lang="jade">
.c-series-index
	.actions
		bunt-link-button(:to="{name: 'series:new'}") new series
	.series-list.list
		.tbody(v-scrollbar.y="")
			router-link.series.item(v-for="series in seriesList", :to="{name: 'series:edit', params: {id: series.id}}")
				.name {{ series.name }}
				//- .date(v-if="event.start.diff(event.end, 'days') > 0") {{ event.start | humandatetime }} - {{ event.end | humandatetime }}
				//- .date(v-else) {{ event.start | humandatetime }} - {{ event.end | time }}
				//- .keyholder {{ event.keyholder.username }}
				.room {{ roomsLookup[series.room].name }}
</template>
<script>
import { mapState } from 'vuex'
export default {
	components: { },
	data () {
		return {
		}
	},
	computed: {
		...mapState(['seriesList', 'roomsLookup', 'user'])
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

.c-series-index
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
	.series-list
		margin-top: 16px
		overflow: hidden
		.series
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
