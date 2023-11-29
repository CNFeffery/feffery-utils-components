import React, { useMemo, useEffect } from 'react';
import DPlayer from "react-dplayer";
import Hls from 'hls.js';
import { v4 as uuidv4 } from 'uuid';
import { isString } from 'lodash';
import useCss from '../../hooks/useCss';
import PropTypes from 'prop-types';

// 定义音乐播放组件FefferyDPlayer
const FefferyDPlayer = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        live,
        autoplay,
        theme,
        loop,
        lang,
        screenshot,
        airplay,
        hotkey,
        chromecast,
        preload,
        volume,
        playbackSpeed,
        logo,
        video,
        subtitle,
        danmaku,
        contextmenu,
        highlight,
        mutex,
        setProps,
        loading_state
    } = props;

    const containerId = uuidv4();

    useEffect(() => {
        // 获取所有右键菜单项
        let allMenuItems = Array.from(document.querySelectorAll('.dplayer-menu-item'));

        // 选择最后两个菜单项
        let lastTwoMenuItems = allMenuItems.slice(-2);

        // 将它们的显示样式设置为 none
        lastTwoMenuItems.forEach(item => {
            item.style.display = 'none';
        })
    })

    const options = useMemo(() => {
        let subtitleOptions = subtitle.isOpen ? { subtitle: subtitle } : {};
        let danmakuOptions = danmaku.isOpen ? { danmaku: danmaku } : {};
        if (video.type == 'hls') {
            video.customType = {
                hls: function (video, player) {
                    if (Hls.isSupported()) {
                        const hls = new Hls();
                        hls.loadSource(video.src);
                        hls.attachMedia(video);
                    } else {
                        player.notice('Error: HLS is not supported.');
                    }
                }
            }
        }
        return {
            ...subtitleOptions,
            ...danmakuOptions,
            container: containerId,
            live: live,
            autoplay: autoplay,
            theme: theme,
            loop: loop,
            lang: lang,
            screenshot: screenshot,
            airplay: airplay,
            hotkey: hotkey,
            chromecast: chromecast,
            preload: preload,
            volume: volume,
            playbackSpeed: playbackSpeed,
            logo: logo,
            video: video,
            contextmenu: contextmenu,
            highlight: highlight,
            mutex: mutex
        }
    }, [live, autoplay, theme, loop, lang, screenshot, airplay, hotkey, chromecast, preload, volume, playbackSpeed, logo, video, subtitle, danmaku, contextmenu, highlight, mutex])

    return (
        <div id={containerId}>
            <DPlayer
                id={id}
                className={
                    isString(className) ?
                        className :
                        (className ? useCss(className) : undefined)
                }
                style={style}
                options={options}
                loading_state={loading_state}
            />
        </div>
    )
}

// 定义参数或属性，API参数参考https://dplayer.diygod.dev/zh/guide.html#参数
FefferyDPlayer.propTypes = {
    // 播放器id
    id: PropTypes.string,

    // 设置播放器的css类名
    className: PropTypes.string,

    // 设置播放器的样式
    style: PropTypes.object,

    // 是否开启开启直播模式，默认为false
    live: PropTypes.bool,

    // 视频是否自动播放，默认为false
    autoplay: PropTypes.bool,

    // 设置主题色，默认为'#b7daff'
    theme: PropTypes.string,

    // 视频是否循环播放, 默认为false
    loop: PropTypes.bool,

    // 设置语言， 可选值: 'en', 'zh-cn', 'zh-tw'，默认为'zh-cn'
    lang: PropTypes.oneOf(['en', 'zh-cn', 'zh-tw']),

    // 是否开启截图，如果开启，视频和视频封面需要允许跨域， 默认为false
    screenshot: PropTypes.bool,

    // 在 Safari 中是否开启 AirPlay，默认false
    airplay: PropTypes.bool,

    // 是否开启热键，支持快进、快退、音量控制、播放暂停， 默认为true
    hotkey: PropTypes.bool,

    // 是否启用Chromecast，默认false
    chromecast: PropTypes.bool,

    // 设置音频预加载，可选值: 'none', 'metadata', 'auto'，默认为'auto'
    preload: PropTypes.oneOf(['none', 'metadata', 'auto']),

    // 默认音量，请注意播放器会记忆用户设置，用户手动设置音量后默认音量即失效
    volume: PropTypes.number,

    // 可选的播放速率，可以设置成自定义的数组
    playbackSpeed: PropTypes.arrayOf(PropTypes.number),

    // 在左上角展示一个 logo，你可以通过 CSS 调整它的大小和位置
    logo: PropTypes.string,

    // 设置视频信息
    video: PropTypes.exact({
        // 设置清晰度切换
        quality: PropTypes.arrayOf(PropTypes.exact({
            // 设置清晰度名称
            name: PropTypes.string,
            // 设置视频链接
            url: PropTypes.string,
            // 设置视频类型，可选的有'auto'、'hls'、'normal'，默认为'auto'
            type: PropTypes.oneOf(['auto', 'hls', 'normal'])
        })),
        // 设置默认清晰度
        defaultQuality: PropTypes.number,
        // 设置视频链接
        url: PropTypes.string,
        // 设置视频封面
        pic: PropTypes.string,
        // 设置视频缩略图
        thumbnails: PropTypes.string,
        // 设置视频类型，可选的有'auto'、'hls'、'normal'，默认为'auto'
        type: PropTypes.oneOf(['auto', 'hls', 'normal'])
    }),

    // 设置外挂字幕
    subtitle: PropTypes.exact({
        // 是否开启外挂字幕，默认为false
        isOpen: PropTypes.bool,
        // 设置字幕链接
        url: PropTypes.string,
        // 设置字幕类型，可选的有'webvtt'、'ass'，默认为'webvtt'，目前只支持 webvtt
        type: PropTypes.oneOf(['webvtt', 'ass']),
        // 设置字幕字号
        fontSize: PropTypes.string,
        // 设置字幕距离播放器底部的距离，取值形如: '10px' '10%'
        bottom: PropTypes.string,
        // 设置字幕颜色
        color: PropTypes.string
    }),

    // 设置弹幕
    danmaku: PropTypes.exact({
        // 是否开启弹幕，默认为false
        isOpen: PropTypes.bool,
        // 设置弹幕弹幕池id，必须唯一，设置弹幕时必选
        id: PropTypes.string,
        // 设置弹幕接口，设置弹幕时必选
        api: PropTypes.string,
        // 设置弹幕后端验证token
        token: PropTypes.string,
        // 设置弹幕最大数量
        maximum: PropTypes.number,
        // 设置额外外挂弹幕
        addition: PropTypes.arrayOf(PropTypes.string),
        // 设置弹幕用户名
        user: PropTypes.string,
        // 设置弹幕距离播放器底部的距离，防止遮挡字幕，取值形如: '10px' '10%'
        bottom: PropTypes.string,
        // 设置海量弹幕模式，即使重叠也展示全部弹幕，请注意播放器会记忆用户设置，用户手动设置后即失效，默认为false
        unlimited: PropTypes.bool,
        // 设置弹幕速度倍率，越大速度越快，默认为1
        speedRate: PropTypes.number
    }),

    // 自定义右键菜单
    contextmenu: PropTypes.array,

    // 自定义进度条提示点
    highlight: PropTypes.array,

    // 是否互斥，阻止多个播放器同时播放，当前播放器播放时暂停其他播放器，默认为true
    mutex: PropTypes.bool,

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyDPlayer.defaultProps = {
    live: false,
    autoplay: false,
    theme: '#b7daff',
    loop: false,
    lang: 'zh-cn',
    screenshot: false,
    hotkey: true,
    airplay: false,
    chromecast: false,
    preload: 'auto',
    volume: 0.7,
    playbackSpeed: [0.5, 0.75, 1, 1.25, 1.5, 2],
    video: {
        type: 'auto'
    },
    subtitle: {
        isOpen: false,
        type: 'webvtt',
        fontSize: '20px',
        bottom: '40px',
        color: '#fff'
    },
    danmaku: {
        isOpen: false,
        unlimited: false,
        speedRate: 1
    },
    contextmenu: [],
    highlight: [],
    mutex: true
}

export default FefferyDPlayer;