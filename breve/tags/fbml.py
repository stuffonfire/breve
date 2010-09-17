# automatically generated by xsd2breve
# modified for href rewriting
import breve.tags
import breve.tags._ext

xmlns = "file:///Users/dwy/Developer/com.artichokelabs/aws/fbml.xsd"
doctype = ""
tag_names = ['action', 'bookmark', 'create-button', 'dashboard', 'default', 'dialog', 'dialog-button', 'dialog-content', 'dialog-title', 'dialogresponse', 'editor', 'editor-button', 'editor-buttonset', 'editor-cancel', 'editor-custom', 'editor-date', 'editor-divider', 'editor-month', 'editor-text', 'editor-textarea', 'editor-time', 'else', 'error', 'explanation', 'fan', 'fbml', 'fbmlversion', 'flv', 'friend-selector', 'google-analytics', 'header', 'help', 'if-can-see', 'if-can-see-photo', 'if-is-app-user', 'if-is-friends-with-viewer', 'if-is-group-member', 'if-is-own-profile', 'if-is-user', 'if-user-has-added-app', 'iframe', 'like', 'like-box', 'login-button', 'message', 'message-preview', 'mobile', 'mp3', 'multi-friend-input', 'multi-friend-selector', 'name', 'narrow', 'notif-email', 'notif-page', 'notif-subject', 'photo', 'profile-action', 'profile-pic', 'pronoun', 'query', 'redirect', 'ref', 'request-form', 'req-choice', 'serverfbml', 'share-button', 'silverlight', 'submit', 'subtitle', 'success', 'swf', 'switch', 'tab-item', 'tabs', 'time', 'title', 'user', 'user-item', 'user-link', 'user-table', 'username', 'wall', 'wallpost', 'wallpost-action', 'wide']

tag_names = ['fb:' + tag for tag in tag_names]
tags = {}

def fbmlize(t):
	tx = breve.tags._ext.pythonize(t)
	tags[tx] = breve.tags.custom_tag(t, flattener=breve.tags.flatten_tag)
	return tags[tx]

map(fbmlize, tag_names)
