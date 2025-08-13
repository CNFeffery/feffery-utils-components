// react核心
import React, { useMemo, useEffect, useRef } from "react";
// 组件核心
import DPlayer from "dplayer";
import Hls from "hls.js";
import flvjs from "flv.js";
import dashjs from "dashjs";
// 辅助库
import { v4 as uuidv4 } from "uuid";
import { isString } from "lodash";
import useCss from "../../hooks/useCss";
import { useLoading } from "../../components/utils";
// 参数类型
import {
  propTypes,
  defaultProps,
} from "../../components/player/FefferyDPlayer.react";

/**
 * 视频播放组件FefferyDPlayer
 */
const FefferyDPlayer = ({
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
  intervalMonitor,
  intervalMonitorDelay,
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
}) => {
  const dplayerId = id || `feffery-dplayer-${uuidv4()}`;
  const dplayer = useRef();
  const dom = useRef();
  const interval = useRef();

  const onPlay = () => {
    playClicks++;
    setProps({
      playClicks: playClicks,
      currentVideoInfo: {
        currentTime: dplayer.current.video.currentTime,
        duration: dplayer.current.video.duration,
        paused: dplayer.current.video.paused,
        volume: dplayer.current.video.volume,
        src: dplayer.current.video.src,
        url: dplayer.current.video.currentSrc,
      },
    });
  };

  const onPause = () => {
    pauseClicks++;
    setProps({
      pauseClicks: pauseClicks,
      currentVideoInfo: {
        currentTime: dplayer.current.video.currentTime,
        duration: dplayer.current.video.duration,
        paused: dplayer.current.video.paused,
        volume: dplayer.current.video.volume,
        src: dplayer.current.video.src,
        url: dplayer.current.video.currentSrc,
      },
    });
  };

  const onSeeked = () => {
    seekClicks++;
    setProps({
      seekClicks: seekClicks,
      currentVideoInfo: {
        currentTime: dplayer.current.video.currentTime,
        duration: dplayer.current.video.duration,
        paused: dplayer.current.video.paused,
        volume: dplayer.current.video.volume,
        src: dplayer.current.video.src,
        url: dplayer.current.video.currentSrc,
      },
    });
  };

  const onNoticeShow = (e) => {
    showNoticeClicks++;
    setProps({
      showNoticeClicks: showNoticeClicks,
      currentNoticeInfo: {
        text: e.innerText,
        opacity: parseFloat(e.style.opacity),
      },
    });
  };

  const onNoticeHide = () => {
    hideNoticeClicks++;
    setProps({ hideNoticeClicks: hideNoticeClicks });
  };

  const onRatechange = () => {
    speedClicks++;
    setProps({ speedClicks: speedClicks });
  };

  const onVolumechange = () => {
    volumeSetClicks++;
    setProps({
      volumeSetClicks: volumeSetClicks,
      currentVideoInfo: {
        currentTime: dplayer.current.video.currentTime,
        duration: dplayer.current.video.duration,
        paused: dplayer.current.video.paused,
        volume: dplayer.current.video.volume,
        src: dplayer.current.video.src,
        url: dplayer.current.video.currentSrc,
      },
      volume: dplayer.current.video.volume,
    });
  };

  const onScreenshot = () => {
    screenshotClicks++;
    setProps({ screenshotClicks: screenshotClicks });
  };

  const onContextmenuShow = () => {
    contextmenuShowClicks++;
    setProps({ contextmenuShowClicks: contextmenuShowClicks });
  };

  const onContextmenuHide = () => {
    contextmenuHideClicks++;
    setProps({ contextmenuHideClicks: contextmenuHideClicks });
  };

  const onFullscreen = () => {
    fullScreenClicks++;
    setProps({ fullScreenClicks: fullScreenClicks });
  };

  const onFullscreenCancel = () => {
    cancelFullScreenClicks++;
    setProps({ cancelFullScreenClicks: cancelFullScreenClicks });
  };

  const onDanmakuSend = (e) => {
    sendDanmakuCallback.sendDanmakuClicks++;
    setProps({
      sendDanmakuCallback: {
        sendDanmakuClicks: sendDanmakuCallback.sendDanmakuClicks,
        sendInfo: e,
      },
    });
  };

  const onDanmakuOpacity = (e) => {
    opacityDanmakuCallback.opacityDanmakuClicks++;
    setProps({
      opacityDanmakuCallback: {
        opacityDanmakuClicks: opacityDanmakuCallback.opacityDanmakuClicks,
        opacity: e,
      },
    });
  };

  const onDanmakuClear = () => {
    clearDanmakuClicks++;
    setProps({ clearDanmakuClicks: clearDanmakuClicks });
  };

  const onDanmakuHide = () => {
    hideDanmakuClicks++;
    setProps({ hideDanmakuClicks: hideDanmakuClicks });
  };

  const onDanmakuShow = () => {
    showDanmakuClicks++;
    setProps({ showDanmakuClicks: showDanmakuClicks });
  };

  const onSubtitleShow = () => {
    subtitleShowClicks++;
    setProps({ subtitleShowClicks: subtitleShowClicks });
  };

  const onSubtitleHide = () => {
    subtitleHideClicks++;
    setProps({ subtitleHideClicks: subtitleHideClicks });
  };

  const onSubtitleChange = () => {
    subtitleChangeClicks++;
    setProps({ subtitleChangeClicks: subtitleChangeClicks });
  };

  const onDestroy = () => {
    destroyClicks++;
    setProps({ destroyClicks: destroyClicks });
  };

  useEffect(() => {
    if (intervalMonitor) {
      interval.current = setInterval(() => {
        setProps({
          currentVideoInfo: {
            currentTime: dplayer.current.video.currentTime,
            duration: dplayer.current.video.duration,
            paused: dplayer.current.video.paused,
            volume: dplayer.current.video.volume,
            src: dplayer.current.video.src,
            url: dplayer.current.video.currentSrc,
          },
        });
      }, intervalMonitorDelay);
    } else {
      clearInterval(interval.current);
    }
  }, [intervalMonitor]);

  useEffect(() => {
    if (play) {
      dplayer.current.play();
      setProps({ play: false });
    }
  }, [play]);

  useEffect(() => {
    if (pause) {
      dplayer.current.pause();
      setProps({ pause: false });
    }
  }, [pause]);

  useEffect(() => {
    if (seek.isSeek && seek.time) {
      dplayer.current.seek(seek.time);
      setProps({ seek: { isSeek: false, time: undefined } });
    }
  }, [seek]);

  useEffect(() => {
    if (notice.isShow && notice.text) {
      dplayer.current.notice(notice.text, notice.time, notice.opacity);
      setProps({
        notice: { isShow: false, text: undefined, time: 2000, opacity: 0.8 },
      });
    }
  }, [notice]);

  useEffect(() => {
    if (speed.isSpeed && speed.rate) {
      dplayer.current.speed(speed.rate);
      setProps({ speed: { isSpeed: false, rate: undefined } });
    }
  }, [speed]);

  useEffect(() => {
    if (volumeSet.isVolumeSet && volumeSet.percentage) {
      dplayer.current.volume(
        volumeSet.percentage,
        volumeSet.nostorage,
        volumeSet.nonotice
      );
      setProps({
        volumeSet: {
          isVolumeSet: false,
          percentage: undefined,
          nostorage: true,
          nonotice: false,
        },
      });
    }
  }, [volumeSet]);

  useEffect(() => {
    if (fullScreen.isFullScreen && fullScreen.type && fullScreen.operate) {
      switch (fullScreen.operate) {
        case "request":
          dplayer.current.fullScreen.request(fullScreen.type);
          break;
        case "cancel":
          dplayer.current.fullScreen.cancel(fullScreen.type);
          break;
        default:
          break;
      }
      setProps({
        fullScreen: {
          isFullScreen: false,
          type: "browser",
          operate: undefined,
        },
      });
    }
  }, [fullScreen]);

  useEffect(() => {
    if (switchQuality.isSwitch && switchQuality.index) {
      dplayer.current.switchQuality(switchQuality.index);
      setProps({ switchQuality: { isSwitch: false, index: undefined } });
    }
  }, [switchQuality]);

  useEffect(() => {
    if (switchVideo.isSwitch && switchVideo.video) {
      dplayer.current.switchVideo(switchVideo.video, switchVideo.danmaku);
      setProps({
        switchVideo: { isSwitch: false, video: undefined, danmaku: undefined },
      });
    }
  }, [switchVideo]);

  useEffect(() => {
    if (sendDanmaku.isSend && sendDanmaku.content) {
      dplayer.current.danmaku.send(sendDanmaku.content, function () {
        console.log("发送成功");
      });
      setProps({ sendDanmaku: { isSend: false, content: undefined } });
    }
  }, [sendDanmaku]);

  useEffect(() => {
    if (drawDanmaku.isDraw && drawDanmaku.content) {
      dplayer.current.danmaku.draw(drawDanmaku.content);
      setProps({ drawDanmakuClicks: drawDanmakuClicks + 1 });
      setProps({ drawDanmaku: { isDraw: false, content: undefined } });
    }
  }, [drawDanmaku]);

  useEffect(() => {
    if (opacityDanmaku.isOpacity && opacityDanmaku.opacity) {
      dplayer.current.danmaku.opacity(opacityDanmaku.opacity);
      setProps({ opacityDanmaku: { isOpacity: false, opacity: undefined } });
    }
  }, [opacityDanmaku]);

  useEffect(() => {
    if (clearDanmaku.isClear) {
      dplayer.current.danmaku.clear();
      setProps({ clearDanmaku: { isClear: false } });
    }
  }, [clearDanmaku]);

  useEffect(() => {
    if (hideDanmaku.isHide) {
      dplayer.current.danmaku.hide();
      setProps({ hideDanmaku: { isHide: false } });
    }
  }, [hideDanmaku]);

  useEffect(() => {
    if (showDanmaku.isShow) {
      dplayer.current.danmaku.show();
      setProps({ showDanmaku: { isShow: false } });
    }
  }, [showDanmaku]);

  useEffect(() => {
    if (destroy) {
      dplayer.current.destroy();
      setProps({ destroy: false });
    }
  }, [destroy]);

  useEffect(() => {
    // 获取所有右键菜单项
    let allMenuItems = Array.from(
      document.getElementById(dplayerId).querySelectorAll(".dplayer-menu-item")
    );

    // 将默认的右键菜单项dom文本包含'关于作者'和'DPlayer'的显示样式设置为 none
    allMenuItems.slice(-2).forEach((item) => {
      item.style.display = "none";
    });
  });

  const options = useMemo(() => {
    let subtitleOptions = subtitle.isOpen ? { subtitle: subtitle } : {};
    let danmakuOptions = danmaku.isOpen ? { danmaku: danmaku } : {};
    let contextmenuOptions =
      contextmenu.length > 0
        ? contextmenu.map((item) => {
            return {
              ...item,
              click: (player) => {
                setProps({ currentClickContextmenu: item });
              },
            };
          })
        : contextmenu;
    let _video = { ...video };
    switch (_video.type) {
      case "hls":
        _video.customType = {
          hls: function (video, player) {
            if (Hls.isSupported()) {
              const hls = new Hls();
              hls.loadSource(video.src);
              hls.attachMedia(video);
            } else {
              player.notice("Error: HLS is not supported.");
            }
          },
        };
        break;
      case "flv":
        _video.customType = {
          flv: function (video, player) {
            if (flvjs.isSupported()) {
              const flvPlayer = flvjs.createPlayer({
                type: "flv",
                url: video.src,
              });
              flvPlayer.attachMediaElement(video);
              flvPlayer.load();
            } else {
              player.notice("Error: FLV is not supported.");
            }
          },
        };
        break;
      case "dash":
        _video.customType = {
          dash: function (video, player) {
            dashjs.MediaPlayer().create().initialize(video, video.src, false);
          },
        };
        break;
      default:
        break;
    }
    return {
      ...subtitleOptions,
      ...danmakuOptions,
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
      video: _video,
      contextmenu: contextmenuOptions,
      highlight: highlight,
      mutex: mutex,
    };
  }, [
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
  ]);

  const registerEvents = (dp) => {
    dp.on("play", onPlay);
    dp.on("pause", onPause);
    dp.on("seeked", onSeeked);
    dp.on("notice_show", onNoticeShow);
    dp.on("notice_hide", onNoticeHide);
    dp.on("ratechange", onRatechange);
    dp.on("volumechange", onVolumechange);
    dp.on("screenshot", onScreenshot);
    dp.on("contextmenu_show", onContextmenuShow);
    dp.on("contextmenu_hide", onContextmenuHide);
    dp.on("fullscreen", onFullscreen);
    dp.on("fullscreen_cancel", onFullscreenCancel);
    dp.on("danmaku_send", onDanmakuSend);
    dp.on("danmaku_opacity", onDanmakuOpacity);
    dp.on("danmaku_clear", onDanmakuClear);
    dp.on("danmaku_hide", onDanmakuHide);
    dp.on("danmaku_show", onDanmakuShow);
    dp.on("subtitle_show", onSubtitleShow);
    dp.on("subtitle_hide", onSubtitleHide);
    dp.on("subtitle_change", onSubtitleChange);
    dp.on("destroy", onDestroy);
  };

  useEffect(() => {
    dplayer.current = new DPlayer({
      container: dom.current,
      ...options,
    });
    registerEvents(dplayer.current);

    return () => {
      dplayer.current?.destroy();
    };
  }, []);

  return (
    <div
      ref={dom}
      id={dplayerId}
      className={
        isString(className)
          ? className
          : className
          ? useCss(className)
          : undefined
      }
      style={style}
      key={key}
      data-dash-is-loading={useLoading()}
    ></div>
  );
};

export default FefferyDPlayer;

FefferyDPlayer.defaultProps = defaultProps;
FefferyDPlayer.propTypes = propTypes;
