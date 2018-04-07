<!-- routes to internal event or plenumslink -->
<template lang="jade">
a(v-if="event.plenumLink", :href="event.plenumLink")
	slot
router-link(v-else, :to="{name: 'events:item', params: {id: event.id}}")
	slot
</template>
<script>
export default {
	props: {
		event: Object
	}
}
</script>
<style lang="stylus">
</style>
