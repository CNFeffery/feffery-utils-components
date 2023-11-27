# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyAPlayer(Component):
    """A FefferyAPlayer component.


Keyword arguments:

- id (string; optional)

- addList (dict; default {    isAdd: False})

    `addList` is a dict with keys:

    - audio (list of dicts; optional)

        `audio` is a list of dicts with keys:

        - artist (string; optional)

        - cover (string; optional)

        - lrc (string; optional)

        - name (string; optional)

        - theme (string; optional)

        - type (a value equal to: 'auto', 'hls', 'normal'; optional)

        - url (string; optional)

    - isAdd (boolean; optional)

- audio (list of dicts; default {    type: 'auto'})

    `audio` is a list of dicts with keys:

    - artist (string; optional)

    - cover (string; optional)

    - lrc (string; optional)

    - name (string; optional)

    - theme (string; optional)

    - type (a value equal to: 'auto', 'hls', 'normal'; optional)

    - url (string; optional)

- autoplay (boolean; default False)

- className (string; optional)

- clearList (boolean; default False)

- currentListAddAudioInfo (dict; optional)

- currentListRemoveAudioInfo (dict; optional)

- currentListSwitchAudioInfo (dict; optional)

- currentNoticeInfo (dict; optional)

- currentPauseAudioInfo (dict; optional)

- currentPlayAudioInfo (dict; optional)

- currentSeekAudioInfo (dict; optional)

- destroy (boolean; default False)

- destroyClicks (number; default 0)

- fixed (boolean; default False)

- hideList (boolean; default False)

- hideLrc (boolean; default False)

- hideLrcClicks (number; default 0)

- hideNoticeClicks (number; default 0)

- listAddClicks (number; default 0)

- listClearClicks (number; default 0)

- listFolded (boolean; default False)

- listHideClicks (number; default 0)

- listMaxHeight (number; optional)

- listRemoveClicks (number; default 0)

- listShowClicks (number; default 0)

- listSwitchClicks (number; default 0)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- loop (a value equal to: 'all', 'one', 'none'; default 'all')

- lrcType (a value equal to: 0, 1, 2, 3; default 0):
    有三种方式来给APlayer传递歌词，使用lrcType参数指明使用哪种方式，然后把歌词放到audio.lrc参数或者HTML里
    1表示把歌词放到JS字符串里面，2表示把歌词放到HTML里面，3表示把歌词放到 LRC 文件里，音频播放时会加载对应的 LRC 文件
    audio.lrc支持下面格式的歌词：  [mm:ss]APlayer[mm:ss.xx]is
    [mm:ss.xxx]amazing  [mm:ss.xx][mm:ss.xx]APlayer
    [mm:ss.xx]<mm:ss.xx>is  [mm:ss.xx]amazing[mm:ss.xx]APlayer.

- mini (boolean; default False)

- mutex (boolean; default True)

- notice (dict; default {    isShow: False,    time: 2000,    opacity: 0.8})

    `notice` is a dict with keys:

    - isShow (boolean; optional)

    - opacity (number; optional)

    - text (string; optional)

    - time (number; optional)

- order (a value equal to: 'list', 'random'; default 'list')

- pause (boolean; default False)

- pauseClicks (number; default 0)

- play (boolean; default False)

- playClicks (number; default 0)

- preload (a value equal to: 'none', 'metadata', 'auto'; default 'auto')

- removeList (dict; default {    isRemove: False})

    `removeList` is a dict with keys:

    - index (number; optional)

    - isRemove (boolean; optional)

- seek (dict; default {    isSeek: False})

    `seek` is a dict with keys:

    - isSeek (boolean; optional)

    - time (number; optional)

- seekClicks (number; default 0)

- showList (boolean; default False)

- showLrc (boolean; default False)

- showLrcClicks (number; default 0)

- showNoticeClicks (number; default 0)

- skipBack (boolean; default False)

- skipBackClicks (number; default 0)

- skipForward (boolean; default False)

- skipForwardClicks (number; default 0)

- storageName (string; default 'aplayer-setting')

- style (dict; optional)

- switchList (dict; default {    isSwitch: False})

    `switchList` is a dict with keys:

    - index (number; optional)

    - isSwitch (boolean; optional)

- theme (string; default '#b7daff')

- volume (number; default 0.7)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyAPlayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, fixed=Component.UNDEFINED, mini=Component.UNDEFINED, autoplay=Component.UNDEFINED, theme=Component.UNDEFINED, loop=Component.UNDEFINED, order=Component.UNDEFINED, preload=Component.UNDEFINED, volume=Component.UNDEFINED, audio=Component.UNDEFINED, mutex=Component.UNDEFINED, lrcType=Component.UNDEFINED, listFolded=Component.UNDEFINED, listMaxHeight=Component.UNDEFINED, storageName=Component.UNDEFINED, play=Component.UNDEFINED, pause=Component.UNDEFINED, seek=Component.UNDEFINED, skipBack=Component.UNDEFINED, skipForward=Component.UNDEFINED, showLrc=Component.UNDEFINED, hideLrc=Component.UNDEFINED, notice=Component.UNDEFINED, showList=Component.UNDEFINED, hideList=Component.UNDEFINED, addList=Component.UNDEFINED, removeList=Component.UNDEFINED, switchList=Component.UNDEFINED, clearList=Component.UNDEFINED, destroy=Component.UNDEFINED, playClicks=Component.UNDEFINED, pauseClicks=Component.UNDEFINED, seekClicks=Component.UNDEFINED, skipBackClicks=Component.UNDEFINED, skipForwardClicks=Component.UNDEFINED, showLrcClicks=Component.UNDEFINED, hideLrcClicks=Component.UNDEFINED, showNoticeClicks=Component.UNDEFINED, hideNoticeClicks=Component.UNDEFINED, listShowClicks=Component.UNDEFINED, listHideClicks=Component.UNDEFINED, listAddClicks=Component.UNDEFINED, listRemoveClicks=Component.UNDEFINED, listSwitchClicks=Component.UNDEFINED, listClearClicks=Component.UNDEFINED, destroyClicks=Component.UNDEFINED, currentPlayAudioInfo=Component.UNDEFINED, currentPauseAudioInfo=Component.UNDEFINED, currentSeekAudioInfo=Component.UNDEFINED, currentNoticeInfo=Component.UNDEFINED, currentListAddAudioInfo=Component.UNDEFINED, currentListRemoveAudioInfo=Component.UNDEFINED, currentListSwitchAudioInfo=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'addList', 'audio', 'autoplay', 'className', 'clearList', 'currentListAddAudioInfo', 'currentListRemoveAudioInfo', 'currentListSwitchAudioInfo', 'currentNoticeInfo', 'currentPauseAudioInfo', 'currentPlayAudioInfo', 'currentSeekAudioInfo', 'destroy', 'destroyClicks', 'fixed', 'hideList', 'hideLrc', 'hideLrcClicks', 'hideNoticeClicks', 'listAddClicks', 'listClearClicks', 'listFolded', 'listHideClicks', 'listMaxHeight', 'listRemoveClicks', 'listShowClicks', 'listSwitchClicks', 'loading_state', 'loop', 'lrcType', 'mini', 'mutex', 'notice', 'order', 'pause', 'pauseClicks', 'play', 'playClicks', 'preload', 'removeList', 'seek', 'seekClicks', 'showList', 'showLrc', 'showLrcClicks', 'showNoticeClicks', 'skipBack', 'skipBackClicks', 'skipForward', 'skipForwardClicks', 'storageName', 'style', 'switchList', 'theme', 'volume']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'addList', 'audio', 'autoplay', 'className', 'clearList', 'currentListAddAudioInfo', 'currentListRemoveAudioInfo', 'currentListSwitchAudioInfo', 'currentNoticeInfo', 'currentPauseAudioInfo', 'currentPlayAudioInfo', 'currentSeekAudioInfo', 'destroy', 'destroyClicks', 'fixed', 'hideList', 'hideLrc', 'hideLrcClicks', 'hideNoticeClicks', 'listAddClicks', 'listClearClicks', 'listFolded', 'listHideClicks', 'listMaxHeight', 'listRemoveClicks', 'listShowClicks', 'listSwitchClicks', 'loading_state', 'loop', 'lrcType', 'mini', 'mutex', 'notice', 'order', 'pause', 'pauseClicks', 'play', 'playClicks', 'preload', 'removeList', 'seek', 'seekClicks', 'showList', 'showLrc', 'showLrcClicks', 'showNoticeClicks', 'skipBack', 'skipBackClicks', 'skipForward', 'skipForwardClicks', 'storageName', 'style', 'switchList', 'theme', 'volume']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyAPlayer, self).__init__(**args)
