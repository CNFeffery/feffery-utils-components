# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyMusicPlayer(Component):
    """A FefferyMusicPlayer component.


Keyword arguments:

- id (string; optional):
    音乐播放器id.

- audioLists (list of dicts; optional):
    设置音乐播放器文件列表信息.

    `audioLists` is a list of dicts with keys:

    - cover (string; optional):
        音乐封面.

    - duration (number; optional):
        歌曲时长.

    - extraParams (dict; optional):
        额外的参数.

    - lyric (string; optional):
        歌词.

    - musicSrc (string; optional):
        音乐链接.

    - name (string; optional):
        音乐名称.

    - singer (string | a list of or a singular dash component, string or number; optional):
        歌手.

- autoHiddenCover (boolean; default False):
    如果没有可用的封面照片，是否自动隐藏封面照片，默认为False.

- autoPlayInitLoadPlayList (boolean; default False):
    加载新播放列表后是否立即播放您的新播放列表，默认为False.

- autoplay (boolean; default True):
    加载完成后是否播放音频。移动设备的自动播放策略更改无效，默认为True.

- bounds (dict; default 'body'):
    拖拽边界.

    `bounds` is a a value equal to: 'body', 'parent' | dict with keys:

    - bottom (number; optional)

    - left (number; optional)

    - right (number; optional)

    - top (number; optional)

- className (string; optional):
    设置音乐播放器的css类名.

- clearPriorAudioLists (boolean; default False):
    是否将新播放列表替换为第一个加载的播放列表，并将 playIndex 重置为 0，默认为False.

- customizeContainerId (string; optional):
    自定义挂载容器类名.

- customizeLightThemeHoverColor (string; default '#3ece89'):
    主题为'light'时，设置相关按钮悬浮的颜色，默认为'#3ece89'.

- customizeThemeColor (string; default '#31c27c'):
    自定义主题颜色，默认为'#31c27c'.

- defaultPlayIndex (number; default 0):
    播放器的默认播放索引，默认为0.

- defaultPlayMode (a value equal to: 'order', 'orderLoop', 'singleLoop', 'shufflePlay'; default 'order'):
    音乐播放器选项的默认播放模式，可选的有'order'、'orderLoop'、'singleLoop'、'shufflePlay'，默认为order\.

- defaultPosition (dict; default {    top: 0,    left: 0}):
    设置音乐播放器mini模式的初始位置，默认为{top:0, left:0}.

    `defaultPosition` is a dict with keys:

    - bottom (number; optional):
        设置音乐播放器距离底部的距离，默认为0.

    - left (number; optional):
        设置音乐播放器距离左侧的距离，默认为0.

    - right (number; optional):
        设置音乐播放器距离右侧的距离，默认为0.

    - top (number; optional):
        设置音乐播放器距离顶部的距离，默认为0.

- defaultVolume (number; default 1):
    音频播放器的默认音量，范围0-1，默认为1.

- drag (boolean; default True):
    播放器是否是可以拖拽的'mini'模式，默认为True.

- extendsContent (a list of or a singular dash component, string or number | boolean | string; optional):
    可扩展的自定义内容.

- glassBg (boolean; default False):
    设置背景是否显示磨砂玻璃效果，默认为False.

- icon (dict; optional):
    设置音乐播放器相关图标.

    `icon` is a dict with keys:

    - close (a list of or a singular dash component, string or number | string; optional):
        设置close图标.

    - delete (a list of or a singular dash component, string or number | string; optional):
        设置delete图标.

    - destroy (a list of or a singular dash component, string or number | string; optional):
        设置destroy图标.

    - download (a list of or a singular dash component, string or number | string; optional):
        设置download图标.

    - loading (a list of or a singular dash component, string or number | string; optional):
        设置loading图标.

    - loop (a list of or a singular dash component, string or number | string; optional):
        设置loop图标.

    - lyric (a list of or a singular dash component, string or number | string; optional):
        设置lyric图标.

    - mute (a list of or a singular dash component, string or number | string; optional):
        设置mute图标.

    - next (a list of or a singular dash component, string or number | string; optional):
        设置next图标.

    - order (a list of or a singular dash component, string or number | string; optional):
        设置order图标.

    - orderLoop (a list of or a singular dash component, string or number | string; optional):
        设置orderLoop图标.

    - pause (a list of or a singular dash component, string or number | string; optional):
        设置pause图标.

    - play (a list of or a singular dash component, string or number | string; optional):
        设置play图标.

    - playLists (a list of or a singular dash component, string or number | string; optional):
        设置playLists图标.

    - prev (a list of or a singular dash component, string or number | string; optional):
        设置prev图标.

    - reload (a list of or a singular dash component, string or number | string; optional):
        设置reload图标.

    - shuffle (a list of or a singular dash component, string or number | string; optional):
        设置shuffle图标.

    - toggle (a list of or a singular dash component, string or number | string; optional):
        设置toggle图标.

    - volume (a list of or a singular dash component, string or number | string; optional):
        设置volume图标.

- key (string; optional):
    设置播放器的key，强制刷新组件.

- loadAudioErrorPlayNext (boolean; default True):
    当前音频播放失败时是否尝试播放下一个音频，默认为True.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh_CN', 'en_US'; default 'zh_CN'):
    设置音乐播放器语言，可选的有'zh_CN'、'en_US'，默认为'zh_CN'.

- lyricClassName (string; optional):
    音频歌词类名.

- mode (a value equal to: 'mini', 'full'; default 'mini'):
    设置播放器主题模式，可选的有'mini'、'full'，默认为mini.

- once (boolean; default False):
    默认的audioPlay句柄功能会在每次暂停后再次播放，如果只想触发一次，可以设置'True'，默认为False.

- playIndex (number; default 0):
    播放器的播放索引，默认为0.

- playModeShowTime (number; default 600):
    设置播放模式切换时提示语的显示时间（毫秒），默认为600.

- preload (boolean | a value equal to: 'auto'; default False):
    设置是否在页面加载后立即加载音频，默认为False.

- quietUpdate (boolean; default False):
    https://github.com/lijinke666/react-music-player#bulb-quiet-update.

- remember (boolean; default False):
    下次访问播放器时，是否保留最后状态，默认为False.

- remove (boolean; default True):
    设置音频是否可以被删除，默认为True.

- responsive (boolean; default True):
    是否开启响应模式，如果设置为False，音频控制器始终显示桌面ui，默认为True.

- restartCurrentOnPrev (boolean; default False):
    尝试播放上一首歌曲时，如果歌曲的当前时间超过 1 秒，是否重新启动当前曲目，默认为False.

- seeked (boolean; default True):
    是否可以拖动或单击进度条以播放新进度，默认为True.

- showDestroy (boolean; default False):
    是否显示销毁按钮，默认为False.

- showDownload (boolean; default True):
    是否显示播放器面板的下载按钮，默认为True.

- showLyric (boolean; default False):
    是否显示播放器面板的音频歌词按钮，默认为False.

- showMediaSession (boolean; default False):
    https://web.dev/media-session/，默认为False.

- showMiniModeCover (boolean; default True):
    音频封面是否示'mini'模式，默认为True.

- showMiniProcessBar (boolean; default False):
    音频进度圆条是否显示'mini'模式，默认为False.

- showPlay (boolean; default True):
    是否显示播放器面板的播放按钮，默认为True.

- showPlayMode (boolean; default True):
    是否显示播放器面板的播放模式切换按钮，默认为True.

- showProgressLoadBar (boolean; default True):
    是否显示音频加载进度条，默认为True.

- showReload (boolean; default True):
    是否显示播放器面板的重新加载按钮，默认为True.

- showThemeSwitch (boolean; default True):
    是否显示播放器面板的主题切换开关，默认为True.

- spaceBar (boolean; default False):
    是否可以通过空格键播放和暂停音频（桌面有效），默认为False.

- style (dict; optional):
    设置音乐播放器的样式.

- theme (a value equal to: 'light', 'dark', 'auto'; default 'dark'):
    设置音乐播放器主题的颜色，可选的有'light'、'dark'、'auto'，默认为'dark'.

- toggleMode (boolean; default True):
    是否可以在两种模式之间切换，full => mini 或 mini => full，默认为True."""
    _children_props = ['audioLists[].singer', 'icon.pause', 'icon.play', 'icon.destroy', 'icon.close', 'icon.delete', 'icon.download', 'icon.toggle', 'icon.lyric', 'icon.volume', 'icon.mute', 'icon.next', 'icon.prev', 'icon.playLists', 'icon.reload', 'icon.loop', 'icon.order', 'icon.orderLoop', 'icon.shuffle', 'icon.loading', 'extendsContent']
    _base_nodes = ['extendsContent', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMusicPlayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, audioLists=Component.UNDEFINED, theme=Component.UNDEFINED, customizeThemeColor=Component.UNDEFINED, customizeLightThemeHoverColor=Component.UNDEFINED, locale=Component.UNDEFINED, icon=Component.UNDEFINED, defaultPosition=Component.UNDEFINED, playModeShowTime=Component.UNDEFINED, bounds=Component.UNDEFINED, preload=Component.UNDEFINED, remember=Component.UNDEFINED, glassBg=Component.UNDEFINED, remove=Component.UNDEFINED, defaultPlayIndex=Component.UNDEFINED, playIndex=Component.UNDEFINED, defaultPlayMode=Component.UNDEFINED, mode=Component.UNDEFINED, once=Component.UNDEFINED, autoplay=Component.UNDEFINED, toggleMode=Component.UNDEFINED, drag=Component.UNDEFINED, seeked=Component.UNDEFINED, showMiniModeCover=Component.UNDEFINED, showMiniProcessBar=Component.UNDEFINED, showProgressLoadBar=Component.UNDEFINED, showPlay=Component.UNDEFINED, showReload=Component.UNDEFINED, showDownload=Component.UNDEFINED, showPlayMode=Component.UNDEFINED, showThemeSwitch=Component.UNDEFINED, showLyric=Component.UNDEFINED, showMediaSession=Component.UNDEFINED, lyricClassName=Component.UNDEFINED, extendsContent=Component.UNDEFINED, defaultVolume=Component.UNDEFINED, loadAudioErrorPlayNext=Component.UNDEFINED, responsive=Component.UNDEFINED, autoHiddenCover=Component.UNDEFINED, clearPriorAudioLists=Component.UNDEFINED, autoPlayInitLoadPlayList=Component.UNDEFINED, spaceBar=Component.UNDEFINED, showDestroy=Component.UNDEFINED, quietUpdate=Component.UNDEFINED, restartCurrentOnPrev=Component.UNDEFINED, customizeContainerId=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'audioLists', 'autoHiddenCover', 'autoPlayInitLoadPlayList', 'autoplay', 'bounds', 'className', 'clearPriorAudioLists', 'customizeContainerId', 'customizeLightThemeHoverColor', 'customizeThemeColor', 'defaultPlayIndex', 'defaultPlayMode', 'defaultPosition', 'defaultVolume', 'drag', 'extendsContent', 'glassBg', 'icon', 'key', 'loadAudioErrorPlayNext', 'loading_state', 'locale', 'lyricClassName', 'mode', 'once', 'playIndex', 'playModeShowTime', 'preload', 'quietUpdate', 'remember', 'remove', 'responsive', 'restartCurrentOnPrev', 'seeked', 'showDestroy', 'showDownload', 'showLyric', 'showMediaSession', 'showMiniModeCover', 'showMiniProcessBar', 'showPlay', 'showPlayMode', 'showProgressLoadBar', 'showReload', 'showThemeSwitch', 'spaceBar', 'style', 'theme', 'toggleMode']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'audioLists', 'autoHiddenCover', 'autoPlayInitLoadPlayList', 'autoplay', 'bounds', 'className', 'clearPriorAudioLists', 'customizeContainerId', 'customizeLightThemeHoverColor', 'customizeThemeColor', 'defaultPlayIndex', 'defaultPlayMode', 'defaultPosition', 'defaultVolume', 'drag', 'extendsContent', 'glassBg', 'icon', 'key', 'loadAudioErrorPlayNext', 'loading_state', 'locale', 'lyricClassName', 'mode', 'once', 'playIndex', 'playModeShowTime', 'preload', 'quietUpdate', 'remember', 'remove', 'responsive', 'restartCurrentOnPrev', 'seeked', 'showDestroy', 'showDownload', 'showLyric', 'showMediaSession', 'showMiniModeCover', 'showMiniProcessBar', 'showPlay', 'showPlayMode', 'showProgressLoadBar', 'showReload', 'showThemeSwitch', 'spaceBar', 'style', 'theme', 'toggleMode']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyMusicPlayer, self).__init__(**args)
