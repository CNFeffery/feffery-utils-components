from __future__ import print_function as _

import os as _os
import sys as _sys
import json

import dash as _dash

# noinspection PyUnresolvedReferences
from ._imports_ import *  # noqa: F403
from ._imports_ import __all__

if not hasattr(_dash, '__plotly_dash') and not hasattr(_dash, 'development'):
    print('Dash was not successfully imported. '
          'Make sure you don\'t have a file '
          'named \n"dash.py" in your current directory.', file=_sys.stderr)
    _sys.exit(1)

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, 'package-info.json'))
with open(_filepath) as f:
    package = json.load(f)

package_name = package['name'].replace(' ', '_').replace('-', '_')
__version__ = package['version']

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_this_module = _sys.modules[__name__]

async_resources = [
    'fuc-shared',
    'feffery_captcha',
    'feffery_aplayer',
    'feffery_dplayer',
    'feffery_music_player',
    'feffery_emoji_picker',
    'feffery_auto_animate',
    'feffery_json_viewer',
    'feffery_resizable',
    'feffery_sortable',
    'feffery_local_large_storage',
    'feffery_color_pickers',
    'feffery_fancy_button',
    'feffery_extra_spinner',
    'feffery_shortcut_panel',
    'feffery_grid',
    'feffery_auto_fit',
    'feffery_rich_text_editor',
    'feffery_markdown_editor',
    'feffery_image_cropper',
    'feffery_photo_sphere_viewer',
    'feffery_excel_preview',
    'feffery_word_preview',
    'feffery_seamless_scroll',
    'feffery_animated_3d_background_three',
    'feffery_animated_3d_background_p5',
    'feffery_rnd',
    'feffery_animated_image',
    'feffery_motion',
    'feffery_dom2image',
    'feffery_slider_captcha',
    'feffery_vditor',
    'feffery_http_requests',
    'feffery_burger',
    'feffery_barcode'
]

_js_dist = []

_js_dist.extend(
    [
        {
            "relative_package_path": "async-{}.js".format(async_resource),
            "external_url": (
                "https://unpkg.com/{0}@{2}"
                "/{1}/async-{3}.js"
            ).format(package_name, __name__, __version__, async_resource),
            "namespace": package_name,
            "async": True,
        }
        for async_resource in async_resources
    ]
)

_js_dist.extend(
    [
        {
            "relative_package_path": "async-{}.js.map".format(async_resource),
            "external_url": (
                "https://unpkg.com/{0}@{2}"
                "/{1}/async-{3}.js.map"
            ).format(package_name, __name__, __version__, async_resource),
            "namespace": package_name,
            "dynamic": True,
        }
        for async_resource in async_resources
    ]
)

_js_dist.extend(
    [
        {
            'relative_package_path': 'feffery_utils_components.min.js',
            'external_url': 'https://unpkg.com/{0}@{2}/{1}/{1}.min.js'.format(
                package_name, __name__, __version__),
            'namespace': package_name
        },
        {
            'relative_package_path': 'feffery_utils_components.min.js.map',
            'external_url': 'https://unpkg.com/{0}@{2}/{1}/{1}.min.js.map'.format(
                package_name, __name__, __version__),
            'namespace': package_name,
            'dynamic': True
        }
    ]
)

_css_dist = []


for _component in __all__:
    setattr(locals()[_component], '_js_dist', _js_dist)
    setattr(locals()[_component], '_css_dist', _css_dist)
