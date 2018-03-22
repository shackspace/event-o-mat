<template lang="jade">
#c-login
	img(src="~assets/images/logo.svg")
	h1 event-o-mat
	h2 v1.alpha

	form(@submit.prevent="submit")
		bunt-input(name="username", v-model="username", label="username")
		bunt-input(name="password", v-model="password", label="password", type="password")
		bunt-button(type="submit") Login
</template>
<script>
import api from 'lib/api'

export default {
	data () {
		return {
			username: '',
			password: ''
		}
	},
	methods: {
		submit () {
			api.auth.login(this.username, this.password).then(() => this.$router.go('/'))
		}
	}
}
</script>
<style lang="stylus">
@import "~_settings"

#c-login
	display: flex
	flex-direction: column
	justify-content: center
	align-items: center
	padding-top: 128px
	img
		width: 20vw
		padding-bottom: 16px
	h1
		font-size: 52px
		line-height: 1em
		font-weight: 200
		margin: 0
		letter-spacing: 24px
		margin-left: 24px
		color: $clr-shack-dark
	h2
		color: $clr-secondary-text-light
		font-weight: 300
		font-size: 16px
		font-family: "Roboto Mono"
		margin: 8px 0 32px 0
		text-align: center
	form
		display: flex
		flex-direction: column
		align-items: center
		input
			width: 150px
			background-color: transparent
		button
			width: 150px

	.bunt-button
		button-style(color: $clr-shack)

</style>
