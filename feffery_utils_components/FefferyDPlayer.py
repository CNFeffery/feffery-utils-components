# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDPlayer(Component):
    """A FefferyDPlayer component.


Keyword arguments:

- id (string; optional)

- airplay (boolean; default False)

- autoplay (boolean; default False)

- cancelFullScreenClicks (number; default 0)

- chromecast (boolean; default False)

- className (string; optional)

- clearDanmaku (boolean; default False)

- clearDanmakuClicks (number; default 0)

- contextmenu (list of dicts; optional)

    `contextmenu` is a list of dicts with keys:

    - icon (a list of or a singular dash component, string or number; optional)

    - key (string; optional)

    - text (string; optional)

- contextmenuHideClicks (number; default 0)

- contextmenuShowClicks (number; default 0)

- currentClickContextmenu (dict; optional)

- currentNoticeInfo (dict; optional)

- currentVideoInfo (dict; optional)

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

- destroy (boolean; default False)

- destroyClicks (number; default 0)

- drawDanmaku (dict; default {    isDraw: False})

    `drawDanmaku` is a dict with keys:

    - content (dict; optional)

        `content` is a dict with keys:

        - color (string; optional)

        - text (string; optional)

        - type (a value equal to: 'top', 'bottom', 'right'; optional)

    - isDraw (boolean; optional)

- drawDanmakuClicks (number; default 0)

- fullScreen (dict; default {    isFullScreen: False,    type: 'browser'})

    `fullScreen` is a dict with keys:

    - isFullScreen (boolean; optional)

    - operate (a value equal to: 'request', 'cancel'; optional)

    - type (a value equal to: 'web', 'browser'; optional)

- fullScreenClicks (number; default 0)

- hideDanmaku (boolean; default False)

- hideDanmakuClicks (number; default 0)

- hideNoticeClicks (number; default 0)

- highlight (list of dicts; optional)

    `highlight` is a list of dicts with keys:

    - text (string; optional)

    - time (number; optional)

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

- notice (dict; default {    isShow: False,    time: 2000,    opacity: 0.8})

    `notice` is a dict with keys:

    - isShow (boolean; optional)

    - opacity (number; optional)

    - text (string; optional)

    - time (number; optional)

- opacityDanmaku (dict; default {    isOpacity: False})

    `opacityDanmaku` is a dict with keys:

    - isOpacity (boolean; optional)

    - opacity (number; optional)

- opacityDanmakuCallback (dict; default {    opacityDanmakuClicks: 0})

    `opacityDanmakuCallback` is a dict with keys:

    - opacity (number; optional)

    - opacityDanmakuClicks (number; optional)

- pause (boolean; default False)

- pauseClicks (number; default 0)

- play (boolean; default False)

- playClicks (number; default 0)

- playbackSpeed (list of numbers; default [0.5, 0.75, 1, 1.25, 1.5, 2])

- preload (a value equal to: 'none', 'metadata', 'auto'; default 'auto')

- preventClickToggle (boolean; default False)

- screenshot (boolean; default False)

- screenshotClicks (number; default 0)

- seek (dict; default {    isSeek: False})

    `seek` is a dict with keys:

    - isSeek (boolean; optional)

    - time (number; optional)

- seekClicks (number; default 0)

- sendDanmaku (dict; default {    isSend: False})

    `sendDanmaku` is a dict with keys:

    - content (dict; optional)

        `content` is a dict with keys:

        - color (string; optional)

        - text (string; optional)

        - type (a value equal to: 'top', 'bottom', 'right'; optional)

    - isSend (boolean; optional)

- sendDanmakuCallback (dict; default {    sendDanmakuClicks: 0})

    `sendDanmakuCallback` is a dict with keys:

    - sendDanmakuClicks (number; optional)

    - sendInfo (dict; optional)

- showDanmaku (boolean; default False)

- showDanmakuClicks (number; default 0)

- showNoticeClicks (number; default 0)

- speed (dict; default {    isSpeed: False})

    `speed` is a dict with keys:

    - isSpeed (boolean; optional)

    - rate (number; optional)

- speedClicks (number; default 0)

- style (dict; optional)

- subtitle (dict; default {    isOpen: False,    type: 'webvtt',    fontSize: '20px',    bottom: '40px',    color: '#fff'})

    `subtitle` is a dict with keys:

    - bottom (string; optional)

    - color (string; optional)

    - fontSize (string; optional)

    - isOpen (boolean; optional)

    - type (a value equal to: 'webvtt', 'ass'; optional)

    - url (string; optional)

- subtitleChangeClicks (number; default 0)

- subtitleHideClicks (number; default 0)

- subtitleShowClicks (number; default 0)

- switchQuality (dict; default {    isSwitch: False})

    `switchQuality` is a dict with keys:

    - index (number; optional)

    - isSwitch (boolean; optional)

- switchVideo (dict; default {    isSwitch: False})

    `switchVideo` is a dict with keys:

    - danmaku (dict; optional)

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

    - isSwitch (boolean; optional)

    - video (dict; optional)

        `video` is a dict with keys:

        - customType (dict; optional)

        - defaultQuality (number; optional)

        - pic (string; optional)

        - quality (list of dicts; optional)

            `quality` is a list of dicts with keys:

    - name (string; optional)

    - type (a value equal to: 'auto', 'hls', 'flv', 'dash', 'normal'; optional)

    - url (string; optional)

        - thumbnails (string; optional)

        - type (a value equal to: 'auto', 'hls', 'flv', 'dash', 'normal'; optional)

        - url (string; optional)

- theme (string; default '#b7daff')

- video (dict; default {    type: 'auto'})

    `video` is a dict with keys:

    - customType (dict; optional)

    - defaultQuality (number; optional)

    - pic (string; optional)

    - quality (list of dicts; optional)

        `quality` is a list of dicts with keys:

        - name (string; optional)

        - type (a value equal to: 'auto', 'hls', 'flv', 'dash', 'normal'; optional)

        - url (string; optional)

    - thumbnails (string; optional)

    - type (a value equal to: 'auto', 'hls', 'flv', 'dash', 'normal'; optional)

    - url (string; optional)

- volume (number; default 0.7)

- volumeSet (dict; default {    isVolume: False,    nostorage: True,    nonotice: False})

    `volumeSet` is a dict with keys:

    - isVolume (boolean; optional)

    - nonotice (boolean; optional)

    - nostorage (boolean; optional)

    - percentage (number; optional)

- volumeSetClicks (number; default 0)"""
    _children_props = ['contextmenu[].icon']
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDPlayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, live=Component.UNDEFINED, autoplay=Component.UNDEFINED, theme=Component.UNDEFINED, loop=Component.UNDEFINED, lang=Component.UNDEFINED, screenshot=Component.UNDEFINED, airplay=Component.UNDEFINED, hotkey=Component.UNDEFINED, chromecast=Component.UNDEFINED, preload=Component.UNDEFINED, volume=Component.UNDEFINED, playbackSpeed=Component.UNDEFINED, logo=Component.UNDEFINED, preventClickToggle=Component.UNDEFINED, video=Component.UNDEFINED, subtitle=Component.UNDEFINED, danmaku=Component.UNDEFINED, contextmenu=Component.UNDEFINED, highlight=Component.UNDEFINED, mutex=Component.UNDEFINED, play=Component.UNDEFINED, pause=Component.UNDEFINED, seek=Component.UNDEFINED, notice=Component.UNDEFINED, speed=Component.UNDEFINED, volumeSet=Component.UNDEFINED, fullScreen=Component.UNDEFINED, switchQuality=Component.UNDEFINED, switchVideo=Component.UNDEFINED, sendDanmaku=Component.UNDEFINED, drawDanmaku=Component.UNDEFINED, opacityDanmaku=Component.UNDEFINED, clearDanmaku=Component.UNDEFINED, hideDanmaku=Component.UNDEFINED, showDanmaku=Component.UNDEFINED, destroy=Component.UNDEFINED, playClicks=Component.UNDEFINED, pauseClicks=Component.UNDEFINED, seekClicks=Component.UNDEFINED, showNoticeClicks=Component.UNDEFINED, hideNoticeClicks=Component.UNDEFINED, speedClicks=Component.UNDEFINED, volumeSetClicks=Component.UNDEFINED, fullScreenClicks=Component.UNDEFINED, cancelFullScreenClicks=Component.UNDEFINED, sendDanmakuCallback=Component.UNDEFINED, drawDanmakuClicks=Component.UNDEFINED, clearDanmakuClicks=Component.UNDEFINED, opacityDanmakuCallback=Component.UNDEFINED, showDanmakuClicks=Component.UNDEFINED, hideDanmakuClicks=Component.UNDEFINED, subtitleShowClicks=Component.UNDEFINED, subtitleHideClicks=Component.UNDEFINED, subtitleChangeClicks=Component.UNDEFINED, screenshotClicks=Component.UNDEFINED, contextmenuShowClicks=Component.UNDEFINED, contextmenuHideClicks=Component.UNDEFINED, currentClickContextmenu=Component.UNDEFINED, destroyClicks=Component.UNDEFINED, currentNoticeInfo=Component.UNDEFINED, currentVideoInfo=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'airplay', 'autoplay', 'cancelFullScreenClicks', 'chromecast', 'className', 'clearDanmaku', 'clearDanmakuClicks', 'contextmenu', 'contextmenuHideClicks', 'contextmenuShowClicks', 'currentClickContextmenu', 'currentNoticeInfo', 'currentVideoInfo', 'danmaku', 'destroy', 'destroyClicks', 'drawDanmaku', 'drawDanmakuClicks', 'fullScreen', 'fullScreenClicks', 'hideDanmaku', 'hideDanmakuClicks', 'hideNoticeClicks', 'highlight', 'hotkey', 'lang', 'live', 'loading_state', 'logo', 'loop', 'mutex', 'notice', 'opacityDanmaku', 'opacityDanmakuCallback', 'pause', 'pauseClicks', 'play', 'playClicks', 'playbackSpeed', 'preload', 'preventClickToggle', 'screenshot', 'screenshotClicks', 'seek', 'seekClicks', 'sendDanmaku', 'sendDanmakuCallback', 'showDanmaku', 'showDanmakuClicks', 'showNoticeClicks', 'speed', 'speedClicks', 'style', 'subtitle', 'subtitleChangeClicks', 'subtitleHideClicks', 'subtitleShowClicks', 'switchQuality', 'switchVideo', 'theme', 'video', 'volume', 'volumeSet', 'volumeSetClicks']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'airplay', 'autoplay', 'cancelFullScreenClicks', 'chromecast', 'className', 'clearDanmaku', 'clearDanmakuClicks', 'contextmenu', 'contextmenuHideClicks', 'contextmenuShowClicks', 'currentClickContextmenu', 'currentNoticeInfo', 'currentVideoInfo', 'danmaku', 'destroy', 'destroyClicks', 'drawDanmaku', 'drawDanmakuClicks', 'fullScreen', 'fullScreenClicks', 'hideDanmaku', 'hideDanmakuClicks', 'hideNoticeClicks', 'highlight', 'hotkey', 'lang', 'live', 'loading_state', 'logo', 'loop', 'mutex', 'notice', 'opacityDanmaku', 'opacityDanmakuCallback', 'pause', 'pauseClicks', 'play', 'playClicks', 'playbackSpeed', 'preload', 'preventClickToggle', 'screenshot', 'screenshotClicks', 'seek', 'seekClicks', 'sendDanmaku', 'sendDanmakuCallback', 'showDanmaku', 'showDanmakuClicks', 'showNoticeClicks', 'speed', 'speedClicks', 'style', 'subtitle', 'subtitleChangeClicks', 'subtitleHideClicks', 'subtitleShowClicks', 'switchQuality', 'switchVideo', 'theme', 'video', 'volume', 'volumeSet', 'volumeSetClicks']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDPlayer, self).__init__(**args)
