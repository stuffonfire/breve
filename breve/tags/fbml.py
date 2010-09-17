# automatically generated by xsd2breve
# modified for href rewriting
import breve.tags
import breve.tags._ext
import choke

xmlns = "file:///Users/dwy/Developer/com.artichokelabs/aws/fbml.xsd"
doctype = ""
tag_names = ['action', 'bookmark', 'create-button', 'dashboard', 'default', 'dialog', 'dialog-button', 'dialog-content', 'dialog-title', 'dialogresponse', 'editor', 'editor-button', 'editor-buttonset', 'editor-cancel', 'editor-custom', 'editor-date', 'editor-divider', 'editor-month', 'editor-text', 'editor-textarea', 'editor-time', 'else', 'error', 'explanation', 'fan', 'fbml', 'fbmlversion', 'flv', 'friend-selector', 'google-analytics', 'header', 'help', 'if-can-see', 'if-can-see-photo', 'if-is-app-user', 'if-is-friends-with-viewer', 'if-is-group-member', 'if-is-own-profile', 'if-is-user', 'if-user-has-added-app', 'iframe', 'like', 'like-box', 'login-button', 'message', 'message-preview', 'mobile', 'mp3', 'multi-friend-input', 'multi-friend-selector', 'name', 'narrow', 'notif-email', 'notif-page', 'notif-subject', 'photo', 'profile-action', 'profile-pic', 'pronoun', 'query', 'redirect', 'ref', 'request-form', 'req-choice', 'serverfbml', 'share-button', 'silverlight', 'submit', 'subtitle', 'success', 'swf', 'switch', 'tab-item', 'tabs', 'time', 'title', 'user', 'user-item', 'user-link', 'user-table', 'username', 'wall', 'wallpost', 'wallpost-action', 'wide']

tag_names = ['fb:' + tag for tag in tag_names]
tags = {}

tls = choke.ALThreadStorage(rewrite={
	'base': [], # replace with your application url, e.g. apps.facebook.com/crap
	'callback': [], # replace with your callback url, e.g. yourdomain.com/crap
	'app-relative': ['href', 'action'],
	'callback-relative': ['clickrewriteurl'],
})

def prependIfNeeded(value, segments):
	if value.startswith('/'):
		value = filter(None, value.split('/'))
		value = segments + value
		value = '/'.join(value)
	return value

def appTagFlattener(tag):
	if tls.rewrite['base']:
		for attribute in tls.rewrite['app-relative']:
			value = tag.attrs.get(attribute, '')
			if value:
				tag.attrs[attribute] = prependIfNeeded(value, tls.rewrite['base'])
	if tls.rewrite['callback']:
		for attribute in tls.rewrite['callback-relative']:
			value = tag.attrs.get(attribute, '')
			if value:
				tag.attrs[attribute] = prependIfNeeded(value, tls.rewrite['callback'])
	return breve.tags.flatten_tag(tag)

def fbmlize(t):
	tx = breve.tags._ext.pythonize(t)
	tags[tx] = breve.tags.custom_tag(t, flattener=breve.tags.flatten_tag)
	return tags[tx]

map(fbmlize, tag_names)
