import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyDPlayer = React.lazy(() => import(/* webpackChunkName: "feffery_dplayer" */ '../../fragments/player/FefferyDPlayer.react'));

/**
 * 视频播放组件FefferyDPlayer
 */
const FefferyDPlayer = ({
    live = false,
    autoplay = false,
    theme = '#b7daff',
    loop = false,
    lang = 'zh-cn',
    screenshot = false,
    hotkey = true,
    airplay = false,
    chromecast = false,
    preload = 'auto',
    volume = 0.7,
    playbackSpeed = [0.5, 0.75, 1, 1.25, 1.5, 2],
    preventClickToggle = false,
    video = { type: 'auto' },
    subtitle = { isOpen: false, type: 'webvtt', fontSize: '20px', bottom: '40px', color: '#fff' },
    danmaku = { isOpen: false, unlimited: false, speedRate: 1 },
    contextmenu = [],
    highlight = [],
    mutex = true,
    play = false,
    pause = false,
    seek = { isSeek: false },
    notice = { isShow: false, time: 2000, opacity: 0.8 },
    speed = { isSpeed: false },
    volumeSet = { isVolume: false, nostorage: true, nonotice: false },
    fullScreen = { isFullScreen: false, type: 'browser' },
    switchQuality = { isSwitch: false },
    switchVideo = { isSwitch: false },
    sendDanmaku = { isSend: false },
    drawDanmaku = { isDraw: false },
    opacityDanmaku = { isOpacity: false },
    clearDanmaku = false,
    hideDanmaku = false,
    showDanmaku = false,
    destroy = false,
    playClicks = 0,
    pauseClicks = 0,
    seekClicks = 0,
    showNoticeClicks = 0,
    hideNoticeClicks = 0,
    speedClicks = 0,
    volumeSetClicks = 0,
    screenshotClicks = 0,
    contextmenuShowClicks = 0,
    contextmenuHideClicks = 0,
    fullScreenClicks = 0,
    cancelFullScreenClicks = 0,
    sendDanmakuCallback = { sendDanmakuClicks: 0 },
    drawDanmakuClicks = 0,
    opacityDanmakuCallback = { opacityDanmakuClicks: 0 },
    clearDanmakuClicks = 0,
    showDanmakuClicks = 0,
    hideDanmakuClicks = 0,
    subtitleShowClicks = 0,
    subtitleHideClicks = 0,
    subtitleChangeClicks = 0,
    destroyClicks = 0,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyDPlayer {
                ...{
                    live,
                    autoplay,
                    theme,
                    loop,
                    lang,
                    screenshot,
                    hotkey,
                    airplay,
                    chromecast,
                    preload,
                    volume,
                    playbackSpeed,
                    preventClickToggle,
                    video,
                    subtitle,
                    danmaku,
                    contextmenu,
                    highlight,
                    mutex,
                    play,
                    pause,
                    seek,
                    notice,
                    speed,
                    volumeSet,
                    fullScreen,
                    switchQuality,
                    switchVideo,
                    sendDanmaku,
                    drawDanmaku,
                    opacityDanmaku,
                    clearDanmaku,
                    hideDanmaku,
                    showDanmaku,
                    destroy,
                    playClicks,
                    pauseClicks,
                    seekClicks,
                    showNoticeClicks,
                    hideNoticeClicks,
                    speedClicks,
                    volumeSetClicks,
                    screenshotClicks,
                    contextmenuShowClicks,
                    contextmenuHideClicks,
                    fullScreenClicks,
                    cancelFullScreenClicks,
                    sendDanmakuCallback,
                    drawDanmakuClicks,
                    opacityDanmakuCallback,
                    clearDanmakuClicks,
                    showDanmakuClicks,
                    hideDanmakuClicks,
                    subtitleShowClicks,
                    subtitleHideClicks,
                    subtitleChangeClicks,
                    destroyClicks,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyDPlayer.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 是否开启开启直播模式
     * 默认值：`false`
     */
    live: PropTypes.bool,

    /**
     * 视频是否自动播放
     * 默认值：`false`
     */
    autoplay: PropTypes.bool,

    /**
     * 设置主题色
     * 默认值：`'#b7daff'`
     */
    theme: PropTypes.string,

    /**
     * 视频是否循环播放
     * 默认值：`false`
     */
    loop: PropTypes.bool,

    /**
     * 设置语言，可选值: `'en'`、`'zh-cn'`、`'zh-tw'`
     * 默认值：`'zh-cn'`
     */
    lang: PropTypes.oneOf(['en', 'zh-cn', 'zh-tw']),

    /**
     * 是否开启截图，如果开启，视频和视频封面需要允许跨域
     * 默认值：`false`
     */
    screenshot: PropTypes.bool,

    /**
     * 在`Safari`中是否开启`AirPlay`
     * 默认值：`false`
     */
    airplay: PropTypes.bool,

    /**
     * 是否开启热键，支持快进、快退、音量控制、播放暂停
     * 默认值：`true`
     */
    hotkey: PropTypes.bool,

    /**
     * 是否启用`Chromecast`
     * 默认值：`false`
     */
    chromecast: PropTypes.bool,

    /**
     * 设置音频预加载，可选值: `'none'`、`'metadata'`、`'auto'`
     * 默认值：`'auto'`
     */
    preload: PropTypes.oneOf(['none', 'metadata', 'auto']),

    /**
     * 默认音量，请注意播放器会记忆用户设置，用户手动设置音量后默认音量即失效
     */
    volume: PropTypes.number,

    /**
     * 可选的播放速率，可以设置成自定义的数组
     */
    playbackSpeed: PropTypes.arrayOf(PropTypes.number),

    /**
     * 在左上角展示一个`logo`，你可以通过`CSS`调整它的大小和位置
     */
    logo: PropTypes.string,

    /**
     * 是否阻止点击播放器时候自动切换播放/暂停
     * 默认值：`false`
     */
    preventClickToggle: PropTypes.bool,

    /**
     * 设置视频信息
     */
    video: PropTypes.shape({
        /**
         * 设置清晰度切换
         */
        quality: PropTypes.arrayOf(PropTypes.exact({
            /**
             * 设置清晰度名称
             */
            name: PropTypes.string,
            /**
             * 设置视频链接
             */
            url: PropTypes.string,
            /**
             * 设置视频类型，可选的有`'auto'`、`'hls'`、`'flv'`、`'dash'`、`'normal'`
             * 默认值：`'auto'`
             */
            type: PropTypes.oneOf(['auto', 'hls', 'flv', 'dash', 'normal'])
        })),
        /**
         * 设置默认清晰度
         */
        defaultQuality: PropTypes.number,
        /**
         * 设置视频链接
         */
        url: PropTypes.string,
        /**
         * 设置视频封面
         */
        pic: PropTypes.string,
        /**
         * 设置视频缩略图
         */
        thumbnails: PropTypes.string,
        /**
         * 设置视频类型，可选的有`'auto'`、`'hls'`、`'flv'`、`'dash'`、`'normal'`
         * 默认值：`'auto'`
         */
        type: PropTypes.oneOf(['auto', 'hls', 'flv', 'dash', 'normal']),
    }),

    /**
     * 设置外挂字幕
     */
    subtitle: PropTypes.exact({
        /**
         * 是否开启外挂字幕
         * 默认值：`false`
         */
        isOpen: PropTypes.bool,
        /**
         * 设置字幕链接
         */
        url: PropTypes.string,
        /**
         * 设置字幕类型，可选的有`'webvtt'`、`'ass'`，目前只支持`'webvtt'`
         * 默认值：`'webvtt'`
         */
        type: PropTypes.oneOf(['webvtt', 'ass']),
        /**
         * 设置字幕字号
         */
        fontSize: PropTypes.string,
        /**
         * 设置字幕距离播放器底部的距离，取值形如: `'10px'`、`'10%'`
         */
        bottom: PropTypes.string,
        /**
         * 设置字幕颜色
         */
        color: PropTypes.string
    }),

    /**
     * 设置弹幕
     */
    danmaku: PropTypes.exact({
        /**
         * 是否开启弹幕
         * 默认值：`false`
         */
        isOpen: PropTypes.bool,
        /**
         * 设置弹幕弹幕池`id`，必须唯一，设置弹幕时必选
         */
        id: PropTypes.string,
        /**
         * 设置弹幕接口，设置弹幕时必选
         */
        api: PropTypes.string,
        /**
         * 设置弹幕后端验证`token`
         */
        token: PropTypes.string,
        /**
         * 设置弹幕最大数量
         */
        maximum: PropTypes.number,
        /**
         * 设置额外外挂弹幕
         */
        addition: PropTypes.arrayOf(PropTypes.string),
        /**
         * 设置弹幕用户名
         */
        user: PropTypes.string,
        /**
         * 设置弹幕距离播放器底部的距离，防止遮挡字幕，取值形如: `'10px'`、`'10%'`
         */
        bottom: PropTypes.string,
        /**
         * 设置海量弹幕模式，即使重叠也展示全部弹幕，请注意播放器会记忆用户设置，用户手动设置后即失效
         * 默认值：`false`
         */
        unlimited: PropTypes.bool,
        /**
         * 设置弹幕速度倍率，越大速度越快
         * 默认值：`1`
         */
        speedRate: PropTypes.number
    }),

    /**
     * 自定义右键菜单
     */
    contextmenu: PropTypes.arrayOf(PropTypes.exact({
        /**
         * 菜单名称
         */
        text: PropTypes.string,
        /**
         * 菜单额外携带的信息
         */
        extraInfo: PropTypes.object
    })),

    /**
     * 自定义进度条提示点
     */
    highlight: PropTypes.arrayOf(PropTypes.exact({
        /**
         * 进度条提示点的时间点
         */
        time: PropTypes.number,
        /**
         * 进度条提示点的文字
         */
        text: PropTypes.string
    })),

    /**
     * 是否互斥，阻止多个播放器同时播放，当前播放器播放时暂停其他播放器
     * 默认值：`true`
     */
    mutex: PropTypes.bool,

    /**
     * 播放视频，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    play: PropTypes.bool,

    /**
     * 暂停视频，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    pause: PropTypes.bool,

    /**
     * 跳转到特定时间，时间的单位为秒，每次`isSeek`设置为`true`后执行完相应操作后会自动置为`false`
     */
    seek: PropTypes.exact({
        /**
         * 跳转到特定时间
         */
        isSeek: PropTypes.bool,
        /**
         * 跳转到的时间
         */
        time: PropTypes.number,
    }),

    /**
     * 显示通知信息，每次`isShow`设置为`true`后执行完相应操作后会自动置为`false`
     */
    notice: PropTypes.exact({
        /**
         * 是否显示通知信息
         */
        isShow: PropTypes.bool,
        /**
         * 通知内容
         */
        text: PropTypes.string,
        /**
         * 通知持续时间，单位为毫秒，设置时间为`0`可以取消通知自动隐藏
         */
        time: PropTypes.number,
        /**
         * 通知透明度
         */
        opacity: PropTypes.number,
    }),

    /**
     * 设置视频速度，每次`isSpeed`设置为`true`后执行完相应操作后会自动置为`false`
     */
    speed: PropTypes.exact({
        /**
         * 是否设置视频速度
         */
        isSpeed: PropTypes.bool,
        /**
         * 视频速度
         */
        rate: PropTypes.number,
    }),

    /**
     * 设置音量，每次`isVolume`设置为`true`后执行完相应操作后会自动置为`false`
     */
    volumeSet: PropTypes.exact({
        /**
         * 是否设置音量
         */
        isVolume: PropTypes.bool,
        /**
         * 音量，取值范围为`0-1`
         */
        percentage: PropTypes.number,
        /**
         * 是否不缓存
         */
        nostorage: PropTypes.bool,
        /**
         * 是否不显示通知
         */
        nonotice: PropTypes.bool
    }),

    /**
     * 设置全屏，每次`isFullScreen`设置为`true`后执行完相应操作后会自动置为`false`
     */
    fullScreen: PropTypes.exact({
        /**
         * 是否设置全屏
         */
        isFullScreen: PropTypes.bool,
        /**
         * 全屏的类型，可选的有`'web'`、`'browser'`
         * 默认值：`'browser'`
         */
        type: PropTypes.oneOf(['web', 'browser']),
        /**
         * 全屏操作类型，可选的有`'request'`、`'cancel'`
         */
        operate: PropTypes.oneOf(['request', 'cancel'])
    }),

    /**
     * 切换清晰度，每次`isSwitch`设置为`true`后执行完相应操作后会自动置为`false`
     */
    switchQuality: PropTypes.exact({
        /**
         * 是否切换清晰度
         */
        isSwitch: PropTypes.bool,
        /**
         * 切换的清晰度`index`
         */
        index: PropTypes.number
    }),

    /**
     * 切换视频，每次`isSwitch`设置为`true`后执行完相应操作后会自动置为`false`
     */
    switchVideo: PropTypes.exact({
        /**
         * 是否切换视频
         */
        isSwitch: PropTypes.bool,
        /**
         * 切换的视频信息
         */
        video: PropTypes.shape({
            /**
             * 设置清晰度切换
             */
            quality: PropTypes.arrayOf(PropTypes.exact({
                /**
                 * 设置清晰度名称
                 */
                name: PropTypes.string,
                /**
                 * 设置视频链接
                 */
                url: PropTypes.string,
                /**
                 * 设置视频类型，可选的有`'auto'`、`'hls'`、`'flv'`、`'dash'`、`'normal'`
                 * 默认值：`'auto'`
                 */
                type: PropTypes.oneOf(['auto', 'hls', 'flv', 'dash', 'normal'])
            })),
            /**
             * 设置默认清晰度
             */
            defaultQuality: PropTypes.number,
            /**
             * 设置视频链接
             */
            url: PropTypes.string,
            /**
             * 设置视频封面
             */
            pic: PropTypes.string,
            /**
             * 设置视频缩略图
             */
            thumbnails: PropTypes.string,
            /**
             * 设置视频类型，可选的有`'auto'`、`'hls'`、`'flv'`、`'dash'`、`'normal'`
             * 默认值：`'auto'`
             */
            type: PropTypes.oneOf(['auto', 'hls', 'flv', 'dash', 'normal']),
        }),
        /**
         * 切换的视频弹幕信息
         */
        danmaku: PropTypes.exact({
            /**
             * 是否开启弹幕
             * 默认值：`false`
             */
            isOpen: PropTypes.bool,
            /**
             * 设置弹幕弹幕池`id`，必须唯一，设置弹幕时必选
             */
            id: PropTypes.string,
            /**
             * 设置弹幕接口，设置弹幕时必选
             */
            api: PropTypes.string,
            /**
             * 设置弹幕后端验证`token`
             */
            token: PropTypes.string,
            /**
             * 设置弹幕最大数量
             */
            maximum: PropTypes.number,
            /**
             * 设置额外外挂弹幕
             */
            addition: PropTypes.arrayOf(PropTypes.string),
            /**
             * 设置弹幕用户名
             */
            user: PropTypes.string,
            /**
             * 设置弹幕距离播放器底部的距离，防止遮挡字幕，取值形如: `'10px'`、`'10%'`
             */
            bottom: PropTypes.string,
            /**
             * 设置海量弹幕模式，即使重叠也展示全部弹幕，请注意播放器会记忆用户设置，用户手动设置后即失效
             * 默认值：`false`
             */
            unlimited: PropTypes.bool,
            /**
             * 设置弹幕速度倍率，越大速度越快
             * 默认值：`1`
             */
            speedRate: PropTypes.number
        })
    }),

    /**
     * 发送弹幕，每次`isSend`设置为`true`后执行完相应操作后会自动置为`false`
     */
    sendDanmaku: PropTypes.exact({
        /**
         * 是否发送弹幕
         */
        isSend: PropTypes.bool,
        /**
         * 发送的弹幕内容
         */
        content: PropTypes.exact({
            /**
             * 弹幕内容
             */
            text: PropTypes.string,
            /**
             * 弹幕颜色
             */
            color: PropTypes.string,
            /**
             * 弹幕位置
             */
            type: PropTypes.oneOf(['top', 'bottom', 'right']),
        }),
    }),

    /**
     * 绘制弹幕，每次`isDraw`设置为`true`后执行完相应操作后会自动置为`false`
     */
    drawDanmaku: PropTypes.exact({
        /**
         * 是否绘制弹幕
         */
        isDraw: PropTypes.bool,
        /**
         * 绘制的弹幕内容
         */
        content: PropTypes.exact({
            /**
             * 弹幕内容
             */
            text: PropTypes.string,
            /**
             * 弹幕颜色
             */
            color: PropTypes.string,
            /**
             * 弹幕位置
             */
            type: PropTypes.oneOf(['top', 'bottom', 'right']),
        }),
    }),

    /**
     * 设置弹幕透明度，每次`isOpacity`设置为`true`后执行完相应操作后会自动置为`false`
     */
    opacityDanmaku: PropTypes.exact({
        /**
         * 是否设置弹幕透明度
         */
        isOpacity: PropTypes.bool,
        /**
         * 弹幕透明度，取值范围为`0-1`
         */
        opacity: PropTypes.number,
    }),

    /**
     * 清空弹幕，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    clearDanmaku: PropTypes.bool,

    /**
     * 隐藏弹幕，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    hideDanmaku: PropTypes.bool,

    /**
     * 显示弹幕，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    showDanmaku: PropTypes.bool,

    /**
     * 销毁播放器，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    destroy: PropTypes.bool,

    /**
     * 监听参数，播放视频的次数
     */
    playClicks: PropTypes.number,

    /**
     * 监听参数，暂停视频的次数
     */
    pauseClicks: PropTypes.number,

    /**
     * 监听参数，跳转到特定时间的次数
     */
    seekClicks: PropTypes.number,

    /**
     * 监听参数，显示通知的次数
     */
    showNoticeClicks: PropTypes.number,

    /**
     * 监听参数，隐藏通知的次数
     */
    hideNoticeClicks: PropTypes.number,

    /**
     * 监听参数，设置视频速度的次数
     */
    speedClicks: PropTypes.number,

    /**
     * 监听参数，设置音量的次数
     */
    volumeSetClicks: PropTypes.number,

    /**
     * 监听参数，进入网页全屏的次数
     */
    fullScreenClicks: PropTypes.number,

    /**
     * 监听参数，退出网页全屏的次数
     */
    cancelFullScreenClicks: PropTypes.number,

    /**
     * 监听参数，发送弹幕的次数和信息
     */
    sendDanmakuCallback: PropTypes.exact({
        /**
         * 发送弹幕的次数
         */
        sendDanmakuClicks: PropTypes.number,
        /**
         * 发送的弹幕信息
         */
        sendInfo: PropTypes.object,
    }),

    /**
     * 监听参数，通过函数绘制弹幕的次数
     */
    drawDanmakuClicks: PropTypes.number,

    /**
     * 监听参数，清空弹幕的次数
     */
    clearDanmakuClicks: PropTypes.number,

    /**
     * 监听参数，设置弹幕透明度的次数和透明度
     */
    opacityDanmakuCallback: PropTypes.exact({
        /**
         * 设置弹幕透明度的次数
         */
        opacityDanmakuClicks: PropTypes.number,
        /**
         * 弹幕透明度，取值范围为0-1
         */
        opacity: PropTypes.number,
    }),

    /**
     * 监听参数，显示弹幕的次数
     */
    showDanmakuClicks: PropTypes.number,

    /**
     * 监听参数，隐藏弹幕的次数
     */
    hideDanmakuClicks: PropTypes.number,

    /**
     * 监听参数，显示字幕的次数
     */
    subtitleShowClicks: PropTypes.number,

    /**
     * 监听参数，隐藏字幕的次数
     */
    subtitleHideClicks: PropTypes.number,

    /**
     * 监听参数，切换字幕的次数
     */
    subtitleChangeClicks: PropTypes.number,

    /**
     * 监听参数，截图的次数
     */
    screenshotClicks: PropTypes.number,

    /**
     * 监听参数，右键菜单显示的次数
     */
    contextmenuShowClicks: PropTypes.number,

    /**
     * 监听参数，右键菜单隐藏的次数
     */
    contextmenuHideClicks: PropTypes.number,

    /**
     * 监听参数，当前点击的右键菜单信息
     */
    currentClickContextmenu: PropTypes.object,

    /**
     * 监听参数，播放器销毁的次数
     */
    destroyClicks: PropTypes.number,

    /**
     * 监听参数，当前通知信息
     */
    currentNoticeInfo: PropTypes.object,

    /**
     * 监听参数，当前视频的信息
     */
    currentVideoInfo: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyDPlayer;

export const propTypes = FefferyDPlayer.propTypes;
export const defaultProps = FefferyDPlayer.defaultProps;