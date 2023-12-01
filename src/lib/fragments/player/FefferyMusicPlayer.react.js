import React, { useEffect } from 'react';
import ReactJkMusicPlayer from 'react-jinke-music-player'
import 'react-jinke-music-player/assets/index.css'
import { propTypes, defaultProps } from '../../components/player/FefferyMusicPlayer.react';

// 定义音乐播放组件FefferyMusicPlayer
const FefferyMusicPlayer = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        key,
        audioLists,
        theme,
        customizeThemeColor,
        customizeLightThemeHoverColor,
        locale,
        icon,
        defaultPosition,
        playModeShowTime,
        bounds,
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
        customizeContainerId,
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
            style={style}
            className={className}
            key={key}
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
            bounds={bounds}
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
            getContainer={customizeContainerId ? () => document.querySelector(`#${customizeContainerId}`) : document.body}
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

export default FefferyMusicPlayer;

FefferyMusicPlayer.defaultProps = defaultProps;
FefferyMusicPlayer.propTypes = propTypes;