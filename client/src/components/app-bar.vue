<!--
The main navigation bar
When there is an active project, the projects tab-nav is shown
!-->
<template lang="jade">
nav.primary(:class="{'with-secondary': hasSecondaryNavbar}")
	.left
		router-link(:to="{name: 'events:list'}").logo
			img(src="~assets/images/logo-white-bg-no-tagline.svg")
	//- bunt-tabs(:active-tab="activeTab")
	//- 	bunt-tab(header="user management", id="a-tab", @selected="tabSelected")
	//- .actions
	//- 	.profile-wrapper(@click="")
	//- 		img.profile(ref="profile", :src="user", @mouseenter="showProfileTooltip = true", @mouseleave="showProfileTooltip = false")
	//- 		tooltip(:show="showProfileTooltip") Settings
	.actions
		bunt-button(v-if="!user.authenticated", @click="login", :loading="loggingIn") Login
</template>
<script>
import api from 'lib/api'
import { mapState } from 'vuex'
import Tooltip from 'buntpapier/src/tooltip'

export default {
	name: 'app-bar',
	components: {Tooltip},
	data () {
		return {
			loggingIn: false,
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
		login () {
			this.loggingIn = true
			api.auth.login()
		}
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
	border-bottom: solid 2px $clr-primary
	display: flex
	justify-content: space-between
	transition: width .3s ease
	border-radius: 0
	position: relative

	.logo
		display: flex
		align-items: center
		padding: 0 8px
		z-index: 101

		img
			height: 40px
			margin-right: 6px

	> .left
		z-index: 101
		display: flex

	.actions
		// z-index: 101
		display: flex
		align-items: center
		padding-right: 16px

		.bunt-icon-button
			icon-button-style(color:$clr-secondary-text-light, style:'clear')

		.bunt-button
			width: 128px
			button-style(color: $clr-primary)
</style>
