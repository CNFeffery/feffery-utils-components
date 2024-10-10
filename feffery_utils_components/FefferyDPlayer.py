# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyDPlayer(Component):
    """A FefferyDPlayer component.


Keyword arguments:

- id (string; optional):
    播放器id.

- className (string; optional):
    设置播放器的css类名.

- style (dict; optional):
    设置播放器的样式.

- key (string; optional):
    设置播放器的key，强制刷新组件.

- live (boolean; default False):
    是否开启开启直播模式，默认为False.

- autoplay (boolean; default False):
    视频是否自动播放，默认为False.

- theme (string; default '#b7daff'):
    设置主题色，默认为'#b7daff'.

- loop (boolean; default False):
    视频是否循环播放, 默认为False.

- lang (a value equal to: 'en', 'zh-cn', 'zh-tw'; default 'zh-cn'):
    设置语言， 可选值: 'en', 'zh-cn', 'zh-tw'，默认为'zh-cn'.

- screenshot (boolean; default False):
    是否开启截图，如果开启，视频和视频封面需要允许跨域， 默认为False.

- airplay (boolean; default False):
    在 Safari 中是否开启 AirPlay，默认False.

- hotkey (boolean; default True):
    是否开启热键，支持快进、快退、音量控制、播放暂停， 默认为True.

- chromecast (boolean; default False):
    是否启用Chromecast，默认False.

- preload (a value equal to: 'none', 'metadata', 'auto'; default 'auto'):
    设置音频预加载，可选值: 'none', 'metadata', 'auto'，默认为'auto'.

- volume (number; default 0.7):
    默认音量，请注意播放器会记忆用户设置，用户手动设置音量后默认音量即失效.

- playbackSpeed (list of numbers; default [0.5, 0.75, 1, 1.25, 1.5, 2]):
    可选的播放速率，可以设置成自定义的数组.

- logo (string; optional):
    在左上角展示一个 logo，你可以通过 CSS 调整它的大小和位置.

- preventClickToggle (boolean; default False):
    是否阻止点击播放器时候自动切换播放/暂停，默认为False.

- video (dict; default {    type: 'auto'}):
    设置视频信息.

    `video` is a dict with keys:

    - quality (list of dicts; optional):
        设置清晰度切换.

        `quality` is a list of dicts with keys:

        - name (string; optional):

            设置清晰度名称.

        - url (string; optional):

            设置视频链接.

        - type (a value equal to: 'auto', 'hls', 'flv', 'dash', 'normal'; optional):

            设置视频类型，可选的有'auto'、'hls'、'flv'、 'dash'、'normal'，默认为'auto'.

    - defaultQuality (number; optional):
        设置默认清晰度.

    - url (string; optional):
        设置视频链接.

    - pic (string; optional):
        设置视频封面.

    - thumbnails (string; optional):
        设置视频缩略图.

    - type (a value equal to: 'auto', 'hls', 'flv', 'dash', 'normal'; optional):
        设置视频类型，可选的有'auto'、'hls'、'flv'、 'dash'、'normal'，默认为'auto'.

    - customType (dict; optional):
        自定义视频类型，此参数无需设置，会根据设置的type参数自动接管.

- subtitle (dict; default {    isOpen: False,    type: 'webvtt',    fontSize: '20px',    bottom: '40px',    color: '#fff'}):
    设置外挂字幕.

    `subtitle` is a dict with keys:

    - isOpen (boolean; optional):
        是否开启外挂字幕，默认为False.

    - url (string; optional):
        设置字幕链接.

    - type (a value equal to: 'webvtt', 'ass'; optional):
        设置字幕类型，可选的有'webvtt'、'ass'，默认为'webvtt'，目前只支持 webvtt.

    - fontSize (string; optional):
        设置字幕字号.

    - bottom (string; optional):
        设置字幕距离播放器底部的距离，取值形如: '10px' '10%'.

    - color (string; optional):
        设置字幕颜色.

- danmaku (dict; default {    isOpen: False,    unlimited: False,    speedRate: 1}):
    设置弹幕.

    `danmaku` is a dict with keys:

    - isOpen (boolean; optional):
        是否开启弹幕，默认为False.

    - id (string; optional):
        设置弹幕弹幕池id，必须唯一，设置弹幕时必选.

    - api (string; optional):
        设置弹幕接口，设置弹幕时必选.

    - token (string; optional):
        设置弹幕后端验证token.

    - maximum (number; optional):
        设置弹幕最大数量.

    - addition (list of strings; optional):
        设置额外外挂弹幕.

    - user (string; optional):
        设置弹幕用户名.

    - bottom (string; optional):
        设置弹幕距离播放器底部的距离，防止遮挡字幕，取值形如: '10px' '10%'.

    - unlimited (boolean; optional):
        设置海量弹幕模式，即使重叠也展示全部弹幕，请注意播放器会记忆用户设置，用户手动设置后即失效，默认为False.

    - speedRate (number; optional):
        设置弹幕速度倍率，越大速度越快，默认为1.

- contextmenu (list of dicts; optional):
    自定义右键菜单.

    `contextmenu` is a list of dicts with keys:

    - text (string; optional):
        菜单名称.

    - extraInfo (dict; optional):
        菜单额外携带的信息.

- highlight (list of dicts; optional):
    自定义进度条提示点.

    `highlight` is a list of dicts with keys:

    - time (number; optional):
        进度条提示点的时间点.

    - text (string; optional):
        进度条提示点的文字.

- mutex (boolean; default True):
    是否互斥，阻止多个播放器同时播放，当前播放器播放时暂停其他播放器，默认为True.

- play (boolean; default False):
    播放视频，每次设置为True后执行完相应操作后会自动置为False.

- pause (boolean; default False):
    暂停视频，每次设置为True后执行完相应操作后会自动置为False.

- seek (dict; default {    isSeek: False}):
    跳转到特定时间，时间的单位为秒，每次isSeek设置为True后执行完相应操作后会自动置为False.

    `seek` is a dict with keys:

    - isSeek (boolean; optional)

    - time (number; optional):
        跳转到的时间.

- notice (dict; default {    isShow: False,    time: 2000,    opacity: 0.8}):
    显示通知信息，每次isShow设置为True后执行完相应操作后会自动置为False.

    `notice` is a dict with keys:

    - isShow (boolean; optional)

    - text (string; optional):
        通知内容.

    - time (number; optional):
        通知持续时间，单位为毫秒，设置时间为 0 可以取消通知自动隐藏.

    - opacity (number; optional):
        通知透明度.

- speed (dict; default {    isSpeed: False}):
    设置视频速度，每次isSpeed设置为True后执行完相应操作后会自动置为False.

    `speed` is a dict with keys:

    - isSpeed (boolean; optional)

    - rate (number; optional):
        视频速度.

- volumeSet (dict; default {    isVolume: False,    nostorage: True,    nonotice: False}):
    设置音量，每次isVolume设置为True后执行完相应操作后会自动置为False.

    `volumeSet` is a dict with keys:

    - isVolume (boolean; optional)

    - percentage (number; optional):
        音量，取值范围为0-1.

    - nostorage (boolean; optional):
        是否不缓存.

    - nonotice (boolean; optional):
        是否不显示通知.

- fullScreen (dict; default {    isFullScreen: False,    type: 'browser'}):
    设置全屏，每次isFullScreen设置为True后执行完相应操作后会自动置为False.

    `fullScreen` is a dict with keys:

    - isFullScreen (boolean; optional):
        是否全屏，每次设置为True后执行完相应操作后会自动置为False.

    - type (a value equal to: 'web', 'browser'; optional):
        全屏的类型，可选的有'web'、'browser'，默认为'browser'.

    - operate (a value equal to: 'request', 'cancel'; optional):
        全屏操作类型，可选的有'request'、'cancel'.

- switchQuality (dict; default {    isSwitch: False}):
    切换清晰度，每次isSwitch设置为True后执行完相应操作后会自动置为False.

    `switchQuality` is a dict with keys:

    - isSwitch (boolean; optional)

    - index (number; optional):
        切换的清晰度index.

- switchVideo (dict; default {    isSwitch: False}):
    切换视频，每次isSwitch设置为True后执行完相应操作后会自动置为False.

    `switchVideo` is a dict with keys:

    - isSwitch (boolean; optional)

    - video (dict; optional):
        切换的视频信息.

        `video` is a dict with keys:

        - quality (list of dicts; optional):
            设置清晰度切换.

            `quality` is a list of dicts with keys:

    - name (string; optional):
        设置清晰度名称.

    - url (string; optional):
        设置视频链接.

    - type (a value equal to: 'auto', 'hls', 'flv', 'dash', 'normal'; optional):
        设置视频类型，可选的有'auto'、'hls'、'flv'、 'dash'、'normal'，默认为'auto'.

        - defaultQuality (number; optional):
            设置默认清晰度.

        - url (string; optional):
            设置视频链接.

        - pic (string; optional):
            设置视频封面.

        - thumbnails (string; optional):
            设置视频缩略图.

        - type (a value equal to: 'auto', 'hls', 'flv', 'dash', 'normal'; optional):
            设置视频类型，可选的有'auto'、'hls'、'flv'、 'dash'、'normal'，默认为'auto'.

        - customType (dict; optional):
            自定义视频类型，此参数无需设置，会根据设置的type参数自动接管.

    - danmaku (dict; optional):
        切换的视频弹幕信息.

        `danmaku` is a dict with keys:

        - isOpen (boolean; optional):
            是否开启弹幕，默认为False.

        - id (string; optional):
            设置弹幕弹幕池id，必须唯一，设置弹幕时必选.

        - api (string; optional):
            设置弹幕接口，设置弹幕时必选.

        - token (string; optional):
            设置弹幕后端验证token.

        - maximum (number; optional):
            设置弹幕最大数量.

        - addition (list of strings; optional):
            设置额外外挂弹幕.

        - user (string; optional):
            设置弹幕用户名.

        - bottom (string; optional):
            设置弹幕距离播放器底部的距离，防止遮挡字幕，取值形如: '10px' '10%'.

        - unlimited (boolean; optional):
            设置海量弹幕模式，即使重叠也展示全部弹幕，请注意播放器会记忆用户设置，用户手动设置后即失效，默认为False.

        - speedRate (number; optional):
            设置弹幕速度倍率，越大速度越快，默认为1.

- sendDanmaku (dict; default {    isSend: False}):
    发送弹幕，每次isSend设置为True后执行完相应操作后会自动置为False.

    `sendDanmaku` is a dict with keys:

    - isSend (boolean; optional)

    - content (dict; optional):
        发送的弹幕内容.

        `content` is a dict with keys:

        - text (string; optional):
            弹幕内容.

        - color (string; optional):
            弹幕颜色.

        - type (a value equal to: 'top', 'bottom', 'right'; optional):
            弹幕位置.

- drawDanmaku (dict; default {    isDraw: False}):
    绘制弹幕，每次isDraw设置为True后执行完相应操作后会自动置为False.

    `drawDanmaku` is a dict with keys:

    - isDraw (boolean; optional)

    - content (dict; optional):
        绘制的弹幕内容.

        `content` is a dict with keys:

        - text (string; optional):
            弹幕内容.

        - color (string; optional):
            弹幕颜色.

        - type (a value equal to: 'top', 'bottom', 'right'; optional):
            弹幕位置.

- opacityDanmaku (dict; default {    isOpacity: False}):
    设置弹幕透明度，每次isOpacity设置为True后执行完相应操作后会自动置为False.

    `opacityDanmaku` is a dict with keys:

    - isOpacity (boolean; optional)

    - opacity (number; optional):
        弹幕透明度，取值范围为0-1.

- clearDanmaku (boolean; default False):
    清空弹幕，每次设置为True后执行完相应操作后会自动置为False.

- hideDanmaku (boolean; default False):
    隐藏弹幕，每次设置为True后执行完相应操作后会自动置为False.

- showDanmaku (boolean; default False):
    显示弹幕，每次设置为True后执行完相应操作后会自动置为False.

- destroy (boolean; default False):
    销毁播放器，每次设置为True后执行完相应操作后会自动置为False.

- playClicks (number; default 0):
    监听参数，播放视频的次数.

- pauseClicks (number; default 0):
    监听参数，暂停视频的次数.

- seekClicks (number; default 0):
    监听参数，跳转到特定时间的次数.

- showNoticeClicks (number; default 0):
    监听参数，显示通知的次数.

- hideNoticeClicks (number; default 0):
    监听参数，隐藏通知的次数.

- speedClicks (number; default 0):
    监听参数，设置视频速度的次数.

- volumeSetClicks (number; default 0):
    监听参数，设置音量的次数.

- fullScreenClicks (number; default 0):
    监听参数，进入网页全屏的次数.

- cancelFullScreenClicks (number; default 0):
    监听参数，退出网页全屏的次数.

- sendDanmakuCallback (dict; default {    sendDanmakuClicks: 0}):
    监听参数，发送弹幕的次数和信息.

    `sendDanmakuCallback` is a dict with keys:

    - sendDanmakuClicks (number; optional)

    - sendInfo (dict; optional):
        发送的弹幕信息.

- drawDanmakuClicks (number; default 0):
    监听参数，通过函数绘制弹幕的次数.

- clearDanmakuClicks (number; default 0):
    监听参数，清空弹幕的次数.

- opacityDanmakuCallback (dict; default {    opacityDanmakuClicks: 0}):
    监听参数，设置弹幕透明度的次数和透明度.

    `opacityDanmakuCallback` is a dict with keys:

    - opacityDanmakuClicks (number; optional)

    - opacity (number; optional):
        弹幕透明度，取值范围为0-1.

- showDanmakuClicks (number; default 0):
    监听参数，显示弹幕的次数.

- hideDanmakuClicks (number; default 0):
    监听参数，隐藏弹幕的次数.

- subtitleShowClicks (number; default 0):
    监听参数，显示字幕的次数.

- subtitleHideClicks (number; default 0):
    监听参数，隐藏字幕的次数.

- subtitleChangeClicks (number; default 0):
    监听参数，切换字幕的次数.

- screenshotClicks (number; default 0):
    监听参数，截图的次数.

- contextmenuShowClicks (number; default 0):
    监听参数，右键菜单显示的次数.

- contextmenuHideClicks (number; default 0):
    监听参数，右键菜单隐藏的次数.

- currentClickContextmenu (dict; optional):
    监听参数，当前点击的右键菜单信息.

- destroyClicks (number; default 0):
    监听参数，播放器销毁的次数.

- currentNoticeInfo (dict; optional):
    监听参数，当前通知信息.

- currentVideoInfo (dict; optional):
    监听参数，当前视频的信息.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyDPlayer'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, key=Component.UNDEFINED, live=Component.UNDEFINED, autoplay=Component.UNDEFINED, theme=Component.UNDEFINED, loop=Component.UNDEFINED, lang=Component.UNDEFINED, screenshot=Component.UNDEFINED, airplay=Component.UNDEFINED, hotkey=Component.UNDEFINED, chromecast=Component.UNDEFINED, preload=Component.UNDEFINED, volume=Component.UNDEFINED, playbackSpeed=Component.UNDEFINED, logo=Component.UNDEFINED, preventClickToggle=Component.UNDEFINED, video=Component.UNDEFINED, subtitle=Component.UNDEFINED, danmaku=Component.UNDEFINED, contextmenu=Component.UNDEFINED, highlight=Component.UNDEFINED, mutex=Component.UNDEFINED, play=Component.UNDEFINED, pause=Component.UNDEFINED, seek=Component.UNDEFINED, notice=Component.UNDEFINED, speed=Component.UNDEFINED, volumeSet=Component.UNDEFINED, fullScreen=Component.UNDEFINED, switchQuality=Component.UNDEFINED, switchVideo=Component.UNDEFINED, sendDanmaku=Component.UNDEFINED, drawDanmaku=Component.UNDEFINED, opacityDanmaku=Component.UNDEFINED, clearDanmaku=Component.UNDEFINED, hideDanmaku=Component.UNDEFINED, showDanmaku=Component.UNDEFINED, destroy=Component.UNDEFINED, playClicks=Component.UNDEFINED, pauseClicks=Component.UNDEFINED, seekClicks=Component.UNDEFINED, showNoticeClicks=Component.UNDEFINED, hideNoticeClicks=Component.UNDEFINED, speedClicks=Component.UNDEFINED, volumeSetClicks=Component.UNDEFINED, fullScreenClicks=Component.UNDEFINED, cancelFullScreenClicks=Component.UNDEFINED, sendDanmakuCallback=Component.UNDEFINED, drawDanmakuClicks=Component.UNDEFINED, clearDanmakuClicks=Component.UNDEFINED, opacityDanmakuCallback=Component.UNDEFINED, showDanmakuClicks=Component.UNDEFINED, hideDanmakuClicks=Component.UNDEFINED, subtitleShowClicks=Component.UNDEFINED, subtitleHideClicks=Component.UNDEFINED, subtitleChangeClicks=Component.UNDEFINED, screenshotClicks=Component.UNDEFINED, contextmenuShowClicks=Component.UNDEFINED, contextmenuHideClicks=Component.UNDEFINED, currentClickContextmenu=Component.UNDEFINED, destroyClicks=Component.UNDEFINED, currentNoticeInfo=Component.UNDEFINED, currentVideoInfo=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'key', 'live', 'autoplay', 'theme', 'loop', 'lang', 'screenshot', 'airplay', 'hotkey', 'chromecast', 'preload', 'volume', 'playbackSpeed', 'logo', 'preventClickToggle', 'video', 'subtitle', 'danmaku', 'contextmenu', 'highlight', 'mutex', 'play', 'pause', 'seek', 'notice', 'speed', 'volumeSet', 'fullScreen', 'switchQuality', 'switchVideo', 'sendDanmaku', 'drawDanmaku', 'opacityDanmaku', 'clearDanmaku', 'hideDanmaku', 'showDanmaku', 'destroy', 'playClicks', 'pauseClicks', 'seekClicks', 'showNoticeClicks', 'hideNoticeClicks', 'speedClicks', 'volumeSetClicks', 'fullScreenClicks', 'cancelFullScreenClicks', 'sendDanmakuCallback', 'drawDanmakuClicks', 'clearDanmakuClicks', 'opacityDanmakuCallback', 'showDanmakuClicks', 'hideDanmakuClicks', 'subtitleShowClicks', 'subtitleHideClicks', 'subtitleChangeClicks', 'screenshotClicks', 'contextmenuShowClicks', 'contextmenuHideClicks', 'currentClickContextmenu', 'destroyClicks', 'currentNoticeInfo', 'currentVideoInfo', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'key', 'live', 'autoplay', 'theme', 'loop', 'lang', 'screenshot', 'airplay', 'hotkey', 'chromecast', 'preload', 'volume', 'playbackSpeed', 'logo', 'preventClickToggle', 'video', 'subtitle', 'danmaku', 'contextmenu', 'highlight', 'mutex', 'play', 'pause', 'seek', 'notice', 'speed', 'volumeSet', 'fullScreen', 'switchQuality', 'switchVideo', 'sendDanmaku', 'drawDanmaku', 'opacityDanmaku', 'clearDanmaku', 'hideDanmaku', 'showDanmaku', 'destroy', 'playClicks', 'pauseClicks', 'seekClicks', 'showNoticeClicks', 'hideNoticeClicks', 'speedClicks', 'volumeSetClicks', 'fullScreenClicks', 'cancelFullScreenClicks', 'sendDanmakuCallback', 'drawDanmakuClicks', 'clearDanmakuClicks', 'opacityDanmakuCallback', 'showDanmakuClicks', 'hideDanmakuClicks', 'subtitleShowClicks', 'subtitleHideClicks', 'subtitleChangeClicks', 'screenshotClicks', 'contextmenuShowClicks', 'contextmenuHideClicks', 'currentClickContextmenu', 'destroyClicks', 'currentNoticeInfo', 'currentVideoInfo', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyDPlayer, self).__init__(**args)
