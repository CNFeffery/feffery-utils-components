# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class FefferyMusicPlayer(Component):
    """A FefferyMusicPlayer component.
音乐播放组件FefferyMusicPlayer

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- audioLists (list of dicts; optional):
    设置音乐播放器文件列表信息.

    `audioLists` is a list of dicts with keys:

    - name (string; optional):
        音乐名称.

    - musicSrc (string; optional):
        音乐链接.

    - cover (string; optional):
        音乐封面.

    - singer (string | a list of or a singular dash component, string or number; optional):
        歌手.

    - duration (number; optional):
        歌曲时长.

    - lyric (string; optional):
        歌词.

    - extraParams (dict; optional):
        额外的参数.

- theme (a value equal to: 'light', 'dark', 'auto'; default 'dark'):
    设置音乐播放器主题的颜色，可选的有`'light'`、`'dark'`、`'auto'`  默认值：`'dark'`.

- customizeThemeColor (string; default '#31c27c'):
    自定义主题颜色  默认值：`'#31c27c'`.

- customizeLightThemeHoverColor (string; default '#3ece89'):
    主题为`'light'`时，设置相关按钮悬浮的颜色  默认值：`'#3ece89'`.

- locale (a value equal to: 'zh_CN', 'en_US'; default 'zh_CN'):
    设置音乐播放器语言，可选的有`'zh_CN'`、`'en_US'`  默认值：`'zh_CN'`.

- icon (dict; optional):
    设置音乐播放器相关图标.

    `icon` is a dict with keys:

    - pause (a list of or a singular dash component, string or number | string; optional):
        设置`pause`图标.

    - play (a list of or a singular dash component, string or number | string; optional):
        设置`play`图标.

    - destroy (a list of or a singular dash component, string or number | string; optional):
        设置`destroy`图标.

    - close (a list of or a singular dash component, string or number | string; optional):
        设置`close`图标.

    - delete (a list of or a singular dash component, string or number | string; optional):
        设置`delete`图标.

    - download (a list of or a singular dash component, string or number | string; optional):
        设置`download`图标.

    - toggle (a list of or a singular dash component, string or number | string; optional):
        设置`toggle`图标.

    - lyric (a list of or a singular dash component, string or number | string; optional):
        设置`lyric`图标.

    - volume (a list of or a singular dash component, string or number | string; optional):
        设置`volume`图标.

    - mute (a list of or a singular dash component, string or number | string; optional):
        设置`mute`图标.

    - next (a list of or a singular dash component, string or number | string; optional):
        设置`next`图标.

    - prev (a list of or a singular dash component, string or number | string; optional):
        设置`prev`图标.

    - playLists (a list of or a singular dash component, string or number | string; optional):
        设置`playLists`图标.

    - reload (a list of or a singular dash component, string or number | string; optional):
        设置`reload`图标.

    - loop (a list of or a singular dash component, string or number | string; optional):
        设置`loop`图标.

    - order (a list of or a singular dash component, string or number | string; optional):
        设置`order`图标.

    - orderLoop (a list of or a singular dash component, string or number | string; optional):
        设置`orderLoop`图标.

    - shuffle (a list of or a singular dash component, string or number | string; optional):
        设置`shuffle`图标.

    - loading (a list of or a singular dash component, string or number | string; optional):
        设置`loading`图标.

- defaultPosition (dict; default { top: 0, left: 0 }):
    设置音乐播放器`mini`模式的初始位置  默认值：`{'top': 0, 'left': 0}`.

    `defaultPosition` is a dict with keys:

    - top (number; optional):
        设置音乐播放器距离顶部的距离  默认值：`0`.

    - left (number; optional):
        设置音乐播放器距离左侧的距离  默认值：`0`.

    - right (number; optional):
        设置音乐播放器距离右侧的距离  默认值：`0`.

    - bottom (number; optional):
        设置音乐播放器距离底部的距离  默认值：`0`.

- playModeShowTime (number; default 600):
    设置播放模式切换时提示语的显示时间（毫秒）  默认值：`600`.

- bounds (dict; default 'body'):
    拖拽边界.

    `bounds` is a a value equal to: 'body', 'parent' | dict with keys:

    - top (number; optional)

    - left (number; optional)

    - right (number; optional)

    - bottom (number; optional)

- preload (boolean | a value equal to: 'auto'; default False):
    设置是否在页面加载后立即加载音频  默认值：`False`.

- remember (boolean; default False):
    下次访问播放器时，是否保留最后状态  默认值：`False`.

- glassBg (boolean; default False):
    设置背景是否显示磨砂玻璃效果  默认值：`False`.

- remove (boolean; default True):
    设置音频是否可以被删除  默认值：`True`.

- defaultPlayIndex (number; default 0):
    播放器的默认播放索引  默认值：`0`.

- playIndex (number; default 0):
    播放器的播放索引  默认值：`0`.

- defaultPlayMode (a value equal to: 'order', 'orderLoop', 'singleLoop', 'shufflePlay'; default 'order'):
    音乐播放器选项的默认播放模式，可选的有`'order'`、`'orderLoop'`、`'singleLoop'`、`'shufflePlay'`
    默认值：`'order'`.

- mode (a value equal to: 'mini', 'full'; default 'mini'):
    设置播放器主题模式，可选的有`'mini'`、`'full'`  默认值：`'mini'`.

- once (boolean; default False):
    默认的`audioPlay`句柄功能会在每次暂停后再次播放，如果只想触发一次，可以设置`True`  默认值：`False`.

- autoplay (boolean; default True):
    加载完成后是否播放音频。移动设备的自动播放策略更改无效  默认值：`True`.

- toggleMode (boolean; default True):
    是否可以在两种模式之间切换，`full => mini`或`mini => full`  默认值：`True`.

- drag (boolean; default True):
    播放器是否是可以拖拽的`'mini'`模式  默认值：`True`.

- seeked (boolean; default True):
    是否可以拖动或单击进度条以播放新进度  默认值：`True`.

- showMiniModeCover (boolean; default True):
    音频封面是否示`'mini'`模式  默认值：`True`.

- showMiniProcessBar (boolean; default False):
    音频进度圆条是否显示`'mini'`模式  默认值：`False`.

- showProgressLoadBar (boolean; default True):
    是否显示音频加载进度条  默认值：`True`.

- showPlay (boolean; default True):
    是否显示播放器面板的播放按钮  默认值：`True`.

- showReload (boolean; default True):
    是否显示播放器面板的重新加载按钮  默认值：`True`.

- showDownload (boolean; default True):
    是否显示播放器面板的下载按钮  默认值：`True`.

- showPlayMode (boolean; default True):
    是否显示播放器面板的播放模式切换按钮  默认值：`True`.

- showThemeSwitch (boolean; default True):
    是否显示播放器面板的主题切换开关  默认值：`True`.

- showLyric (boolean; default False):
    是否显示播放器面板的音频歌词按钮  默认值：`False`.

- showMediaSession (boolean; default False):
    [media-session](https://web.dev/media-session/)  默认值：`False`.

- lyricClassName (string; optional):
    音频歌词类名.

- extendsContent (a list of or a singular dash component, string or number | boolean | string; optional):
    可扩展的自定义内容.

- defaultVolume (number; default 1):
    音频播放器的默认音量，范围`0-1`  默认值：`1`.

- loadAudioErrorPlayNext (boolean; default True):
    当前音频播放失败时是否尝试播放下一个音频  默认值：`True`.

- responsive (boolean; default True):
    是否开启响应模式，如果设置为`False`，音频控制器始终显示桌面`ui`  默认值：`True`.

- autoHiddenCover (boolean; default False):
    如果没有可用的封面照片，是否自动隐藏封面照片  默认值：`False`.

- clearPriorAudioLists (boolean; default False):
    是否将新播放列表替换为第一个加载的播放列表，并将`playIndex`重置为`0`  默认值：`False`.

- autoPlayInitLoadPlayList (boolean; default False):
    加载新播放列表后是否立即播放您的新播放列表  默认值：`False`.

- spaceBar (boolean; default False):
    是否可以通过空格键播放和暂停音频（桌面有效）  默认值：`False`.

- showDestroy (boolean; default False):
    是否显示销毁按钮  默认值：`False`.

- quietUpdate (boolean; default False):
    [bulb-quiet-update](https://github.com/lijinke666/react-music-player#bulb-quiet-update).

- restartCurrentOnPrev (boolean; default False):
    尝试播放上一首歌曲时，如果歌曲的当前时间超过`1`秒，是否重新启动当前曲目  默认值：`False`.

- customizeContainerId (string; optional):
    自定义挂载容器类名."""
    _children_props = ['audioLists[].singer', 'icon.pause', 'icon.play', 'icon.destroy', 'icon.close', 'icon.delete', 'icon.download', 'icon.toggle', 'icon.lyric', 'icon.volume', 'icon.mute', 'icon.next', 'icon.prev', 'icon.playLists', 'icon.reload', 'icon.loop', 'icon.order', 'icon.orderLoop', 'icon.shuffle', 'icon.loading', 'extendsContent']
    _base_nodes = ['extendsContent', 'children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyMusicPlayer'
    AudioLists = TypedDict(
        "AudioLists",
            {
            "name": NotRequired[str],
            "musicSrc": NotRequired[str],
            "cover": NotRequired[str],
            "singer": NotRequired[typing.Union[str, typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]]]],
            "duration": NotRequired[typing.Union[int, float, numbers.Number]],
            "lyric": NotRequired[str],
            "extraParams": NotRequired[dict]
        }
    )

    Icon = TypedDict(
        "Icon",
            {
            "pause": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "play": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "destroy": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "close": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "delete": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "download": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "toggle": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "lyric": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "volume": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "mute": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "next": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "prev": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "playLists": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "reload": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "loop": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "order": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "orderLoop": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "shuffle": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]],
            "loading": NotRequired[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], str]]
        }
    )

    DefaultPosition = TypedDict(
        "DefaultPosition",
            {
            "top": NotRequired[typing.Union[int, float, numbers.Number]],
            "left": NotRequired[typing.Union[int, float, numbers.Number]],
            "right": NotRequired[typing.Union[int, float, numbers.Number]],
            "bottom": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    Bounds = TypedDict(
        "Bounds",
            {
            "top": NotRequired[typing.Union[int, float, numbers.Number]],
            "left": NotRequired[typing.Union[int, float, numbers.Number]],
            "right": NotRequired[typing.Union[int, float, numbers.Number]],
            "bottom": NotRequired[typing.Union[int, float, numbers.Number]]
        }
    )

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        audioLists: typing.Optional[typing.Sequence["AudioLists"]] = None,
        theme: typing.Optional[Literal["light", "dark", "auto"]] = None,
        customizeThemeColor: typing.Optional[str] = None,
        customizeLightThemeHoverColor: typing.Optional[str] = None,
        locale: typing.Optional[Literal["zh_CN", "en_US"]] = None,
        icon: typing.Optional["Icon"] = None,
        defaultPosition: typing.Optional["DefaultPosition"] = None,
        playModeShowTime: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        bounds: typing.Optional[typing.Union[Literal["body", "parent"], "Bounds"]] = None,
        preload: typing.Optional[typing.Union[bool, Literal["auto"]]] = None,
        remember: typing.Optional[bool] = None,
        glassBg: typing.Optional[bool] = None,
        remove: typing.Optional[bool] = None,
        defaultPlayIndex: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        playIndex: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        defaultPlayMode: typing.Optional[Literal["order", "orderLoop", "singleLoop", "shufflePlay"]] = None,
        mode: typing.Optional[Literal["mini", "full"]] = None,
        once: typing.Optional[bool] = None,
        autoplay: typing.Optional[bool] = None,
        toggleMode: typing.Optional[bool] = None,
        drag: typing.Optional[bool] = None,
        seeked: typing.Optional[bool] = None,
        showMiniModeCover: typing.Optional[bool] = None,
        showMiniProcessBar: typing.Optional[bool] = None,
        showProgressLoadBar: typing.Optional[bool] = None,
        showPlay: typing.Optional[bool] = None,
        showReload: typing.Optional[bool] = None,
        showDownload: typing.Optional[bool] = None,
        showPlayMode: typing.Optional[bool] = None,
        showThemeSwitch: typing.Optional[bool] = None,
        showLyric: typing.Optional[bool] = None,
        showMediaSession: typing.Optional[bool] = None,
        lyricClassName: typing.Optional[str] = None,
        extendsContent: typing.Optional[typing.Union[typing.Union[str, int, float, ComponentType, typing.Sequence[typing.Union[str, int, float, ComponentType]]], bool, str]] = None,
        defaultVolume: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        loadAudioErrorPlayNext: typing.Optional[bool] = None,
        responsive: typing.Optional[bool] = None,
        autoHiddenCover: typing.Optional[bool] = None,
        clearPriorAudioLists: typing.Optional[bool] = None,
        autoPlayInitLoadPlayList: typing.Optional[bool] = None,
        spaceBar: typing.Optional[bool] = None,
        showDestroy: typing.Optional[bool] = None,
        quietUpdate: typing.Optional[bool] = None,
        restartCurrentOnPrev: typing.Optional[bool] = None,
        customizeContainerId: typing.Optional[str] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'audioLists', 'theme', 'customizeThemeColor', 'customizeLightThemeHoverColor', 'locale', 'icon', 'defaultPosition', 'playModeShowTime', 'bounds', 'preload', 'remember', 'glassBg', 'remove', 'defaultPlayIndex', 'playIndex', 'defaultPlayMode', 'mode', 'once', 'autoplay', 'toggleMode', 'drag', 'seeked', 'showMiniModeCover', 'showMiniProcessBar', 'showProgressLoadBar', 'showPlay', 'showReload', 'showDownload', 'showPlayMode', 'showThemeSwitch', 'showLyric', 'showMediaSession', 'lyricClassName', 'extendsContent', 'defaultVolume', 'loadAudioErrorPlayNext', 'responsive', 'autoHiddenCover', 'clearPriorAudioLists', 'autoPlayInitLoadPlayList', 'spaceBar', 'showDestroy', 'quietUpdate', 'restartCurrentOnPrev', 'customizeContainerId']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'audioLists', 'theme', 'customizeThemeColor', 'customizeLightThemeHoverColor', 'locale', 'icon', 'defaultPosition', 'playModeShowTime', 'bounds', 'preload', 'remember', 'glassBg', 'remove', 'defaultPlayIndex', 'playIndex', 'defaultPlayMode', 'mode', 'once', 'autoplay', 'toggleMode', 'drag', 'seeked', 'showMiniModeCover', 'showMiniProcessBar', 'showProgressLoadBar', 'showPlay', 'showReload', 'showDownload', 'showPlayMode', 'showThemeSwitch', 'showLyric', 'showMediaSession', 'lyricClassName', 'extendsContent', 'defaultVolume', 'loadAudioErrorPlayNext', 'responsive', 'autoHiddenCover', 'clearPriorAudioLists', 'autoPlayInitLoadPlayList', 'spaceBar', 'showDestroy', 'quietUpdate', 'restartCurrentOnPrev', 'customizeContainerId']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyMusicPlayer, self).__init__(**args)
