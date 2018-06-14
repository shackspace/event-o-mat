<template lang="jade">
.c-event-form
	.actions
		bunt-button#delete(v-if="!creation", @click="confirmDelete = true") delete
		.form-actions
			bunt-button#create(@click="save", :loading="saving", :error!="errorSaving", :error-message="error") {{ creation ? 'create' : 'save' }}
			bunt-link-button(v-if="!creation", :to="{name: 'events:item', params: {id: event.id}}", @click="restore") cancel
	.scroll(v-scrollbar.y="")
		bunt-input(name="name", label="Event Name", v-model="event.name", :validation="$v.event.name")
		datepicker(name="start", label="Start Date/Time", v-model="event.start", :validation="$v.event.start")
		datepicker(name="end", label="End Date/Time", v-model="event.end", :validation="$v.event.end")
		bunt-select(name="room", label="Room", v-model="event.room", :options="rooms", option-label="name", option-value="id", :validation="$v.event.room")
		bunt-input(name="keyholder", label="Keyholder(s)", v-model="event.keyholder")
		bunt-switch(name="publish", v-model="event.publish", label="Announce to website?")
		p Description:
		.description
			textarea(v-model="event.description")
		a(href="https://guides.github.com/features/mastering-markdown/", title: "mardown cheatsheet", target="_blank") you can format your description with markdown
	bunt-dialog.event-form-dialog(:open="confirmDelete", @close="confirmDelete = false")
		h1 Do you really want to delete this event?
		.confirm-actions
			bunt-button#cancel-delete(@click="confirmDelete = false") cancel
			bunt-button#confirm-delete(@click="deleteEvent", :loading="deleting", :error-message="deleteError") delete
</template>
<script>
import { mapState } from 'vuex'
import api from 'lib/api'
import { required } from 'buntpapier/src/vuelidate/validators'
import { apiValidator, apiValidatorMixin } from 'components/mixins/api-error-validation'
import Datepicker from 'components/datepicker'

export default {
	components: { Datepicker },
	mixins: [apiValidatorMixin],
	props: {
		event: Object,
		creation: {
			type: Boolean,
			default: false
		}
	},
	data () {
		return {
			saving: false,
			error: null,
			errorSaving: false,
			backup: null,
			deleting: false,
			confirmDelete: false,
			deleteError: null
		}
	},
	validations () {
		return {
			event: {
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
		this.backup = Object.assign({}, this.event)
		this.backup.start = this.backup.start.clone()
		this.backup.end = this.backup.end.clone()
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
			const event = Object.assign({}, this.event)
			event.start = event.start.format()
			event.end = event.end.format()
			api.events[this.creation ? 'create' : 'update'](event).then((event) => {
				this.$router.push({name: 'events:item', params: {id: event.id}})
				this.clearApiErrors()
			}).catch((error) => {
				this.saving = false
				this.errorSaving = true
				this.handleApiErrors(error)
				if (error.json.detail) {
					this.error = error.json.detail
				}
			})
		},
		restore () {
			Object.assign(this.event, this.backup)
		},
		deleteEvent () {
			this.deleting = true
			api.events.delete(this.event).then(() => {
				this.$router.push({name: 'events'})
			}).catch((error) => {
				this.deleting = false
				this.deleteError = error.json.detail
			})
		}
	}
}
</script>
<style lang="stylus">
@import '~_settings'
.c-event-form
	display: flex
	flex-direction: column
	flex: 1 1 50vw
	padding: 32px 64px 0
	box-sizing: border-box
	.scroll
		padding: 16px 0
		position: relative
	.bunt-input
		width: 25vw
		min-width: 240px
		.hint
			ellipsis()
			overflow: visible
	.description
		flex: 1
		position: relative
		border: 2px solid $clr-grey
		display: flex
	textarea
		flex: 1
		resize: none
		border: none
		min-height: 512px
	> .actions
		display: flex
		flex: 0 0 auto
		padding-bottom: 24px
		justify-content: space-between
	#delete
		button-style(color: $clr-danger)
	#create
		button-style(color: $clr-primary)
		width: 128px
		margin: 0 8px
	.preview
		flex: 1
.bunt-dialog
	padding: 16px
	display: flex
	flex-direction: column
	align-items: center

	.confirm-actions
		align-self: flex-end
		#confirm-delete
			button-style(color: $clr-danger)
		#cancel-delete
			button-style(style: 'clear')
			margin-right: 8px
</style>
