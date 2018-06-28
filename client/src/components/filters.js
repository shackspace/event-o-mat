import Vue from 'vue'
import moment from 'moment'

const dateFormat = 'YYYY-MM-DD'
const datetimeFormat = 'YYYY-MM-DD HH:mm'
const timeFormat = 'HH:mm'
const humanDatetimeFormat = 'DD. MMM HH:mm'

Vue.filter('datetime', (date) => {
	return moment(date).format(datetimeFormat)
})

Vue.filter('humandatetime', (date) => {
	return moment(date).format(humanDatetimeFormat)
})

Vue.filter('date', (date) => {
	return moment(date).format(dateFormat)
})

Vue.filter('time', (date) => {
	return moment(date).format(timeFormat)
})

Vue.filter('fromnow', (date) => {
	return moment(date).fromNow()
})
Vue.filter('truncate', (str, length) => {
	return (str.length > length ? str.slice(0, length - 1) + '…' : str)
})
Vue.filter('times', (count) => {
	if (count === 1)
		return 'once'
	if (count === 2)
		return 'twice'
	return `${count} times`
})
