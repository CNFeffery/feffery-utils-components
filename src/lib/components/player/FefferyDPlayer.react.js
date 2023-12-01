import React, { useMemo, useEffect, useRef } from 'react';
import DPlayer from "react-dplayer";
import Hls from 'hls.js';
import flvjs from 'flv.js';
import dashjs from 'dashjs';
import { v4 as uuidv4 } from 'uuid';
import { isString } from 'lodash';
import useCss from '../../hooks/useCss';
import PropTypes from 'prop-types';

// 定义视频播放组件FefferyDPlayer
const FefferyDPlayer = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        key,
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
        currentClickContextmenu,
        fullScreenClicks,
        cancelFullScreenClicks,
        sendDanmakuCallback,
        drawDanmakuClicks,
        opacityDanmakuCallback,
        clearDanmakuClicks,
        hideDanmakuClicks,
        showDanmakuClicks,
        subtitleShowClicks,
        subtitleHideClicks,
        subtitleChangeClicks,
        destroyClicks,
        currentNoticeInfo,
        currentVideoInfo,
        setProps,
        loading_state
    } = props;

    const containerId = uuidv4();

    const dplayer = useRef(null);

    const onPlay = () => {
        setProps({ playClicks: playClicks + 1 })
        setProps({
            currentVideoInfo: {
                currentTime: dplayer.current.dp.video.currentTime,
                duration: dplayer.current.dp.video.duration,
                paused: dplayer.current.dp.video.paused,
                volume: dplayer.current.dp.video.volume,
                src: dplayer.current.dp.video.src,
                url: dplayer.current.dp.video.currentSrc
            }
        })
    };

    const onPause = () => {
        setProps({ pauseClicks: pauseClicks + 1 })
        setProps({
            currentVideoInfo: {
                currentTime: dplayer.current.dp.video.currentTime,
                duration: dplayer.current.dp.video.duration,
                paused: dplayer.current.dp.video.paused,
                volume: dplayer.current.dp.video.volume,
                src: dplayer.current.dp.video.src,
                url: dplayer.current.dp.video.currentSrc
            }
        })
    };

    const onSeeked = () => {
        setProps({ seekClicks: seekClicks + 1 })
        setProps({
            currentVideoInfo: {
                currentTime: dplayer.current.dp.video.currentTime,
                duration: dplayer.current.dp.video.duration,
                paused: dplayer.current.dp.video.paused,
                volume: dplayer.current.dp.video.volume,
                src: dplayer.current.dp.video.src,
                url: dplayer.current.dp.video.currentSrc
            }
        })
    };

    const onNoticeShow = (e) => {
        setProps({ currentNoticeInfo: { text: e.innerText, opacity: parseFloat(e.style.opacity) } });
        setProps({ showNoticeClicks: showNoticeClicks + 1 })
    };

    const onNoticeHide = () => {
        setProps({ hideNoticeClicks: hideNoticeClicks + 1 })
    };

    const onRatechange = () => {
        setProps({ speedClicks: speedClicks + 1 })
    };

    const onVolumechange = () => {
        setProps({ volumeSetClicks: volumeSetClicks + 1 })
        setProps({
            currentVideoInfo: {
                currentTime: dplayer.current.dp.video.currentTime,
                duration: dplayer.current.dp.video.duration,
                paused: dplayer.current.dp.video.paused,
                volume: dplayer.current.dp.video.volume,
                src: dplayer.current.dp.video.src,
                url: dplayer.current.dp.video.currentSrc
            }
        })
        setProps({ volume: dplayer.current.dp.video.volume })
    };

    const onScreenshot = () => {
        setProps({ screenshotClicks: screenshotClicks + 1 })
    };

    const onContextmenuShow = () => {
        setProps({ contextmenuShowClicks: contextmenuShowClicks + 1 })
    };

    const onContextmenuHide = () => {
        setProps({ contextmenuHideClicks: contextmenuHideClicks + 1 })
    };

    const onFullscreen = () => {
        setProps({ fullScreenClicks: fullScreenClicks + 1 })
    };

    const onFullscreenCancel = () => {
        setProps({ cancelFullScreenClicks: cancelFullScreenClicks + 1 })
    };

    const onDanmakuSend = (e) => {
        setProps({ sendDanmakuCallback: { sendDanmakuClicks: sendDanmakuCallback.sendDanmakuClicks + 1, sendInfo: e } })
    };

    const onDanmakuOpacity = (e) => {
        setProps({ opacityDanmakuCallback: { opacityDanmakuClicks: opacityDanmakuCallback.opacityDanmakuClicks + 1, opacity: e } })
    };

    const onDanmakuClear = () => {
        setProps({ clearDanmakuClicks: clearDanmakuClicks + 1 })
    };

    const onDanmakuHide = () => {
        setProps({ hideDanmakuClicks: hideDanmakuClicks + 1 })
    };

    const onDanmakuShow = () => {
        setProps({ showDanmakuClicks: showDanmakuClicks + 1 })
    };

    const onSubtitleShow = () => {
        setProps({ subtitleShowClicks: subtitleShowClicks + 1 })
    };

    const onSubtitleHide = () => {
        setProps({ subtitleHideClicks: subtitleHideClicks + 1 })
    };

    const onSubtitleChange = () => {
        setProps({ subtitleChangeClicks: subtitleChangeClicks + 1 })
    };

    const onDestroy = () => {
        setProps({ destroyClicks: destroyClicks + 1 })
    };

    useEffect(() => {
        if (play) {
            dplayer.current.dp.play();
            setProps({ play: false });
        }
    }, [play])

    useEffect(() => {
        if (pause) {
            dplayer.current.dp.pause();
            setProps({ pause: false });
        }
    }, [pause])

    useEffect(() => {
        if (seek.isSeek && seek.time) {
            dplayer.current.dp.seek(seek.time);
            setProps({ seek: { isSeek: false, time: undefined } });
        }
    }, [seek])

    useEffect(() => {
        if (notice.isShow && notice.text) {
            dplayer.current.dp.notice(notice.text, notice.time, notice.opacity);
            setProps({ notice: { isShow: false, text: undefined, time: 2000, opacity: 0.8 } });
        }
    }, [notice])

    useEffect(() => {
        if (speed.isSpeed && speed.rate) {
            dplayer.current.dp.speed(speed.rate);
            setProps({ speed: { isSpeed: false, rate: undefined } });
        }
    }, [speed])

    useEffect(() => {
        if (volumeSet.isVolumeSet && volumeSet.percentage) {
            dplayer.current.dp.volume(volumeSet.percentage, volumeSet.nostorage, volumeSet.nonotice);
            setProps({ volumeSet: { isVolumeSet: false, percentage: undefined, nostorage: true, nonotice: false } });
        }
    }, [volumeSet])

    useEffect(() => {
        if (fullScreen.isFullScreen && fullScreen.type && fullScreen.operate) {
            switch (fullScreen.operate) {
                case 'request':
                    dplayer.current.dp.fullScreen.request(fullScreen.type);
                    break;
                case 'cancel':
                    dplayer.current.dp.fullScreen.cancel(fullScreen.type);
                    break;
                default:
                    break;
            }
            setProps({ fullScreen: { isFullScreen: false, type: 'browser', operate: undefined } });
        }
    }, [fullScreen])

    useEffect(() => {
        if (switchQuality.isSwitch && switchQuality.index) {
            dplayer.current.dp.switchQuality(switchQuality.index);
            setProps({ switchQuality: { isSwitch: false, index: undefined } });
        }
    }, [switchQuality])

    useEffect(() => {
        if (switchVideo.isSwitch && switchVideo.video) {
            dplayer.current.dp.switchVideo(switchVideo.video, switchVideo.danmaku);
            setProps({ switchVideo: { isSwitch: false, video: undefined, danmaku: undefined } });
        }
    }, [switchVideo])

    useEffect(() => {
        if (sendDanmaku.isSend && sendDanmaku.content) {
            dplayer.current.dp.danmaku.send(sendDanmaku.content, function () { console.log('发送成功') });
            setProps({ sendDanmaku: { isSend: false, content: undefined } });
        }
    }, [sendDanmaku])

    useEffect(() => {
        if (drawDanmaku.isDraw && drawDanmaku.content) {
            dplayer.current.dp.danmaku.draw(drawDanmaku.content);
            setProps({ drawDanmakuClicks: drawDanmakuClicks + 1 })
            setProps({ drawDanmaku: { isDraw: false, content: undefined } });
        }
    }, [drawDanmaku])

    useEffect(() => {
        if (opacityDanmaku.isOpacity && opacityDanmaku.opacity) {
            dplayer.current.dp.danmaku.opacity(opacityDanmaku.opacity);
            setProps({ opacityDanmaku: { isOpacity: false, opacity: undefined } });
        }
    }, [opacityDanmaku])

    useEffect(() => {
        if (clearDanmaku.isClear) {
            dplayer.current.dp.danmaku.clear();
            setProps({ clearDanmaku: { isClear: false } });
        }
    }, [clearDanmaku])

    useEffect(() => {
        if (hideDanmaku.isHide) {
            dplayer.current.dp.danmaku.hide();
            setProps({ hideDanmaku: { isHide: false } });
        }
    }, [hideDanmaku])

    useEffect(() => {
        if (showDanmaku.isShow) {
            dplayer.current.dp.danmaku.show();
            setProps({ showDanmaku: { isShow: false } });
        }
    }, [showDanmaku])

    useEffect(() => {
        if (destroy) {
            dplayer.current.dp.destroy();
            setProps({ destroy: false });
        }
    }, [destroy])

    useEffect(() => {
        // 获取所有右键菜单项
        let allMenuItems = Array.from(document.getElementById(containerId).querySelectorAll('.dplayer-menu-item'));

        // 将dom文本包含'关于作者'和'DPlayer'的显示样式设置为 none
        allMenuItems.forEach(item => {
            if (item.innerText.includes('关于作者') || item.innerText.includes('DPlayer')) {
                item.style.display = 'none';
            }
        })
    })

    const options = useMemo(() => {
        let subtitleOptions = subtitle.isOpen ? { subtitle: subtitle } : {};
        let danmakuOptions = danmaku.isOpen ? { danmaku: danmaku } : {};
        let contextmenuOptions = contextmenu.length > 0 ? contextmenu.map(item => { return { ...item, click: (player) => { setProps({ currentClickContextmenu: item }) } } }) : contextmenu;
        switch (video.type) {
            case 'hls':
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
                break;
            case 'flv':
                video.customType = {
                    flv: function (video, player) {
                        if (flvjs.isSupported()) {
                            const flvPlayer = flvjs.createPlayer({
                                type: 'flv',
                                url: video.src
                            });
                            flvPlayer.attachMediaElement(video);
                            flvPlayer.load();
                        } else {
                            player.notice('Error: FLV is not supported.');
                        }
                    }
                }
                break;
            case 'dash':
                video.customType = {
                    dash: function (video, player) {
                        dashjs.MediaPlayer().create().initialize(video, video.src, false);
                    }
                }
                break;
            default:
                break;
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
            preventClickToggle: preventClickToggle,
            video: video,
            contextmenu: contextmenuOptions,
            highlight: highlight,
            mutex: mutex
        }
    }, [live, autoplay, theme, loop, lang, screenshot, airplay, hotkey, chromecast, preload, volume, playbackSpeed, logo, preventClickToggle, video, subtitle, danmaku, contextmenu, highlight, mutex])

    return (
        <div id={containerId}>
            <DPlayer
                ref={dplayer}
                id={id}
                className={
                    isString(className) ?
                        className :
                        (className ? useCss(className) : undefined)
                }
                style={style}
                key={key}
                options={options}
                onPlay={onPlay}
                onPause={onPause}
                onSeeked={onSeeked}
                onNoticeShow={onNoticeShow}
                onNoticeHide={onNoticeHide}
                onRatechange={onRatechange}
                onVolumechange={onVolumechange}
                onScreenshot={onScreenshot}
                onContextmenuShow={onContextmenuShow}
                onContextmenuHide={onContextmenuHide}
                onFullscreen={onFullscreen}
                onFullscreenCancel={onFullscreenCancel}
                onDanmakuSend={onDanmakuSend}
                onDanmakuOpacity={onDanmakuOpacity}
                onDanmakuClear={onDanmakuClear}
                onDanmakuShow={onDanmakuShow}
                onDanmakuHide={onDanmakuHide}
                onSubtitleShow={onSubtitleShow}
                onSubtitleHide={onSubtitleHide}
                onSubtitleChange={onSubtitleChange}
                onDestroy={onDestroy}
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

    // 设置播放器的key，强制刷新组件
    key: PropTypes.string,

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

    // 是否阻止点击播放器时候自动切换播放/暂停，默认为false
    preventClickToggle: PropTypes.bool,

    // 设置视频信息
    video: PropTypes.exact({
        // 设置清晰度切换
        quality: PropTypes.arrayOf(PropTypes.exact({
            // 设置清晰度名称
            name: PropTypes.string,
            // 设置视频链接
            url: PropTypes.string,
            // 设置视频类型，可选的有'auto'、'hls'、'flv'、 'dash'、'normal'，默认为'auto'
            type: PropTypes.oneOf(['auto', 'hls', 'flv', 'dash', 'normal'])
        })),
        // 设置默认清晰度
        defaultQuality: PropTypes.number,
        // 设置视频链接
        url: PropTypes.string,
        // 设置视频封面
        pic: PropTypes.string,
        // 设置视频缩略图
        thumbnails: PropTypes.string,
        // 设置视频类型，可选的有'auto'、'hls'、'flv'、 'dash'、'normal'，默认为'auto'
        type: PropTypes.oneOf(['auto', 'hls', 'flv', 'dash', 'normal']),
        // 自定义视频类型，此参数无需设置，会根据设置的type参数自动接管
        customType: PropTypes.object
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
    contextmenu: PropTypes.arrayOf(PropTypes.exact({
        // 菜单key
        key: PropTypes.string,
        // 菜单名称
        text: PropTypes.string,
        // 菜单图标
        icon: PropTypes.node
    })),

    // 自定义进度条提示点
    highlight: PropTypes.arrayOf(PropTypes.exact({
        // 进度条提示点的时间点
        time: PropTypes.number,
        // 进度条提示点的文字
        text: PropTypes.string
    })),

    // 是否互斥，阻止多个播放器同时播放，当前播放器播放时暂停其他播放器，默认为true
    mutex: PropTypes.bool,

    // 播放视频，每次设置为true后执行完相应操作后会自动置为false
    play: PropTypes.bool,

    // 暂停视频，每次设置为true后执行完相应操作后会自动置为false
    pause: PropTypes.bool,

    // 跳转到特定时间，时间的单位为秒，每次isSeek设置为true后执行完相应操作后会自动置为false
    seek: PropTypes.exact({
        isSeek: PropTypes.bool,
        // 跳转到的时间
        time: PropTypes.number,
    }),

    // 显示通知信息，每次isShow设置为true后执行完相应操作后会自动置为false
    notice: PropTypes.exact({
        isShow: PropTypes.bool,
        // 通知内容
        text: PropTypes.string,
        // 通知持续时间，单位为毫秒，设置时间为 0 可以取消通知自动隐藏
        time: PropTypes.number,
        // 通知透明度
        opacity: PropTypes.number,
    }),

    // 设置视频速度，每次isSpeed设置为true后执行完相应操作后会自动置为false
    speed: PropTypes.exact({
        isSpeed: PropTypes.bool,
        // 视频速度
        rate: PropTypes.number,
    }),

    // 设置音量，每次isVolume设置为true后执行完相应操作后会自动置为false
    volumeSet: PropTypes.exact({
        isVolume: PropTypes.bool,
        // 音量，取值范围为0-1
        percentage: PropTypes.number,
        // 是否不缓存
        nostorage: PropTypes.bool,
        // 是否不显示通知
        nonotice: PropTypes.bool
    }),

    // 设置全屏，每次isFullScreen设置为true后执行完相应操作后会自动置为false
    fullScreen: PropTypes.exact({
        // 是否全屏，每次设置为true后执行完相应操作后会自动置为false
        isFullScreen: PropTypes.bool,
        // 全屏的类型，可选的有'web'、'browser'，默认为'browser'
        type: PropTypes.oneOf(['web', 'browser']),
        // 全屏操作类型，可选的有'request'、'cancel'
        operate: PropTypes.oneOf(['request', 'cancel'])
    }),

    // 切换清晰度，每次isSwitch设置为true后执行完相应操作后会自动置为false
    switchQuality: PropTypes.exact({
        isSwitch: PropTypes.bool,
        // 切换的清晰度index
        index: PropTypes.number
    }),

    // 切换视频，每次isSwitch设置为true后执行完相应操作后会自动置为false
    switchVideo: PropTypes.exact({
        isSwitch: PropTypes.bool,
        // 切换的视频信息
        video: PropTypes.exact({
            // 设置清晰度切换
            quality: PropTypes.arrayOf(PropTypes.exact({
                // 设置清晰度名称
                name: PropTypes.string,
                // 设置视频链接
                url: PropTypes.string,
                // 设置视频类型，可选的有'auto'、'hls'、'flv'、 'dash'、'normal'，默认为'auto'
                type: PropTypes.oneOf(['auto', 'hls', 'flv', 'dash', 'normal'])
            })),
            // 设置默认清晰度
            defaultQuality: PropTypes.number,
            // 设置视频链接
            url: PropTypes.string,
            // 设置视频封面
            pic: PropTypes.string,
            // 设置视频缩略图
            thumbnails: PropTypes.string,
            // 设置视频类型，可选的有'auto'、'hls'、'flv'、 'dash'、'normal'，默认为'auto'
            type: PropTypes.oneOf(['auto', 'hls', 'flv', 'dash', 'normal']),
            // 自定义视频类型，此参数无需设置，会根据设置的type参数自动接管
            customType: PropTypes.object
        }),
        // 切换的视频弹幕信息
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
    }),

    // 发送弹幕，每次isSend设置为true后执行完相应操作后会自动置为false
    sendDanmaku: PropTypes.exact({
        isSend: PropTypes.bool,
        // 发送的弹幕内容
        content: PropTypes.exact({
            // 弹幕内容
            text: PropTypes.string,
            // 弹幕颜色
            color: PropTypes.string,
            // 弹幕位置
            type: PropTypes.oneOf(['top', 'bottom', 'right']),
        }),
    }),

    // 绘制弹幕，每次isDraw设置为true后执行完相应操作后会自动置为false
    drawDanmaku: PropTypes.exact({
        isDraw: PropTypes.bool,
        // 绘制的弹幕内容
        content: PropTypes.exact({
            // 弹幕内容
            text: PropTypes.string,
            // 弹幕颜色
            color: PropTypes.string,
            // 弹幕位置
            type: PropTypes.oneOf(['top', 'bottom', 'right']),
        }),
    }),

    // 设置弹幕透明度，每次isOpacity设置为true后执行完相应操作后会自动置为false
    opacityDanmaku: PropTypes.exact({
        isOpacity: PropTypes.bool,
        // 弹幕透明度，取值范围为0-1
        opacity: PropTypes.number,
    }),

    // 清空弹幕，每次设置为true后执行完相应操作后会自动置为false
    clearDanmaku: PropTypes.bool,

    // 隐藏弹幕，每次设置为true后执行完相应操作后会自动置为false
    hideDanmaku: PropTypes.bool,

    // 显示弹幕，每次设置为true后执行完相应操作后会自动置为false
    showDanmaku: PropTypes.bool,

    // 销毁播放器，每次设置为true后执行完相应操作后会自动置为false
    destroy: PropTypes.bool,

    // 监听参数，播放视频的次数
    playClicks: PropTypes.number,

    // 监听参数，暂停视频的次数
    pauseClicks: PropTypes.number,

    // 监听参数，跳转到特定时间的次数
    seekClicks: PropTypes.number,

    // 监听参数，显示通知的次数
    showNoticeClicks: PropTypes.number,

    // 监听参数，隐藏通知的次数
    hideNoticeClicks: PropTypes.number,

    // 监听参数，设置视频速度的次数
    speedClicks: PropTypes.number,

    // 监听参数，设置音量的次数
    volumeSetClicks: PropTypes.number,

    // 监听参数，进入网页全屏的次数
    fullScreenClicks: PropTypes.number,

    // 监听参数，退出网页全屏的次数
    cancelFullScreenClicks: PropTypes.number,

    // 监听参数，发送弹幕的次数和信息
    sendDanmakuCallback: PropTypes.exact({
        sendDanmakuClicks: PropTypes.number,
        // 发送的弹幕信息
        sendInfo: PropTypes.object,
    }),

    // 监听参数，通过函数绘制弹幕的次数
    drawDanmakuClicks: PropTypes.number,

    // 监听参数，清空弹幕的次数
    clearDanmakuClicks: PropTypes.number,

    // 监听参数，设置弹幕透明度的次数和透明度
    opacityDanmakuCallback: PropTypes.exact({
        opacityDanmakuClicks: PropTypes.number,
        // 弹幕透明度，取值范围为0-1
        opacity: PropTypes.number,
    }),

    // 监听参数，显示弹幕的次数
    showDanmakuClicks: PropTypes.number,

    // 监听参数，隐藏弹幕的次数
    hideDanmakuClicks: PropTypes.number,

    // 监听参数，显示字幕的次数
    subtitleShowClicks: PropTypes.number,

    // 监听参数，隐藏字幕的次数
    subtitleHideClicks: PropTypes.number,

    // 监听参数，切换字幕的次数
    subtitleChangeClicks: PropTypes.number,

    // 监听参数，截图的次数
    screenshotClicks: PropTypes.number,

    // 监听参数，右键菜单显示的次数
    contextmenuShowClicks: PropTypes.number,

    // 监听参数，右键菜单隐藏的次数
    contextmenuHideClicks: PropTypes.number,

    // 监听参数，当前点击的右键菜单信息
    currentClickContextmenu: PropTypes.object,

    // 监听参数，播放器销毁的次数
    destroyClicks: PropTypes.number,

    // 监听参数，当前通知信息
    currentNoticeInfo: PropTypes.object,

    // 监听参数，当前视频的信息
    currentVideoInfo: PropTypes.object,

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
    preventClickToggle: false,
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
    mutex: true,
    play: false,
    pause: false,
    seek: {
        isSeek: false
    },
    notice: {
        isShow: false,
        time: 2000,
        opacity: 0.8
    },
    speed: {
        isSpeed: false
    },
    volumeSet: {
        isVolume: false,
        nostorage: true,
        nonotice: false
    },
    fullScreen: {
        isFullScreen: false,
        type: 'browser'
    },
    switchQuality: {
        isSwitch: false
    },
    switchVideo: {
        isSwitch: false
    },
    sendDanmaku: {
        isSend: false
    },
    drawDanmaku: {
        isDraw: false
    },
    opacityDanmaku: {
        isOpacity: false
    },
    clearDanmaku: false,
    hideDanmaku: false,
    showDanmaku: false,
    destroy: false,
    playClicks: 0,
    pauseClicks: 0,
    seekClicks: 0,
    showNoticeClicks: 0,
    hideNoticeClicks: 0,
    speedClicks: 0,
    volumeSetClicks: 0,
    screenshotClicks: 0,
    contextmenuShowClicks: 0,
    contextmenuHideClicks: 0,
    fullScreenClicks: 0,
    cancelFullScreenClicks: 0,
    sendDanmakuCallback: {
        sendDanmakuClicks: 0
    },
    drawDanmakuClicks: 0,
    opacityDanmakuCallback: {
        opacityDanmakuClicks: 0
    },
    clearDanmakuClicks: 0,
    showDanmakuClicks: 0,
    hideDanmakuClicks: 0,
    subtitleShowClicks: 0,
    subtitleHideClicks: 0,
    subtitleChangeClicks: 0,
    destroyClicks: 0
}

export default FefferyDPlayer;