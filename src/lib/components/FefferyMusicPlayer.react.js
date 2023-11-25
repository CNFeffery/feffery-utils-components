import React, { useEffect } from 'react';
import ReactJkMusicPlayer from 'react-jinke-music-player'
import 'react-jinke-music-player/assets/index.css'
import PropTypes from 'prop-types';

// 定义音乐播放组件FefferyMusicPlayer
const FefferyMusicPlayer = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        audioLists,
        theme,
        customizeThemeColor,
        customizeLightThemeHoverColor,
        locale,
        icon,
        defaultPosition,
        playModeShowTime,
        preload,
        remember,
        glassBg,
        remove,
        defaultPlayIndex,
        playIndex,
        mode,
        once,
        autoplay,
        toggleMode,
        drag,
        seeked,
        showMiniModeCover,
        showMiniProcessBar,
        showProgressLoadBar,
        showPlay,
        showReload,
        showDownload,
        showPlayMode,
        showThemeSwitch,
        showLyric,
        showMediaSession,
        lyricClassName,
        extendsContent,
        defaultVolume,
        loadAudioErrorPlayNext,
        responsive,
        autoHiddenCover,
        clearPriorAudioLists,
        autoPlayInitLoadPlayList,
        spaceBar,
        showDestroy,
        quietUpdate,
        restartCurrentOnPrev,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        const style = document.createElement('style');
        style.innerHTML = `
        .react-jinke-music-player-main .loading svg{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-mobile-play-model-tip{
            background-color: ${customizeThemeColor};
        }
        .react-jinke-music-player-mobile-progress .rc-slider-handle,.react-jinke-music-player-mobile-progress .rc-slider-track{
            background-color: ${customizeThemeColor};
        }
        .react-jinke-music-player-mobile-progress .rc-slider-handle:active{
            box-shadow:0 0 2px ${customizeThemeColor};
        }
        .audio-lists-panel-content .audio-item.playing, .audio-lists-panel-content .audio-item.playing svg{
            color: ${customizeThemeColor};
        }
        .audio-lists-panel-content .audio-item:active .group:not([class=".player-delete"]) svg,.audio-lists-panel-content .audio-item:hover .group:not([class=".player-delete"]) svg{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main ::-webkit-scrollbar-thumb{
            background-color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main .lyric-btn-active, .react-jinke-music-player-main .lyric-btn-active svg{
            color: ${customizeThemeColor}!important;
        }
        .react-jinke-music-player-main .music-player-lyric{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main svg:active, .react-jinke-music-player-main svg:hover{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main .music-player-panel .panel-content .rc-slider-handle, .react-jinke-music-player-main .music-player-panel .panel-content .rc-slider-track{
            background-color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main .music-player-panel .panel-content .rc-slider-handle:active{
            box-shadow:0 0 2px ${customizeThemeColor};
        }
        .react-jinke-music-player-main .music-player-panel .panel-content .progress-bar-content .progress-bar .progress{
            background-color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main .music-player-panel .panel-content .player-content>.group>i{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main .music-player-panel .panel-content .player-content .loop-btn.active{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main .music-player-panel .panel-content .player-content .audio-lists-btn>.group:hover,.react-jinke-music-player-main .music-player-panel .panel-content .player-content .audio-lists-btn>.group:hover>svg{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main.light-theme svg{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main.light-theme svg:hover{
            color: ${customizeLightThemeHoverColor};
        }
        .react-jinke-music-player-main.light-theme .rc-switch-checked{
            background-color: ${customizeThemeColor}!important;border:1px solid ${customizeThemeColor};
        }
        .react-jinke-music-player-main.light-theme .audio-lists-panel .audio-item.playing, .react-jinke-music-player-main.light-theme .audio-lists-panel .audio-item.playing svg{
            color: ${customizeThemeColor}!important;
        }
        .react-jinke-music-player-main.light-theme .audio-item:active svg, .react-jinke-music-player-main.light-theme .audio-item:hover svg{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main.light-theme .audio-item.playing svg{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player-main.light-theme .audio-item.playing .player-singer{
            color: ${customizeThemeColor}!important;
        }
        .react-jinke-music-player-main.light-theme .play-mode-title{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player .music-player-controller{
            color: ${customizeThemeColor};
        }
        .react-jinke-music-player .audio-circle-process-bar circle[class=stroke]{
            stroke: ${customizeThemeColor};
        }
        `;
        document.head.appendChild(style);
    }, [customizeThemeColor, customizeLightThemeHoverColor]);

    return (
        <ReactJkMusicPlayer
            id={id}
            className={className}
            audioLists={audioLists.map(({ extraParams, ...audio }) => {
                return {
                    ...audio,
                    ...extraParams
                };
            })}
            theme={theme}
            locale={locale}
            icon={icon}
            defaultPosition={defaultPosition}
            playModeShowTime={playModeShowTime}
            preload={preload}
            remember={remember}
            glassBg={glassBg}
            remove={remove}
            defaultPlayIndex={defaultPlayIndex}
            playIndex={playIndex}
            mode={mode}
            once={once}
            autoplay={autoplay}
            toggleMode={toggleMode}
            drag={drag}
            seeked={seeked}
            showMiniModeCover={showMiniModeCover}
            showMiniProcessBar={showMiniProcessBar}
            showProgressLoadBar={showProgressLoadBar}
            showPlay={showPlay}
            showReload={showReload}
            showDownload={showDownload}
            showPlayMode={showPlayMode}
            showThemeSwitch={showThemeSwitch}
            showLyric={showLyric}
            showMediaSession={showMediaSession}
            lyricClassName={lyricClassName}
            extendsContent={extendsContent}
            defaultVolume={defaultVolume}
            loadAudioErrorPlayNext={loadAudioErrorPlayNext}
            responsive={responsive}
            autoHiddenCover={autoHiddenCover}
            clearPriorAudioLists={clearPriorAudioLists}
            autoPlayInitLoadPlayList={autoPlayInitLoadPlayList}
            spaceBar={spaceBar}
            showDestroy={showDestroy}
            quietUpdate={quietUpdate}
            restartCurrentOnPrev={restartCurrentOnPrev}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } >
        </ReactJkMusicPlayer>
    )
}

// 定义参数或属性
FefferyMusicPlayer.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置容器的css类名
    className: PropTypes.string,

    // 设置音乐播放器文件列表信息
    audioLists: PropTypes.arrayOf(PropTypes.exact({
        cover: PropTypes.string,
        currentTime: PropTypes.number,
        duration: PropTypes.number,
        ended: PropTypes.bool,
        musicSrc: PropTypes.string,
        muted: PropTypes.bool,
        name: PropTypes.string,
        networkState: PropTypes.number,
        paused: PropTypes.bool,
        played: PropTypes.bool,
        readyState: PropTypes.number,
        startDate: PropTypes.any,
        volume: PropTypes.number,
        lyric: PropTypes.string,
        extraParams: PropTypes.object,
    })),

    // 设置音乐播放器主题的颜色，可选的有'light'、'dark'、'auto'，默认为'dark'
    theme: PropTypes.oneOf(['light', 'dark', 'auto']),

    // 自定义主题颜色，默认为'#31c27c'
    customizeThemeColor: PropTypes.string,

    // 主题为'light'时，设置相关按钮悬浮的颜色，默认为'#3ece89'
    customizeLightThemeHoverColor: PropTypes.string,

    // 设置音乐播放器语言，可选的有'zh_CN'、'en_US'，默认为'zh_CN'
    locale: PropTypes.oneOf(['zh_CN', 'en_US']),

    // 设置音乐播放器相关图标
    icon: PropTypes.exact({
        // 设置pause图标
        pause: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置play图标
        play: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置destroy图标
        destroy: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置close图标
        close: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置delete图标
        delete: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置download图标
        download: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置toggle图标
        toggle: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置lyric图标
        lyric: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置volume图标
        volume: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置mute图标
        mute: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置next图标
        next: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置prev图标
        prev: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置playLists图标
        playLists: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置reload图标
        reload: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置loop图标
        loop: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置order图标
        order: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置orderLoop图标
        orderLoop: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置shuffle图标
        shuffle: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        // 设置loading图标
        loading: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),
    }),

    // 设置音乐播放器初始位置，默认为{top:0, left:0}
    defaultPosition: PropTypes.exact({
        // 设置音乐播放器距离顶部的距离，默认为0
        top: PropTypes.number,

        // 设置音乐播放器距离左侧的距离，默认为0
        left: PropTypes.number,

        // 设置音乐播放器距离右侧的距离，默认为0
        right: PropTypes.number,

        // 设置音乐播放器距离底部的距离，默认为0
        bottom: PropTypes.number
    }),

    // 设置播放模式切换显示时间（毫秒），默认为600
    playModeShowTime: PropTypes.number,

    // 设置是否在页面加载后立即加载音频，默认为false
    preload: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.oneOf(['auto'])
    ]),

    // The next time you access the player, do you keep the last state，默认为false
    remember: PropTypes.bool,

    // Whether the player's background displays frosted glass effect，默认为false
    glassBg: PropTypes.bool,

    // The Audio Can be deleted，默认为true
    remove: PropTypes.bool,

    // Default play index of the audio player，默认为0
    defaultPlayIndex: PropTypes.number,

    // play index of the audio player，默认为0
    playIndex: PropTypes.number,

    // 音乐播放器选项的默认播放模式，可选的有'order'、'orderLoop'、'singleLoop'、'shufflePlay'，默认为order
    defaultPlayMode: PropTypes.oneOf(['order', 'orderLoop', 'singleLoop', 'shufflePlay']),

    // audio theme switch checkedText，默认为mini
    mode: PropTypes.oneOf(['mini', 'full']),

    // The default audioPlay handle function will be played again after each pause, If you only want to trigger it once, you can set 'true'，默认为false
    once: PropTypes.bool,

    // Whether the audio is played after loading is completed. mobile devices are invalid autoplay-policy-changes，默认为true
    autoplay: PropTypes.bool,

    // Whether you can switch between two modes, full => mini or mini => full，默认为true
    toggleMode: PropTypes.bool,

    // audio controller is can be drag of the "mini" mode，默认为true
    drag: PropTypes.bool,

    // Whether you can drag or click the progress bar to play in the new progress，默认为true
    seeked: PropTypes.bool,

    // audio cover is show of the "mini" mode，默认为true
    showMiniModeCover: PropTypes.bool,

    // audio progress circle bar is show of the "mini" mode，默认为false
    showMiniProcessBar: PropTypes.bool,

    // Displays the audio load progress bar，默认为true
    showProgressLoadBar: PropTypes.bool,

    // play button display of the audio player panel，默认为true
    showPlay: PropTypes.bool,

    // reload button display of the audio player panel，默认为true
    showReload: PropTypes.bool,

    // download button display of the audio player panel，默认为true
    showDownload: PropTypes.bool,

    // play mode toggle button display of the audio player panel，默认为true
    showPlayMode: PropTypes.bool,

    // theme toggle switch display of the audio player panel，默认为true
    showThemeSwitch: PropTypes.bool,

    // audio lyric button display of the audio player panel，默认为false
    showLyric: PropTypes.bool,

    // https://web.dev/media-session/，默认为false
    showMediaSession: PropTypes.bool,

    // audio lyric class name
    lyricClassName: PropTypes.string,

    // Extensible custom content like <><button>button1</button> <button>button2</button></>
    extendsContent: PropTypes.oneOfType([
        PropTypes.node,
        PropTypes.bool,
        PropTypes.string
    ]),

    // default volume of the audio player , range 0-1，默认为1
    defaultVolume: PropTypes.number,

    // Whether to try playing the next audio when the current audio playback fails，默认为true
    loadAudioErrorPlayNext: PropTypes.bool,

    // Whether to turn on the response mode, if set false, audio controller always show desktop ui，默认为true
    responsive: PropTypes.bool,

    // Auto hide the cover photo if no cover photo is available，默认为false
    autoHiddenCover: PropTypes.bool,

    // Replace a new playlist with the first loaded playlist and reset playIndex to 0，默认为false
    clearPriorAudioLists: PropTypes.bool,

    // Play your new play list right after your new play list is loaded turn false，默认为false
    autoPlayInitLoadPlayList: PropTypes.bool,

    // Play and pause audio through space bar （Desktop effective），默认为false
    spaceBar: PropTypes.bool,

    // Destroy player button display，默认为false
    showDestroy: PropTypes.bool,

    quietUpdate: PropTypes.bool,

    // Restarts the current track when trying to play previous song, if the current time of the song is more than 1 second，默认为false
    restartCurrentOnPrev: PropTypes.bool,

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
FefferyMusicPlayer.defaultProps = {
    theme: 'dark',
    customizeThemeColor: '#31c27c',
    customizeLightThemeHoverColor: '#3ece89',
    locale: 'zh_CN',
    defaultPosition: {
        top: 0,
        left: 0
    },
    playModeShowTime: 600,
    preload: false,
    remember: false,
    glassBg: false,
    remove: true,
    defaultPlayIndex: 0,
    playIndex: 0,
    defaultPlayMode: 'order',
    mode: 'mini',
    once: false,
    autoplay: true,
    toggleMode: true,
    drag: true,
    seeked: true,
    showMiniModeCover: true,
    showMiniProcessBar: false,
    showProgressLoadBar: true,
    showPlay: true,
    showReload: true,
    showDownload: true,
    showPlayMode: true,
    showThemeSwitch: true,
    showLyric: false,
    showMediaSession: false,
    defaultVolume: 1,
    loadAudioErrorPlayNext: true,
    responsive: true,
    autoHiddenCover: false,
    clearPriorAudioLists: false,
    autoPlayInitLoadPlayList: false,
    spaceBar: false,
    showDestroy: false,
    quietUpdate: false,
    restartCurrentOnPrev: false
}

export default FefferyMusicPlayer;