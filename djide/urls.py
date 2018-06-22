from django.conf.urls import include, url
from djide.views import edit,tree_data,model_editor
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#
urlpatterns = [
    url(r'^$', edit, name='edit'),
    url(r'^tree-data$', tree_data, name='treedata'),
    url(r'^model-editor', model_editor, name='modeleditor'),
]
