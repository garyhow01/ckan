import logging

import ckan.plugins as p
from ckan.lib.navl.validators import ignore_empty

from ckan.common import json

log = logging.getLogger(__name__)

try:
    import ckanext.resourceproxy.plugin as proxy
except ImportError:
    pass

DEFAULT_IMAGE_FORMATS = ['png', 'jpeg', 'jpg', 'gif']


class ImageView(p.SingletonPlugin):
    '''This extenstion makes views of images'''

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'theme/templates')

    def info(self):
        return {'name': 'image',
                'title': 'Image',
                'schema': {'image_url': [ignore_empty, unicode]},
                'form_template': 'image_form.html'}

    def can_preview(self, data_dict):
        return True

    def setup_template_variables(self, context, data_dict):
        return

    def preview_template(self, context, data_dict):
        return 'image.html'
