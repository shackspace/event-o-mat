<template lang="jade">
.c-event-form
	bunt-input(name="name", label="Event Name", v-model="formData.name", :validation="$v.formData.name")
	bunt-input(name="description", label="Description", v-model="formData.description", :validation="$v.formData.description")
	bunt-input(name="start", label="Start Date/Time", v-model="formData.start", :validation="$v.formData.start")
	bunt-input(name="end", label="End Date/Time", v-model="formData.end", :validation="$v.formData.end")
	bunt-select(name="room", label="Room", v-model="formData.room", :options="rooms", option-label="name", option-value="id", :validation="$v.formData.room")
	bunt-button#create(@click.native="save", :loading="saving", :error!="errorSaving") create
</template>
<script>
import { mapState } from 'vuex'
import api from 'lib/api'
import { required } from 'buntpapier/src/vuelidate/validators'
import { apiValidator, apiValidatorMixin } from 'components/mixins/api-error-validation'

export default {
	components: {},
	mixins: [apiValidatorMixin],
	prop: {
		event: Object
	},
	data () {
		return {
			formData: {
				name: '',
				description: '',
				start: '',
				end: '',
				room: null
			},
			saving: false,
			errorSaving: false
		}
	},
	validations () {
		return {
			formData: {
				name: {
					apiValidator: apiValidator.bind(this)('name'),
					required: required('Events without names are pretty useless, eh?')
				},
				description: {
					apiValidator: apiValidator.bind(this)('description'),
				},
				start: {
					apiValidator: apiValidator.bind(this)('start'),
					required: required('event needs a start date')
				},
				end: {
					apiValidator: apiValidator.bind(this)('end'),
					required: required('event needs an end date')
				},
				room: {
					apiValidator: apiValidator.bind(this)('room'),
					required: required('need to choose a room!')
				}
			}
		}
	},
	computed: {
		...mapState(['rooms'])
	},
	created () {
		if (this.event) {
			this.formData = this.event
		}
	},
	mounted () {
		this.$nextTick(() => {
		})
	},
	methods: {
		save () {
			this.clearApiErrors()
			this.$v.$touch()
			if (this.$v.$invalid) return
			this.saving = true
			api.events[this.event ? 'update' : 'create'](this.formData).then((event) => {
				this.$router.push({name: 'events:item', params: {id: event.id}})
				this.clearApiErrors()
			}).catch((error) => {
				this.saving = false
				this.errorSaving = true
				this.handleApiErrors(error)
			})
		}
	}
}
</script>
<style lang="stylus">
@import '~_settings'
.c-new-event
	display: flex
	flex-direction: column
	align-items: center
	.bunt-input
		width: 25vw
		min-width: 240px
		.hint
			ellipsis()
			overflow: visible
	#create
		button-style(color: $clr-shack)
</style>
