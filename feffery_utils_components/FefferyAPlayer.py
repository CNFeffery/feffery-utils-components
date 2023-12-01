# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyAPlayer(Component):
    """A FefferyAPlayer component.


Keyword arguments:

- id (string; optional):
    播放器id.

- addList (dict; default {    isAdd: False}):
    增加音频到播放列表，每次isAdd设置为True后执行完相应操作后会自动置为False.

    `addList` is a dict with keys:

    - audio (list of dicts; optional):
        音频信息.

        `audio` is a list of dicts with keys:

        - artist (string; optional):

            设置音频作者.

        - cover (string; optional):

            设置音频封面.

        - lrc (string; optional):

            设置音频lrc歌词.

        - name (string; optional):

            设置音频名称.

        - theme (string; optional):

            设置切换到此音频时的主题色，比上面的 theme 优先级高.

        - type (a value equal to: 'auto', 'hls', 'normal'; optional):

            设置音频类型，可选的有'auto'、'hls'、'normal'，默认为'auto'.

        - url (string; optional):

            设置音频链接.

    - isAdd (boolean; optional)

- audio (list of dicts; default [{    type: 'auto'}]):
    设置音频信息.

    `audio` is a list of dicts with keys:

    - artist (string; optional):
        设置音频作者.

    - cover (string; optional):
        设置音频封面.

    - lrc (string; optional):
        设置音频lrc歌词.

    - name (string; optional):
        设置音频名称.

    - theme (string; optional):
        设置切换到此音频时的主题色，比上面的 theme 优先级高.

    - type (a value equal to: 'auto', 'hls', 'normal'; optional):
        设置音频类型，可选的有'auto'、'hls'、'normal'，默认为'auto'.

    - url (string; optional):
        设置音频链接.

- autoplay (boolean; default False):
    音频是否自动播放，默认为False.

- className (string; optional):
    设置播放器的css类名.

- clearList (boolean; default False):
    清空播放列表，每次设置为True后执行完相应操作后会自动置为False.

- currentListAddAudioInfo (dict; optional):
    监听参数，当前列表执行添加操作的音频信息.

- currentListRemoveAudioInfo (dict; optional):
    监听参数，当前列表执行移除操作的音频信息.

- currentListSwitchAudioInfo (dict; optional):
    监听参数，当前列表切换到的音频信息.

- currentNoticeInfo (dict; optional):
    监听参数，当前显示的通知信息.

- currentPauseAudioInfo (dict; optional):
    监听参数，当前暂停的音频信息.

- currentPlayAudioInfo (dict; optional):
    监听参数，当前播放的音频信息.

- currentSeekAudioInfo (dict; optional):
    监听参数，当前改动进度条的音频信息.

- destroy (boolean; default False):
    销毁播放器，每次设置为True后执行完相应操作后会自动置为False.

- destroyClicks (number; default 0):
    监听参数，播放器销毁的次数.

- fixed (boolean; default False):
    是否开启吸底模式，默认为False.

- hideList (boolean; default False):
    隐藏播放列表，每次设置为True后执行完相应操作后会自动置为False.

- hideLrc (boolean; default False):
    隐藏歌词，每次设置为True后执行完相应操作后会自动置为False.

- hideLrcClicks (number; default 0):
    监听参数，隐藏歌词的次数.

- hideNoticeClicks (number; default 0):
    监听参数，隐藏通知的次数.

- key (string; optional):
    设置播放器的key，强制刷新组件.

- listAddClicks (number; default 0):
    监听参数，添加音频到播放列表的次数.

- listClearClicks (number; default 0):
    监听参数，清空播放列表的次数.

- listFolded (boolean; default False):
    列表是否默认折叠，默认为False.

- listHideClicks (number; default 0):
    监听参数，隐藏播放列表的次数.

- listMaxHeight (number; optional):
    设置列表最大高度.

- listRemoveClicks (number; default 0):
    监听参数，删除音频的次数.

- listShowClicks (number; default 0):
    监听参数，显示播放列表的次数.

- listSwitchClicks (number; default 0):
    监听参数，切换到播放列表里的其他音频的次数.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- loop (a value equal to: 'all', 'one', 'none'; default 'all'):
    设置音频循环播放, 可选值: 'all', 'one', 'none'，默认为'all'.

- lrcType (a value equal to: 0, 1, 2, 3; default 0):
    有三种方式来给APlayer传递歌词，使用lrcType参数指明使用哪种方式，然后把歌词放到audio.lrc参数或者HTML里
    1表示把歌词放到JS字符串里面，2表示把歌词放到HTML里面，3表示把歌词放到 LRC 文件里，音频播放时会加载对应的 LRC 文件
    audio.lrc支持下面格式的歌词：  [mm:ss]APlayer[mm:ss.xx]is
    [mm:ss.xxx]amazing  [mm:ss.xx][mm:ss.xx]APlayer
    [mm:ss.xx]<mm:ss.xx>is  [mm:ss.xx]amazing[mm:ss.xx]APlayer.

- mini (boolean; default False):
    是否开启迷你模式，默认为False.

- mutex (boolean; default True):
    是否互斥，阻止多个播放器同时播放，当前播放器播放时暂停其他播放器，默认为True.

- notice (dict; default {    isShow: False,    time: 2000,    opacity: 0.8}):
    显示通知信息，每次isShow设置为True后执行完相应操作后会自动置为False.

    `notice` is a dict with keys:

    - isShow (boolean; optional)

    - opacity (number; optional):
        通知透明度.

    - text (string; optional):
        通知内容.

    - time (number; optional):
        通知持续时间，单位为毫秒，设置时间为 0 可以取消通知自动隐藏.

- order (a value equal to: 'list', 'random'; default 'list'):
    设置音频循环顺序, 可选值: 'list', 'random'，默认为'list'.

- pause (boolean; default False):
    暂停音频，每次设置为True后执行完相应操作后会自动置为False.

- pauseClicks (number; default 0):
    监听参数，暂停音频的次数.

- play (boolean; default False):
    播放音频，每次设置为True后执行完相应操作后会自动置为False.

- playClicks (number; default 0):
    监听参数，播放音频的次数.

- preload (a value equal to: 'none', 'metadata', 'auto'; default 'auto'):
    设置音频预加载，可选值: 'none', 'metadata', 'auto'，默认为'auto'.

- removeList (dict; default {    isRemove: False}):
    删除播放列表中的音频，每次isDelete设置为True后执行完相应操作后会自动置为False.

    `removeList` is a dict with keys:

    - index (number; optional):
        音频索引.

    - isRemove (boolean; optional)

- seek (dict; default {    isSeek: False}):
    跳转到特定时间，时间的单位为秒，每次isSeek设置为True后执行完相应操作后会自动置为False.

    `seek` is a dict with keys:

    - isSeek (boolean; optional)

    - time (number; optional):
        跳转到的时间.

- seekClicks (number; default 0):
    监听参数，跳转到特定时间的次数.

- showList (boolean; default False):
    显示播放列表，每次设置为True后执行完相应操作后会自动置为False.

- showLrc (boolean; default False):
    显示歌词，每次设置为True后执行完相应操作后会自动置为False.

- showLrcClicks (number; default 0):
    监听参数，显示歌词的次数.

- showNoticeClicks (number; default 0):
    监听参数，显示通知的次数.

- skipBack (boolean; default False):
    切换到上一首音频，每次设置为True后执行完相应操作后会自动置为False.

- skipBackClicks (number; default 0):
    监听参数，通过函数切换到上一首音频的次数.

- skipForward (boolean; default False):
    切换到下一首音频，每次设置为True后执行完相应操作后会自动置为False.

- skipForwardClicks (number; default 0):
    监听参数，通过函数切换到下一首音频的次数.

- storageName (string; default 'aplayer-setting'):
    存储播放器设置的 localStorage key，默认为'aplayer-setting'.

- style (dict; optional):
    设置播放器的样式.

- switchList (dict; default {    isSwitch: False}):
    切换播放列表，每次isSwitch设置为True后执行完相应操作后会自动置为False.

    `switchList` is a dict with keys:

    - index (number; optional):
        音频索引.

    - isSwitch (boolean; optional)

- theme (string; default '#b7daff'):
    设置主题色，默认为'#b7daff'.

- volume (number; default 0.7):
    默认音量，请注意播放器会记忆用户设置，用户手动设置音量后默认音量即失效."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyAPlayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, fixed=Component.UNDEFINED, mini=Component.UNDEFINED, autoplay=Component.UNDEFINED, theme=Component.UNDEFINED, loop=Component.UNDEFINED, order=Component.UNDEFINED, preload=Component.UNDEFINED, volume=Component.UNDEFINED, audio=Component.UNDEFINED, mutex=Component.UNDEFINED, lrcType=Component.UNDEFINED, listFolded=Component.UNDEFINED, listMaxHeight=Component.UNDEFINED, storageName=Component.UNDEFINED, play=Component.UNDEFINED, pause=Component.UNDEFINED, seek=Component.UNDEFINED, skipBack=Component.UNDEFINED, skipForward=Component.UNDEFINED, showLrc=Component.UNDEFINED, hideLrc=Component.UNDEFINED, notice=Component.UNDEFINED, showList=Component.UNDEFINED, hideList=Component.UNDEFINED, addList=Component.UNDEFINED, removeList=Component.UNDEFINED, switchList=Component.UNDEFINED, clearList=Component.UNDEFINED, destroy=Component.UNDEFINED, playClicks=Component.UNDEFINED, pauseClicks=Component.UNDEFINED, seekClicks=Component.UNDEFINED, skipBackClicks=Component.UNDEFINED, skipForwardClicks=Component.UNDEFINED, showLrcClicks=Component.UNDEFINED, hideLrcClicks=Component.UNDEFINED, showNoticeClicks=Component.UNDEFINED, hideNoticeClicks=Component.UNDEFINED, listShowClicks=Component.UNDEFINED, listHideClicks=Component.UNDEFINED, listAddClicks=Component.UNDEFINED, listRemoveClicks=Component.UNDEFINED, listSwitchClicks=Component.UNDEFINED, listClearClicks=Component.UNDEFINED, destroyClicks=Component.UNDEFINED, currentPlayAudioInfo=Component.UNDEFINED, currentPauseAudioInfo=Component.UNDEFINED, currentSeekAudioInfo=Component.UNDEFINED, currentNoticeInfo=Component.UNDEFINED, currentListAddAudioInfo=Component.UNDEFINED, currentListRemoveAudioInfo=Component.UNDEFINED, currentListSwitchAudioInfo=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'addList', 'audio', 'autoplay', 'className', 'clearList', 'currentListAddAudioInfo', 'currentListRemoveAudioInfo', 'currentListSwitchAudioInfo', 'currentNoticeInfo', 'currentPauseAudioInfo', 'currentPlayAudioInfo', 'currentSeekAudioInfo', 'destroy', 'destroyClicks', 'fixed', 'hideList', 'hideLrc', 'hideLrcClicks', 'hideNoticeClicks', 'key', 'listAddClicks', 'listClearClicks', 'listFolded', 'listHideClicks', 'listMaxHeight', 'listRemoveClicks', 'listShowClicks', 'listSwitchClicks', 'loading_state', 'loop', 'lrcType', 'mini', 'mutex', 'notice', 'order', 'pause', 'pauseClicks', 'play', 'playClicks', 'preload', 'removeList', 'seek', 'seekClicks', 'showList', 'showLrc', 'showLrcClicks', 'showNoticeClicks', 'skipBack', 'skipBackClicks', 'skipForward', 'skipForwardClicks', 'storageName', 'style', 'switchList', 'theme', 'volume']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'addList', 'audio', 'autoplay', 'className', 'clearList', 'currentListAddAudioInfo', 'currentListRemoveAudioInfo', 'currentListSwitchAudioInfo', 'currentNoticeInfo', 'currentPauseAudioInfo', 'currentPlayAudioInfo', 'currentSeekAudioInfo', 'destroy', 'destroyClicks', 'fixed', 'hideList', 'hideLrc', 'hideLrcClicks', 'hideNoticeClicks', 'key', 'listAddClicks', 'listClearClicks', 'listFolded', 'listHideClicks', 'listMaxHeight', 'listRemoveClicks', 'listShowClicks', 'listSwitchClicks', 'loading_state', 'loop', 'lrcType', 'mini', 'mutex', 'notice', 'order', 'pause', 'pauseClicks', 'play', 'playClicks', 'preload', 'removeList', 'seek', 'seekClicks', 'showList', 'showLrc', 'showLrcClicks', 'showNoticeClicks', 'skipBack', 'skipBackClicks', 'skipForward', 'skipForwardClicks', 'storageName', 'style', 'switchList', 'theme', 'volume']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyAPlayer, self).__init__(**args)
