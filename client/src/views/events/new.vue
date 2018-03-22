<template lang="jade">
.c-new-event
	bunt-input(name="name", label="Event Name", v-model="formData.name")
	bunt-input(name="description", label="Description", v-model="formData.description")
	bunt-button(@click.native="create", :loading="sending") create
</template>
<script>
import api from 'lib/api'

export default {
	components: {},
	data () {
		return {
			formData: {
				name: '',
				description: ''
			},
			sending: false
		}
	},
	computed: {},
	created () {},
	mounted () {
		this.$nextTick(() => {
		})
	},
	methods: {
		create () {
			this.sending = true
			api.events.create(formData).then((event) => {
				this.$router.push({name: 'event:item', params: {id: event.id}})
			})
		}
	}
}
</script>
<style lang="stylus">
</style>
