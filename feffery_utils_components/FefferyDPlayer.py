# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDPlayer(Component):
    """A FefferyDPlayer component.


Keyword arguments:

- id (string; optional)

- airplay (boolean; default False)

- autoplay (boolean; default False)

- chromecast (boolean; default False)

- className (string; optional)

- contextmenu (list; optional)

- danmaku (dict; default {    isOpen: False,    unlimited: False,    speedRate: 1})

    `danmaku` is a dict with keys:

    - addition (list of strings; optional)

    - api (string; optional)

    - bottom (string; optional)

    - id (string; optional)

    - isOpen (boolean; optional)

    - maximum (number; optional)

    - speedRate (number; optional)

    - token (string; optional)

    - unlimited (boolean; optional)

    - user (string; optional)

- highlight (list; optional)

- hotkey (boolean; default True)

- lang (a value equal to: 'en', 'zh-cn', 'zh-tw'; default 'zh-cn')

- live (boolean; default False)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- logo (string; optional)

- loop (boolean; default False)

- mutex (boolean; default True)

- playbackSpeed (list of numbers; default [0.5, 0.75, 1, 1.25, 1.5, 2])

- preload (a value equal to: 'none', 'metadata', 'auto'; default 'auto')

- screenshot (boolean; default False)

- style (dict; optional)

- subtitle (dict; default {    isOpen: False,    type: 'webvtt',    fontSize: '20px',    bottom: '40px',    color: '#fff'})

    `subtitle` is a dict with keys:

    - bottom (string; optional)

    - color (string; optional)

    - fontSize (string; optional)

    - isOpen (boolean; optional)

    - type (a value equal to: 'webvtt', 'ass'; optional)

    - url (string; optional)

- theme (string; default '#b7daff')

- video (dict; default {    type: 'auto'})

    `video` is a dict with keys:

    - defaultQuality (number; optional)

    - pic (string; optional)

    - quality (list of dicts; optional)

        `quality` is a list of dicts with keys:

        - name (string; optional)

        - type (a value equal to: 'auto', 'hls', 'normal'; optional)

        - url (string; optional)

    - thumbnails (string; optional)

    - type (a value equal to: 'auto', 'hls', 'normal'; optional)

    - url (string; optional)

- volume (number; default 0.7)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDPlayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, live=Component.UNDEFINED, autoplay=Component.UNDEFINED, theme=Component.UNDEFINED, loop=Component.UNDEFINED, lang=Component.UNDEFINED, screenshot=Component.UNDEFINED, airplay=Component.UNDEFINED, hotkey=Component.UNDEFINED, chromecast=Component.UNDEFINED, preload=Component.UNDEFINED, volume=Component.UNDEFINED, playbackSpeed=Component.UNDEFINED, logo=Component.UNDEFINED, video=Component.UNDEFINED, subtitle=Component.UNDEFINED, danmaku=Component.UNDEFINED, contextmenu=Component.UNDEFINED, highlight=Component.UNDEFINED, mutex=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'airplay', 'autoplay', 'chromecast', 'className', 'contextmenu', 'danmaku', 'highlight', 'hotkey', 'lang', 'live', 'loading_state', 'logo', 'loop', 'mutex', 'playbackSpeed', 'preload', 'screenshot', 'style', 'subtitle', 'theme', 'video', 'volume']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'airplay', 'autoplay', 'chromecast', 'className', 'contextmenu', 'danmaku', 'highlight', 'hotkey', 'lang', 'live', 'loading_state', 'logo', 'loop', 'mutex', 'playbackSpeed', 'preload', 'screenshot', 'style', 'subtitle', 'theme', 'video', 'volume']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDPlayer, self).__init__(**args)
