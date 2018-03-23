// Use this mixin in components with vuelidate
// to support validation functions based on API error responses
//
// validator usage:
// componentField: apiValidator('API_FIELD_NAME')
// call `handleApiErrors(errorResponse)` after async api responses
// call `clearApiErrors` before a new request

import {withParams} from 'vuelidate/lib/validators/common'

const apiValidatorMixin = {
	data () {
		return {
			apiErrors: null
		}
	},
	methods: {
		clearApiErrors () {
			this.apiErrors = null
		},
		handleApiErrors (error) {
			if (error.response.status === 400) {
				this.apiErrors = error.json
				this.$v.$touch()
			}
		}
	}
}

const apiValidator = function (property) {
	return withParams((addParams) => {
		return () => {
			if (this.apiErrors) {
				addParams({message: this.apiErrors[property]})
			}
			return !(this.apiErrors && this.apiErrors[property])
		}
	})
}

export { apiValidator, apiValidatorMixin }
