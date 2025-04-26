# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class FefferyAPlayer(Component):
    """A FefferyAPlayer component.
音频播放组件FefferyAPlayer

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- fixed (boolean; default False):
    是否开启吸底模式  默认值：`False`.

- mini (boolean; default False):
    是否开启迷你模式  默认值：`False`.

- autoplay (boolean; default False):
    音频是否自动播放  默认值：`False`.

- theme (string; default '#b7daff'):
    设置主题色  默认值：`'#b7daff'`.

- loop (a value equal to: 'all', 'one', 'none'; default 'all'):
    设置音频循环播放, 可选值: `'all'`、`'one'`、`'none'`  默认值：`'all'`.

- order (a value equal to: 'list', 'random'; default 'list'):
    设置音频循环顺序, 可选值: `'list'`、`'random'`  默认值：`'list'`.

- preload (a value equal to: 'none', 'metadata', 'auto'; default 'auto'):
    设置音频预加载，可选值: `'none'`、`'metadata'`、`'auto'`  默认值：`'auto'`.

- volume (number; default 0.7):
    默认音量，请注意播放器会记忆用户设置，用户手动设置音量后默认音量即失效.

- audio (list of dicts; default [{ type: 'auto' }]):
    设置音频信息.

    `audio` is a list of dicts with keys:

    - name (string; optional):
        设置音频名称.

    - artist (string; optional):
        设置音频作者.

    - url (string; optional):
        设置音频链接.

    - cover (string; optional):
        设置音频封面.

    - lrc (string; optional):
        设置音频`lrc`歌词.

    - theme (string; optional):
        设置切换到此音频时的主题色，比上面的`theme`优先级高.

    - type (a value equal to: 'auto', 'hls', 'normal'; optional):
        设置音频类型，可选的有`'auto'`、`'hls'`、`'normal'`  默认值：`'auto'`.

- mutex (boolean; default True):
    是否互斥，阻止多个播放器同时播放，当前播放器播放时暂停其他播放器  默认值：`True`.

- lrcType (a value equal to: 0, 1, 2, 3; default 0):
    有三种方式来给`APlayer`传递歌词，使用`lrcType`参数指明使用哪种方式，然后把歌词放到`audio.lrc`参数或者`HTML`里
    `1`表示把歌词放到`JS`字符串里面，`2`表示把歌词放到`HTML`里面，`3`表示把歌词放到`LRC`文件里，音频播放时会加载对应的`LRC`文件
    `audio.lrc`支持下面格式的歌词：  `[mm:ss]APlayer[mm:ss.xx]is`
    `[mm:ss.xxx]amazing`  `[mm:ss.xx][mm:ss.xx]APlayer`
    `[mm:ss.xx]<mm:ss.xx>is`  `[mm:ss.xx]amazing[mm:ss.xx]APlayer`.

- listFolded (boolean; default False):
    列表是否默认折叠  默认值：`False`.

- listMaxHeight (number; optional):
    设置列表最大高度.

- storageName (string; default 'aplayer-setting'):
    存储播放器设置的`localStorage key`  默认值：`'aplayer-setting'`.

- play (boolean; default False):
    播放音频，每次设置为`True`后执行完相应操作后会自动置为`False`.

- pause (boolean; default False):
    暂停音频，每次设置为`True`后执行完相应操作后会自动置为`False`.

- seek (dict; default { isSeek: False }):
    跳转到特定时间，时间的单位为秒，每次`isSeek`设置为`True`后执行完相应操作后会自动置为`False`.

    `seek` is a dict with keys:

    - isSeek (boolean; optional):
        是否跳转到特定时间.

    - time (number; optional):
        跳转到的时间.

- skipBack (boolean; default False):
    切换到上一首音频，每次设置为`True`后执行完相应操作后会自动置为`False`.

- skipForward (boolean; default False):
    切换到下一首音频，每次设置为`True`后执行完相应操作后会自动置为`False`.

- showLrc (boolean; default False):
    显示歌词，每次设置为`True`后执行完相应操作后会自动置为`False`.

- hideLrc (boolean; default False):
    隐藏歌词，每次设置为`True`后执行完相应操作后会自动置为`False`.

- notice (dict; default { isShow: False, time: 2000, opacity: 0.8 }):
    显示通知信息，每次`isShow`设置为`True`后执行完相应操作后会自动置为`False`.

    `notice` is a dict with keys:

    - isShow (boolean; optional):
        是否显示通知信息.

    - text (string; optional):
        通知内容.

    - time (number; optional):
        通知持续时间，单位为毫秒，设置时间为`0`可以取消通知自动隐藏.

    - opacity (number; optional):
        通知透明度.

- showList (boolean; default False):
    显示播放列表，每次设置为`True`后执行完相应操作后会自动置为`False`.

- hideList (boolean; default False):
    隐藏播放列表，每次设置为`True`后执行完相应操作后会自动置为`False`.

- addList (dict; default { isAdd: False }):
    增加音频到播放列表，每次`isAdd`设置为`True`后执行完相应操作后会自动置为`False`.

    `addList` is a dict with keys:

    - isAdd (boolean; optional):
        是否增加音频到播放列表.

    - audio (list of dicts; optional):
        音频信息.

        `audio` is a list of dicts with keys:

        - name (string; optional):

            设置音频名称.

        - artist (string; optional):

            设置音频作者.

        - url (string; optional):

            设置音频链接.

        - cover (string; optional):

            设置音频封面.

        - lrc (string; optional):

            设置音频`lrc`歌词.

        - theme (string; optional):

            设置切换到此音频时的主题色，比上面的`theme`优先级高.

        - type (a value equal to: 'auto', 'hls', 'normal'; optional):

            设置音频类型，可选的有`'auto'`、`'hls'`、`'normal'`  默认值：`'auto'`.

- removeList (dict; default { isRemove: False }):
    删除播放列表中的音频，每次`isRemove`设置为`True`后执行完相应操作后会自动置为`False`.

    `removeList` is a dict with keys:

    - isRemove (boolean; optional):
        是否删除播放列表中的音频.

    - index (number; optional):
        音频索引.

- switchList (dict; default { isSwitch: False }):
    切换播放列表，每次`isSwitch`设置为`True`后执行完相应操作后会自动置为`False`.

    `switchList` is a dict with keys:

    - isSwitch (boolean; optional):
        是否切换播放列表.

    - index (number; optional):
        音频索引.

- clearList (boolean; default False):
    清空播放列表，每次设置为`True`后执行完相应操作后会自动置为`False`.

- destroy (boolean; default False):
    销毁播放器，每次设置为`True`后执行完相应操作后会自动置为`False`.

- playClicks (number; default 0):
    监听参数，播放音频的次数.

- pauseClicks (number; default 0):
    监听参数，暂停音频的次数.

- seekClicks (number; default 0):
    监听参数，跳转到特定时间的次数.

- skipBackClicks (number; default 0):
    监听参数，通过函数切换到上一首音频的次数.

- skipForwardClicks (number; default 0):
    监听参数，通过函数切换到下一首音频的次数.

- showLrcClicks (number; default 0):
    监听参数，显示歌词的次数.

- hideLrcClicks (number; default 0):
    监听参数，隐藏歌词的次数.

- showNoticeClicks (number; default 0):
    监听参数，显示通知的次数.

- hideNoticeClicks (number; default 0):
    监听参数，隐藏通知的次数.

- listShowClicks (number; default 0):
    监听参数，显示播放列表的次数.

- listHideClicks (number; default 0):
    监听参数，隐藏播放列表的次数.

- listAddClicks (number; default 0):
    监听参数，添加音频到播放列表的次数.

- listRemoveClicks (number; default 0):
    监听参数，删除音频的次数.

- listSwitchClicks (number; default 0):
    监听参数，切换到播放列表里的其他音频的次数.

- listClearClicks (number; default 0):
    监听参数，清空播放列表的次数.

- destroyClicks (number; default 0):
    监听参数，播放器销毁的次数.

- currentPlayAudioInfo (dict; optional):
    监听参数，当前播放的音频信息.

- currentPauseAudioInfo (dict; optional):
    监听参数，当前暂停的音频信息.

- currentSeekAudioInfo (dict; optional):
    监听参数，当前改动进度条的音频信息.

- currentNoticeInfo (dict; optional):
    监听参数，当前显示的通知信息.

- currentListAddAudioInfo (dict; optional):
    监听参数，当前列表执行添加操作的音频信息.

- currentListRemoveAudioInfo (dict; optional):
    监听参数，当前列表执行移除操作的音频信息.

- currentListSwitchAudioInfo (dict; optional):
    监听参数，当前列表切换到的音频信息."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyAPlayer'
    Audio = TypedDict(
        "Audio",
            {
            "name": NotRequired[str],
            "artist": NotRequired[str],
            "url": NotRequired[str],
            "cover": NotRequired[str],
            "lrc": NotRequired[str],
            "theme": NotRequired[str],
            "type": NotRequired[Literal["auto", "hls", "normal"]]
        }
    )

    Seek = TypedDict(
        "Seek",
            {
            "isSeek": NotRequired[bool],
            "time": NotRequired[NumberType]
        }
    )

    Notice = TypedDict(
        "Notice",
            {
            "isShow": NotRequired[bool],
            "text": NotRequired[str],
            "time": NotRequired[NumberType],
            "opacity": NotRequired[NumberType]
        }
    )

    AddListAudio = TypedDict(
        "AddListAudio",
            {
            "name": NotRequired[str],
            "artist": NotRequired[str],
            "url": NotRequired[str],
            "cover": NotRequired[str],
            "lrc": NotRequired[str],
            "theme": NotRequired[str],
            "type": NotRequired[Literal["auto", "hls", "normal"]]
        }
    )

    AddList = TypedDict(
        "AddList",
            {
            "isAdd": NotRequired[bool],
            "audio": NotRequired[typing.Sequence["AddListAudio"]]
        }
    )

    RemoveList = TypedDict(
        "RemoveList",
            {
            "isRemove": NotRequired[bool],
            "index": NotRequired[NumberType]
        }
    )

    SwitchList = TypedDict(
        "SwitchList",
            {
            "isSwitch": NotRequired[bool],
            "index": NotRequired[NumberType]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        key: typing.Optional[str] = None,
        style: typing.Optional[typing.Any] = None,
        className: typing.Optional[typing.Union[str, dict]] = None,
        fixed: typing.Optional[bool] = None,
        mini: typing.Optional[bool] = None,
        autoplay: typing.Optional[bool] = None,
        theme: typing.Optional[str] = None,
        loop: typing.Optional[Literal["all", "one", "none"]] = None,
        order: typing.Optional[Literal["list", "random"]] = None,
        preload: typing.Optional[Literal["none", "metadata", "auto"]] = None,
        volume: typing.Optional[NumberType] = None,
        audio: typing.Optional[typing.Sequence["Audio"]] = None,
        mutex: typing.Optional[bool] = None,
        lrcType: typing.Optional[Literal[0, 1, 2, 3]] = None,
        listFolded: typing.Optional[bool] = None,
        listMaxHeight: typing.Optional[NumberType] = None,
        storageName: typing.Optional[str] = None,
        play: typing.Optional[bool] = None,
        pause: typing.Optional[bool] = None,
        seek: typing.Optional["Seek"] = None,
        skipBack: typing.Optional[bool] = None,
        skipForward: typing.Optional[bool] = None,
        showLrc: typing.Optional[bool] = None,
        hideLrc: typing.Optional[bool] = None,
        notice: typing.Optional["Notice"] = None,
        showList: typing.Optional[bool] = None,
        hideList: typing.Optional[bool] = None,
        addList: typing.Optional["AddList"] = None,
        removeList: typing.Optional["RemoveList"] = None,
        switchList: typing.Optional["SwitchList"] = None,
        clearList: typing.Optional[bool] = None,
        destroy: typing.Optional[bool] = None,
        playClicks: typing.Optional[NumberType] = None,
        pauseClicks: typing.Optional[NumberType] = None,
        seekClicks: typing.Optional[NumberType] = None,
        skipBackClicks: typing.Optional[NumberType] = None,
        skipForwardClicks: typing.Optional[NumberType] = None,
        showLrcClicks: typing.Optional[NumberType] = None,
        hideLrcClicks: typing.Optional[NumberType] = None,
        showNoticeClicks: typing.Optional[NumberType] = None,
        hideNoticeClicks: typing.Optional[NumberType] = None,
        listShowClicks: typing.Optional[NumberType] = None,
        listHideClicks: typing.Optional[NumberType] = None,
        listAddClicks: typing.Optional[NumberType] = None,
        listRemoveClicks: typing.Optional[NumberType] = None,
        listSwitchClicks: typing.Optional[NumberType] = None,
        listClearClicks: typing.Optional[NumberType] = None,
        destroyClicks: typing.Optional[NumberType] = None,
        currentPlayAudioInfo: typing.Optional[dict] = None,
        currentPauseAudioInfo: typing.Optional[dict] = None,
        currentSeekAudioInfo: typing.Optional[dict] = None,
        currentNoticeInfo: typing.Optional[dict] = None,
        currentListAddAudioInfo: typing.Optional[dict] = None,
        currentListRemoveAudioInfo: typing.Optional[dict] = None,
        currentListSwitchAudioInfo: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'key', 'style', 'className', 'fixed', 'mini', 'autoplay', 'theme', 'loop', 'order', 'preload', 'volume', 'audio', 'mutex', 'lrcType', 'listFolded', 'listMaxHeight', 'storageName', 'play', 'pause', 'seek', 'skipBack', 'skipForward', 'showLrc', 'hideLrc', 'notice', 'showList', 'hideList', 'addList', 'removeList', 'switchList', 'clearList', 'destroy', 'playClicks', 'pauseClicks', 'seekClicks', 'skipBackClicks', 'skipForwardClicks', 'showLrcClicks', 'hideLrcClicks', 'showNoticeClicks', 'hideNoticeClicks', 'listShowClicks', 'listHideClicks', 'listAddClicks', 'listRemoveClicks', 'listSwitchClicks', 'listClearClicks', 'destroyClicks', 'currentPlayAudioInfo', 'currentPauseAudioInfo', 'currentSeekAudioInfo', 'currentNoticeInfo', 'currentListAddAudioInfo', 'currentListRemoveAudioInfo', 'currentListSwitchAudioInfo']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'fixed', 'mini', 'autoplay', 'theme', 'loop', 'order', 'preload', 'volume', 'audio', 'mutex', 'lrcType', 'listFolded', 'listMaxHeight', 'storageName', 'play', 'pause', 'seek', 'skipBack', 'skipForward', 'showLrc', 'hideLrc', 'notice', 'showList', 'hideList', 'addList', 'removeList', 'switchList', 'clearList', 'destroy', 'playClicks', 'pauseClicks', 'seekClicks', 'skipBackClicks', 'skipForwardClicks', 'showLrcClicks', 'hideLrcClicks', 'showNoticeClicks', 'hideNoticeClicks', 'listShowClicks', 'listHideClicks', 'listAddClicks', 'listRemoveClicks', 'listSwitchClicks', 'listClearClicks', 'destroyClicks', 'currentPlayAudioInfo', 'currentPauseAudioInfo', 'currentSeekAudioInfo', 'currentNoticeInfo', 'currentListAddAudioInfo', 'currentListRemoveAudioInfo', 'currentListSwitchAudioInfo']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyAPlayer, self).__init__(**args)

setattr(FefferyAPlayer, "__init__", _explicitize_args(FefferyAPlayer.__init__))
