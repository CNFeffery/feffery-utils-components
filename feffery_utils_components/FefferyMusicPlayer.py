# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyMusicPlayer(Component):
    """A FefferyMusicPlayer component.


Keyword arguments:

- id (string; optional)

- audioLists (list of dicts; optional)

    `audioLists` is a list of dicts with keys:

    - cover (string; optional)

    - duration (number; optional)

    - extraParams (dict; optional)

    - lyric (string; optional)

    - musicSrc (string; optional)

    - name (string; optional)

    - singer (string | a list of or a singular dash component, string or number; optional)

- autoHiddenCover (boolean; default False)

- autoPlayInitLoadPlayList (boolean; default False)

- autoplay (boolean; default True)

- bounds (dict; default 'body')

    `bounds` is a a value equal to: 'body', 'parent' | dict with keys:

    - bottom (number; optional)

    - left (number; optional)

    - right (number; optional)

    - top (number; optional)

- className (string; optional)

- clearPriorAudioLists (boolean; default False)

- customizeContainerId (string; optional)

- customizeLightThemeHoverColor (string; default '#3ece89')

- customizeThemeColor (string; default '#31c27c')

- defaultPlayIndex (number; default 0)

- defaultPlayMode (a value equal to: 'order', 'orderLoop', 'singleLoop', 'shufflePlay'; default 'order')

- defaultPosition (dict; default {    top: 0,    left: 0})

    `defaultPosition` is a dict with keys:

    - bottom (number; optional)

    - left (number; optional)

    - right (number; optional)

    - top (number; optional)

- defaultVolume (number; default 1)

- drag (boolean; default True)

- extendsContent (a list of or a singular dash component, string or number | boolean | string; optional)

- glassBg (boolean; default False)

- icon (dict; optional)

    `icon` is a dict with keys:

    - close (a list of or a singular dash component, string or number | string; optional)

    - delete (a list of or a singular dash component, string or number | string; optional)

    - destroy (a list of or a singular dash component, string or number | string; optional)

    - download (a list of or a singular dash component, string or number | string; optional)

    - loading (a list of or a singular dash component, string or number | string; optional)

    - loop (a list of or a singular dash component, string or number | string; optional)

    - lyric (a list of or a singular dash component, string or number | string; optional)

    - mute (a list of or a singular dash component, string or number | string; optional)

    - next (a list of or a singular dash component, string or number | string; optional)

    - order (a list of or a singular dash component, string or number | string; optional)

    - orderLoop (a list of or a singular dash component, string or number | string; optional)

    - pause (a list of or a singular dash component, string or number | string; optional)

    - play (a list of or a singular dash component, string or number | string; optional)

    - playLists (a list of or a singular dash component, string or number | string; optional)

    - prev (a list of or a singular dash component, string or number | string; optional)

    - reload (a list of or a singular dash component, string or number | string; optional)

    - shuffle (a list of or a singular dash component, string or number | string; optional)

    - toggle (a list of or a singular dash component, string or number | string; optional)

    - volume (a list of or a singular dash component, string or number | string; optional)

- loadAudioErrorPlayNext (boolean; default True)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh_CN', 'en_US'; default 'zh_CN')

- lyricClassName (string; optional)

- mode (a value equal to: 'mini', 'full'; default 'mini')

- once (boolean; default False)

- playIndex (number; default 0)

- playModeShowTime (number; default 600)

- preload (boolean | a value equal to: 'auto'; default False)

- quietUpdate (boolean; default False)

- remember (boolean; default False)

- remove (boolean; default True)

- responsive (boolean; default True)

- restartCurrentOnPrev (boolean; default False)

- seeked (boolean; default True)

- showDestroy (boolean; default False)

- showDownload (boolean; default True)

- showLyric (boolean; default False)

- showMediaSession (boolean; default False)

- showMiniModeCover (boolean; default True)

- showMiniProcessBar (boolean; default False)

- showPlay (boolean; default True)

- showPlayMode (boolean; default True)

- showProgressLoadBar (boolean; default True)

- showReload (boolean; default True)

- showThemeSwitch (boolean; default True)

- spaceBar (boolean; default False)

- style (dict; optional)

- theme (a value equal to: 'light', 'dark', 'auto'; default 'dark')

- toggleMode (boolean; default True)"""
    _children_props = ['audioLists[].singer', 'icon.pause', 'icon.play', 'icon.destroy', 'icon.close', 'icon.delete', 'icon.download', 'icon.toggle', 'icon.lyric', 'icon.volume', 'icon.mute', 'icon.next', 'icon.prev', 'icon.playLists', 'icon.reload', 'icon.loop', 'icon.order', 'icon.orderLoop', 'icon.shuffle', 'icon.loading', 'extendsContent']
    _base_nodes = ['extendsContent', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMusicPlayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, audioLists=Component.UNDEFINED, theme=Component.UNDEFINED, customizeThemeColor=Component.UNDEFINED, customizeLightThemeHoverColor=Component.UNDEFINED, locale=Component.UNDEFINED, icon=Component.UNDEFINED, defaultPosition=Component.UNDEFINED, playModeShowTime=Component.UNDEFINED, bounds=Component.UNDEFINED, preload=Component.UNDEFINED, remember=Component.UNDEFINED, glassBg=Component.UNDEFINED, remove=Component.UNDEFINED, defaultPlayIndex=Component.UNDEFINED, playIndex=Component.UNDEFINED, defaultPlayMode=Component.UNDEFINED, mode=Component.UNDEFINED, once=Component.UNDEFINED, autoplay=Component.UNDEFINED, toggleMode=Component.UNDEFINED, drag=Component.UNDEFINED, seeked=Component.UNDEFINED, showMiniModeCover=Component.UNDEFINED, showMiniProcessBar=Component.UNDEFINED, showProgressLoadBar=Component.UNDEFINED, showPlay=Component.UNDEFINED, showReload=Component.UNDEFINED, showDownload=Component.UNDEFINED, showPlayMode=Component.UNDEFINED, showThemeSwitch=Component.UNDEFINED, showLyric=Component.UNDEFINED, showMediaSession=Component.UNDEFINED, lyricClassName=Component.UNDEFINED, extendsContent=Component.UNDEFINED, defaultVolume=Component.UNDEFINED, loadAudioErrorPlayNext=Component.UNDEFINED, responsive=Component.UNDEFINED, autoHiddenCover=Component.UNDEFINED, clearPriorAudioLists=Component.UNDEFINED, autoPlayInitLoadPlayList=Component.UNDEFINED, spaceBar=Component.UNDEFINED, showDestroy=Component.UNDEFINED, quietUpdate=Component.UNDEFINED, restartCurrentOnPrev=Component.UNDEFINED, customizeContainerId=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'audioLists', 'autoHiddenCover', 'autoPlayInitLoadPlayList', 'autoplay', 'bounds', 'className', 'clearPriorAudioLists', 'customizeContainerId', 'customizeLightThemeHoverColor', 'customizeThemeColor', 'defaultPlayIndex', 'defaultPlayMode', 'defaultPosition', 'defaultVolume', 'drag', 'extendsContent', 'glassBg', 'icon', 'loadAudioErrorPlayNext', 'loading_state', 'locale', 'lyricClassName', 'mode', 'once', 'playIndex', 'playModeShowTime', 'preload', 'quietUpdate', 'remember', 'remove', 'responsive', 'restartCurrentOnPrev', 'seeked', 'showDestroy', 'showDownload', 'showLyric', 'showMediaSession', 'showMiniModeCover', 'showMiniProcessBar', 'showPlay', 'showPlayMode', 'showProgressLoadBar', 'showReload', 'showThemeSwitch', 'spaceBar', 'style', 'theme', 'toggleMode']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'audioLists', 'autoHiddenCover', 'autoPlayInitLoadPlayList', 'autoplay', 'bounds', 'className', 'clearPriorAudioLists', 'customizeContainerId', 'customizeLightThemeHoverColor', 'customizeThemeColor', 'defaultPlayIndex', 'defaultPlayMode', 'defaultPosition', 'defaultVolume', 'drag', 'extendsContent', 'glassBg', 'icon', 'loadAudioErrorPlayNext', 'loading_state', 'locale', 'lyricClassName', 'mode', 'once', 'playIndex', 'playModeShowTime', 'preload', 'quietUpdate', 'remember', 'remove', 'responsive', 'restartCurrentOnPrev', 'seeked', 'showDestroy', 'showDownload', 'showLyric', 'showMediaSession', 'showMiniModeCover', 'showMiniProcessBar', 'showPlay', 'showPlayMode', 'showProgressLoadBar', 'showReload', 'showThemeSwitch', 'spaceBar', 'style', 'theme', 'toggleMode']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyMusicPlayer, self).__init__(**args)
