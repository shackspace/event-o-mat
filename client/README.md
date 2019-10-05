# event-o-mat frontend


## Developing
event-o-mat uses npm for everything™:

```
npm install
npm start
cp config.stage.js config.dev.js
```

Note: The client builds fine using nodejs-lts (currently at v10.16.3)

## Folder structure
```
┣━━ build: webpack configs and build scripts
┣━━ src: all the code
┃   ┣━━ assets: static files
┃   ┣━━ components: reusable vue components
┃   ┣━━ lib: plain js modules
┃   ┣━━ store: vuex store, mutators, getters, etc
┃   ┣━━ styles: global styles and stylus modules
┃   ┣━━ views: vue components for specific routes (folder structure follows route url)
┃   ┣━━ App.vue: base layout for everything after login
┃   ┣━━ router.js: all the routes
┃   ┣━━ main.js: app entry point
┃   ┣━━ main.vue: "body" component, only contains the root router-view
```

## Conventions

event-o-mat uses three languages:

### JavaScript
Currently ES2015 and Stage-3 features, as provided by babel.  
Linting is done with Eslint and a slightly customized standard.js.  
Listen to the Linter.

### Jade Templates
Jade compiles down to HTML.
Vue templates are all in jade/pug.  
Has no linting.

#### Jade guide
Always use `.class` and `#id` for static defines.

Right:
```
button#btn-save.active
```
Wrong:
```
button(id="btn-save", class="active")
```

Always use vue binding shorthands `:` and `@` instead of `v-bind:` and `v-on:`

Set html attributes in the following order (first to last):
- `v-if` / `v-show`
- `v-for`
- `key`
- `:id`
- `:class`
- `:style`
- `v-model`
- `:value`
- component props
- event bindings

Avoid trailing whitespaces by using tag interpolation:
```
p This is an #[a(href="#") inline link] with spaces around it.
```

### Stylus
Stylus is a preprocessor for CSS, like SASS or LESS.  
Has no linter.

#### Stylus guide
- don't use `{} or ;`
- use `: ` between property and value
- prefix variables with `$`

#### Stylus example
```stylus
nav.toolbar
	/*flex 1*/
	card()
	height: 52px
	z-index: 100
	background-color: $ax-primary

	.top-container
		display: flex
		justify-content: space-between

	.actions
		display: flex
		align-items: center
		margin-right: 16px

	h1
		color: $clr-primary-text-dark
		margin: 8px 16px
		font-size: 20px
		font-weight: 300

		.name
			font-weight: 400
```


##### How to Find Color Variables
Colors are prefixed with `$clr-`.
Find existing colors from:
- https://github.com/rashfael/buntpapier/blob/master/buntpapier/variables.styl
- https://github.com/rashfael/buntpapier/blob/master/buntpapier/colors.styl (mapping https://www.materialui.co/colors)
- for text colors, use `$clr-[primary,secondary,disabled,dividers]-text-[light,dark]` (These greys are defined with alpha on black or white and work better on various backgrounds, use `light` for light backgrounds and `dark` for dark backgrounds)


### Vue Files
`.vue` files combine ES, jade template and stylus sheets into one file.  
The template gets used as component templates.  
The stylus sheet is NOT scoped, so ALWAYS use a fitting root selector (for example the component root element class).
