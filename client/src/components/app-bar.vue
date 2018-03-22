<!--
The main navigation bar
When there is an active project, the projects tab-nav is shown
!-->
<template lang="jade">
nav.primary(:class="{'with-secondary': hasSecondaryNavbar}")
	.left
		router-link(:to="{name: 'users'}").logo
			img(src="~assets/images/logo.svg")
	bunt-tabs(:active-tab="activeTab")
		bunt-tab(header="user management", id="a-tab", @selected="tabSelected")
	.actions
		.profile-wrapper(@click="")
			img.profile(ref="profile", :src="user.profile.picture", @mouseenter="showProfileTooltip = true", @mouseleave="showProfileTooltip = false")
			tooltip(:show="showProfileTooltip") Settings
</template>
<script>
import { mapState } from 'vuex'
import Tooltip from 'buntpapier/src/tooltip'

export default {
	name: 'app-bar',
	components: {Tooltip},
	data () {
		return {
			showProfile: false,
			showProfileTooltip: false
		}
	},
	computed: {
		...mapState(['user']),
		activeTab () {
			return this.$route.name.split(':', 1)[0]
		},
		hasSecondaryNavbar () {
			return this.$route.matched.some(record => record.meta.hasNavbar)
		}
	},
	methods: {
		tabSelected (id) {
			if (this.$route.name.split(':', 1)[0] === id)
				return // HACK prevent programatic select changing route, see computed.activeTab
			this.$router.replace({name: id, params: this.$route.params})
		},
	}
}
</script>
<style lang="stylus">
@import '~_settings'

nav.primary
	z-index: 100
	flex: 0 0 48px
	card()
	background-color: $clr-white
	border-bottom: solid 2px $ax-primary
	display: flex
	justify-content: space-between
	transition: width .3s ease
	border-radius: 0
	position: relative

	&.with-secondary
		box-shadow: none

	.profile
		height: 32px
		width: 32px
		border-radius: 50%
		margin-left: 8px
		cursor: pointer

	.bottom-container
		display: flex
		flex-direction: column

	.logo
		display: flex
		align-items: center
		padding: 0 8px
		z-index: 101

		img
			height: 40px
			margin-right: 6px

	$nav-height = 48px
	.project-bar
		position: absolute
		left: 0
		right: 0
		display: flex
		justify-content: space-around
		border-radius: 0
		flex: 1
		z-index: 100
		align-self: flex-end
		.bunt-tabs
			width: auto
			tabs-style(
				background-color: transparent,
				color: $clr-secondary-text-light,
				active-color: $clr-primary-text-light,
				indicator-color: $ax-primary
			)
			margin-bottom: 0
			.bunt-tabs-indicator
				height: 5px
			.bunt-tabs-body
				display: none
	.left
		z-index: 101
		display: flex
	.project-name
		h1
			color: $clr-primary-text-light
			margin: 0 4px 0px 16px
			line-height: $nav-height
			font-size: 14px
			font-weight: 300
			span.project-id
				margin-left: 4px
				font-weight: 400
				&::after
					content: ' – '
			span.project-name
				font-weight: 500

	.actions
		z-index: 101
		display: flex
		align-items: center
		padding-right: 16px

		.bunt-icon-button
			icon-button-style(color:$clr-secondary-text-light, style:'clear')

		.profile-wrapper
			position: relative
.bunt-drop
	z-index: 100
.apps-popover
	card()
	width: 320px
	padding: 0px
	.legacy-apps
		div
			padding: 0px 15px
			&:hover
				background-color: $clr-grey-100
			a
				display: flex
				height: 42px
				align-items: center
				i
					padding-right: 15px
					font-size: 16px
					color: $clr-secondary-text-light
				span
					font-size: 15px
					color: $clr-secondary-text-light
	.help-apps
		border-bottom: border-separator()
		>div
			padding: 15px 15px
			&:hover
				background-color: $clr-grey-100
			a
				height: 42px
				div
					font-size: 18px
					color: $clr-grey-900
				span
					font-size: 12px
					color: $clr-secondary-text-light
</style>
