<template lang="jade">
.c-users.bi-view
	.users-panel.left-panel
		.actions
			bunt-input(v-model="search", name='search')
		.user-list(v-scrollbar.y="")
			router-link.user(v-for="user in scrolledUsers", :to="{name: 'user', params: {id: user.id}}")
				.profile
					img(:src="user.picture")
				.name(v-if="user.first_name") {{ user.first_name }} {{ user.last_name }}
				.name(v-else) {{ user.name }}
				.email {{ user.email }}
				.last(v-if="user.last_login") {{ user.last_login | fromnow }}
				.last(v-else) never
			infinite-scroll(@infinite="onInfinite")
	.center-frame
		transition(name="bi-view-center-animation", mode="in-out")
			router-view(v-if="this.$route.name === 'user'", :key="this.$route.params.id")
</template>
<script>
import { mapState } from 'vuex'
import fuzzysearch from 'fuzzysearch'
import InfiniteScroll from 'components/infinite-scroll'
export default {
	components: {InfiniteScroll},
	data () {
		return {
			search: '',
			scroll: 100
		}
	},
	computed: {
		...mapState(['users']),
		scrolledUsers () {
			return this.filteredUsers.slice(0, this.scroll)
		},
		filteredUsers () {
			return this.users.filter((user) => {
				return fuzzysearch(this.search.toLowerCase(), user.email.toLowerCase()) ||
					fuzzysearch(this.search.toLowerCase(), (user.name?.toLowerCase() || ''))
			})
		}
	},
	created () {},
	mounted () {
		this.$nextTick(() => {
		})
	},
	methods: {
		onInfinite () {
			this.scroll += 100;
		}
	}
}
</script>
<style lang="stylus">
@import '~_settings'
.c-users

	.users-panel
		flex: 2
	.user-list
		flex: 1
		display: flex
		flex-direction: column
		position: relative
	.user
		display: flex
		flex-shrink: 0
		align-items: center
		height: 52px
		border-bottom: border-separator()
		> *
			padding: 0 16px
			&:first-child
				padding-left: 36px
		.last
			flex: 0
			margin-left: auto
			min-width: 100px
			color $clr-disabled-text-light
		.name
			min-width: 150px

	.profile img
		height: 32px
		width: 32px
		border-radius: 50%
</style>
