import moment from 'moment'
moment.locale('de')

const plenumForWeek = (date) => {
	if (date.week() % 2 === 0) {
		date.day('Donnerstag')
	} else {
		date.day('Mittwoch')
	}
	date.set('hour', 20)
}

export { plenumForWeek }

export function nextPlenum () {
	const plenumDate = moment().startOf('week')
	plenumForWeek(plenumDate)
	if (moment().isAfter(plenumDate, 'day')) {
		plenumDate.day(8)
		plenumForWeek(plenumDate)
	}
	return plenumDate
}
