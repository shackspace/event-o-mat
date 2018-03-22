import Vue from 'vue'
import PerfectScrollbar from 'perfect-scrollbar'
import 'perfect-scrollbar/css/perfect-scrollbar.css'

// usage
//
// `v-scrollbar` | `v-scrollbar.x.y` : scrolling both axis
// `v-scrollbar.x` | `v-scrollbar.y' : scrolling one axis`
// CAUTION: in jade, you need to use `v-scrollbar.x=''` (empty value)
// set the value `v-scrollbar="VALUE"` to trigger a scrollbar update on value change
Vue.directive('scrollbar', {
	bind (el, binding) {
		const scrollX = binding.modifiers.x
		const scrollY = binding.modifiers.y
		Vue.nextTick(() => {
			el.__nagini__ = {
				scrollbar: new PerfectScrollbar(el, {
					suppressScrollX: (scrollY || scrollX) && !scrollX,
					suppressScrollY: (scrollY || scrollX) && !scrollY
				})
			}
		})
	},
	update (el, binding) {
		if (!el.__nagini__?.scrollbar) return
		Vue.nextTick(() => {
			el.__nagini__.scrollbar.update()
		})
	}
})

Vue.directive('truncate', function (el, binding) {
	el.classList.add('truncated')
	el.title = el.textContent
})
