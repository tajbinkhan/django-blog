JAZZMIN_SETTINGS = {
	"site_title": "Django Blog Administration",
	"site_header": "Django Blog Administration",
	"site_brand": "Blog Administration",
	"site_icon": "blog/img/favicon.ico",
	# Add your own branding here
	"site_logo": "blog/img/favicon.ico",
	"welcome_sign": "Welcome to the Django Blog",
	# Copyright on the footer
	"copyright": "Django Blog",
	# "user_avatar": "blog/img/favicon.ico",
	#############
	# Side Menu #
	"topmenu_links": [
		# Url that gets reversed (Permissions can be added)
		{"name": "Visit Website",  "url": "/", "new_window": True, "permissions": ["auth.view_user"]},
	],
	#############
	# Whether to display the side menu
	"show_sidebar": True,
	# Whether to aut expand the menu
	"navigation_expanded": True,
	# Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
	# for the full list of 5.13.0 free icon classes
	"icons": {
		"auth": "fas fa-users-cog",
		"auth.user": "fas fa-user",
		"users.User": "fas fa-user",
		"auth.Group": "fas fa-users",
		"auth.Permission": "fas fa-user-lock",
		"admin.LogEntry": "fas fa-file",
		"blog.Category": "fas fa-clipboard-list",
		"blog.Post": "fas fa-blog",
		"blog.Comment": "fas fa-comments",
		'site_setting.AllSetting': "fas fa-toolbox",
		'site_setting.EmailContent': "fas fa-envelope",
		'user.Profile': "fas fa-user-check",
		'account.EmailAddress': "fas fa-at",
		'socialaccount.SocialAccount': "fas fa-share-alt",
		'socialaccount.SocialToken': "fas fa-coins",
		'socialaccount.SocialApp': "fas fa-people-arrows",
	},
	# # Icons that are used when one is not manually specified
	"default_icon_parents": "fas fa-chevron-circle-right",
	"default_icon_children": "fas fa-arrow-circle-right",
	#################
	# Related Modal #
	#################
	# Use modals instead of popups
	"related_modal_active": False,
	#############
	# UI Tweaks #
	#############
	# Relative paths to custom CSS/JS scripts (must be present in static files)
	# Uncomment this line once you create the bootstrap-dark.css file
	# "custom_css": "css/bootstrap-dark.css",
	"custom_js": None,
	# Whether to show the UI customizer on the sidebar
	"show_ui_builder": False,
	###############
	# Change view #
	###############
	"changeform_format": "horizontal_tabs",
	# override change forms on a per modeladmin basis
	"changeform_format_overrides": {
		"auth.user": "collapsible",
		"auth.group": "vertical_tabs",
	},
}