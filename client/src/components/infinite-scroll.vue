<!--
Naginis common "pagination"
Used together with API-Cursors

Usage:

infinite-scroll(@infinite="onInfinite", :loading='itemsLoading')

Trigger api call at `onInfinite`
set loading to `true` to show progress indicator and to prevent additional firing of `onInfinite`
!-->
<template lang="jade">
.infinite-scroll
	bunt-progress-circular(v-if="loading", size="huge", :page="true")
</template>
<script>
/**
 * get current distance from footer
 */
function getCurrentDistance (el) {
	const styles = window.getComputedStyle(el)
	const innerHeight = parseInt(styles.height, 10)
	const scrollHeight = el.scrollHeight
	const scrollTop = isNaN(el.scrollTop) ? el.pageYOffset : el.scrollTop
	const paddingTop = parseInt(styles.paddingTop, 10)
	const paddingBottom = parseInt(styles.paddingBottom, 10)
	return scrollHeight - innerHeight - scrollTop - paddingTop - paddingBottom
}

export default {
	name: 'infinite-scroll',
	components: {},
	props: {
		distance: {
			type: Number,
			default: 100,
		},
		loading: Boolean
	},
	data () {
		return {
			scrollParent: null,
			isComplete: false,
			isLocked: false,
		}
	},
	computed: {},
	created () {},
	mounted () {
		this.$nextTick(() => {
			this.scrollParent = this.$el.parentElement
			this.scrollParent.addEventListener('scroll', this.scrollHandler)
			this.scrollHandler()
		})
	},
	methods: {
		scrollHandler () {
			const currentDistance = getCurrentDistance(this.scrollParent)
			if (!this.loading && !this.isComplete && currentDistance <= this.distance) {
				// this.isLocked = true
				this.$emit('infinite')
			}
		},
		lock () {
			this.isLocked = true
		},
		unlock () {
			this.isLocked = false
		}
	},
	destroyed () {
		if (!this.isComplete && this.scrollParent)
			this.scrollParent.removeEventListener('scroll', this.scrollHandler)
	}
}
</script>
<style lang="stylus">
</style>
