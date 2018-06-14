<template lang="jade">
.c-series-form
	.actions
		bunt-button#delete(v-if="!creation", @click="confirmDelete = true") delete
		.form-actions
			bunt-button#create(@click="save", :loading="saving", :error!="errorSaving", :error-message="error") {{ creation ? 'create' : 'save' }}
			bunt-link-button(v-if="!creation", :to="{name: 'series:item', params: {id: series.id}}", @click="restore") cancel
	.scroll(v-scrollbar.y="")
		bunt-input(name="name", label="Series Name", v-model="series.name", :validation="$v.series.name")
		bunt-input(name="start", label="Start Time", v-model="series.start", :validation="$v.series.start")
		bunt-input(name="end", label="End Time", v-model="series.end", :validation="$v.series.end")
		bunt-select(name="room", label="Room", v-model="series.room", :options="rooms", option-label="name", option-value="id", :validation="$v.series.room")
		bunt-input(name="keyholder", label="Keyholder(s)", v-model="series.keyholder")
		bunt-input(name="rrule", label="Recurrence Rule", v-model="series.rrule", :validation="$v.series.rrule", hint="uses the <a href='https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html' target='_blank'>ical rrule format</a>. (DTSTART is not needed)", :hint-is-html="true")
		p
		p Description:
		.description
			textarea(v-model="series.description")
		a(href="https://guides.github.com/features/mastering-markdown/", title: "mardown cheatsheet", target="_blank") you can format your description with markdown
	bunt-dialog.series-form-dialog(:open="confirmDelete", @close="confirmDelete = false")
		h1 Do you really want to delete this series?
		.confirm-actions
			bunt-button#cancel-delete(@click="confirmDelete = false") cancel
			bunt-button#confirm-delete(@click="deleteSeries", :loading="deleting", :error-message="deleteError") delete
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
		series: Object,
		creation: {
			type: Boolean,
			default: false
		}
	},
	data () {
		return {
			backup: null,
			saving: false,
			error: null,
			errorSaving: false,
			deleting: false,
			confirmDelete: false,
			deleteError: null
		}
	},
	validations () {
		return {
			series: {
				name: {
					apiValidator: apiValidator.bind(this)('name'),
					required: required('Series without names are pretty useless, eh?')
				},
				description: {
					apiValidator: apiValidator.bind(this)('description'),
				},
				start: {
					apiValidator: apiValidator.bind(this)('start'),
					required: required('series needs a start date')
				},
				end: {
					apiValidator: apiValidator.bind(this)('end'),
					required: required('series needs an end date')
				},
				room: {
					apiValidator: apiValidator.bind(this)('room'),
					required: required('need to choose a room!')
				},
				rrule: {
					apiValidator: apiValidator.bind(this)('rrule'),
					required: required('no recurrence without a rule!')
				}
			}
		}
	},
	computed: {
		...mapState(['rooms'])
	},
	created () {
		this.backup = Object.assign({}, this.series)
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
			this.errorSaving = false
			api.series[this.creation ? 'create' : 'update'](this.series).then((series) => {
				this.$router.push({name: 'series:edit', params: {id: series.id}})
				this.clearApiErrors()
				this.saving = false
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
		deleteSeries () {
			this.deleting = true
			api.series.delete(this.series).then(() => {
				this.$router.push({name: 'series'})
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
.c-series-form
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
