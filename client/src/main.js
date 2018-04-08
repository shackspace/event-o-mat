import Vue from 'vue'
import Router from 'vue-router'
import Buntpapier from 'buntpapier'
import Vuelidate from 'vuelidate'
import moment from 'moment'

import api from 'lib/api'
import store from 'store'
import routes from './routes'
import 'components/directives'
import 'components/filters'

import Main from './main.vue'
Vue.use(Router)
Vue.use(Buntpapier)
Vue.use(Vuelidate)

Vue.moment = moment

let router = new Router({
	mode: 'history',
	routes: routes
})

router.beforeEach((to, from, next) => {
	if (to.matched.some(record => record.meta.requiresAuth) && !api.auth.authenticated) {
		localStorage.setItem('redirectPath', `${window.location.pathname}`)
		next({path: '/login'})
	} else {
		next()
	}
})

Main.router = router
Main.store = store

window.api = api
window.moment = moment

api.auth.getSession().then(() => {
	console.log('initing!')
	new Vue(Main).$mount('#v-app')
	// restore url before login
	if (store.state.user.authenticated && localStorage.redirectPath) {
		router.replace(localStorage.redirectPath)
		localStorage.removeItem('redirectPath')
	}
}).catch((error) => {
	console.error(error)
	new Vue(Main).$mount('#v-app')
})
