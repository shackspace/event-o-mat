<template lang="jade">
.c-user.center-panel
	.user-content(v-if="user")
		.user-header
			.profile(v-if="user.picture")
				img(:src="user.picture")
			h2(v-if="user.name") {{ user.name }}
			h2(v-else) {{ user.email }}
			.button-row
				bunt-button#impersonate(@click.native="impersonate", :loading="loadingImpersonate") impersonate
				bunt-button#intercom(@click.native="intercom", :loading="loadingIntercom") intercom
		.user-body
			.info
				strong Email: 
				a(:href="`mailto:${user.email}`") {{ user.email }}
			.info(v-if="user.date_joined")
				strong Joined 
				span {{ user.date_joined | fromnow }}
			.info(v-if="user.last_login")
				strong Last login 
				span {{ user.last_login | fromnow }}
			.info
				strong Groups
				ul
					li(v-for="group in user.groups") {{ group }}

	bunt-progress-circular(v-else, size="huge", :page="true")
</template>
<script>
import api from 'lib/api'
export default {
	data () {
		return {
			user: null,
			loadingImpersonate: null,
			loadingIntercom: null
		}
	},
	computed: {},
	created () {
		api.idm.users.get(this.$route.params.id).then((response) => {
			this.user = response
		})
	},
	methods: {
		impersonate () {
			this.loadingImpersonate = true
			api.idm.users.impersonate(this.user.id).then((response) => {
				window.open('https://cockpit.ax-semantics.com/#access_token=impersonation&token_type=Bearer&id_token=' + response.token, '_blank')
				this.loadingImpersonate = false
			})
		},
		intercom () {
			this.loadingIntercom = true
			api.idm.users.intercom(this.user.id).then((response) => {
				window.open(response.url, '_blank')
				this.loadingIntercom = false
			})
		}
	}
}
</script>
<style lang="stylus">
@import '~_settings'
.c-user
	display: flex
	flex-direction: column
	background-color: $clr-white

	.user-content
		position: relative
		flex: 1
		align-self: center
		width: 90%

		.user-header
			display: flex
			flex-direction: column
			justify-content: space-between
			align-items: center
			width: 100%
			border-bottom: border-separator()
			margin-bottom: 32px

			.profile img
				height: 128px
				width: 128px
				margin-top: 32px

			.button-row
				display: flex
				width: 100%
				padding-bottom: 16px
				justify-content: space-around
				#impersonate
					button-style(color: $clr-blue)
				#intercom
					button-style(color: $clr-blue)

		.user-body
			margin-left: auto
			line-height: 24px
			ul
				line-height: 1
</style>
