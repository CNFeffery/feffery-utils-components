import React, { useMemo, useEffect, useRef } from 'react';
import DPlayer from "react-dplayer";
import Hls from 'hls.js';
import flvjs from 'flv.js';
import dashjs from 'dashjs';
import { v4 as uuidv4 } from 'uuid';
import { isString } from 'lodash';
import useCss from '../../hooks/useCss';
import { propTypes, defaultProps } from '../../components/player/FefferyDPlayer.react';

/**
 * 视频播放组件FefferyDPlayer
 */
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
                currentSrc: dplayer.current.dp.video.currentSrc
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

        // 将默认的右键菜单项dom文本包含'关于作者'和'DPlayer'的显示样式设置为 none
        allMenuItems.slice(-2).forEach(item => {
            item.style.display = 'none';
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

export default FefferyDPlayer;

FefferyDPlayer.defaultProps = defaultProps;
FefferyDPlayer.propTypes = propTypes;