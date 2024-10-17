import React, { useRef, useEffect } from 'react';
import ReactAplayer from 'react-aplayer';
import Hls from 'hls.js';
import { v4 as uuidv4 } from 'uuid';
import { isString } from 'lodash';
import useCss from '../../hooks/useCss';
import { propTypes, defaultProps } from '../../components/player/FefferyAPlayer.react';

/**
 * 音频播放组件FefferyAPlayer
 */
const FefferyAPlayer = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        key,
        fixed,
        mini,
        autoplay,
        theme,
        loop,
        order,
        preload,
        volume,
        audio,
        mutex,
        lrcType,
        listFolded,
        listMaxHeight,
        storageName,
        play,
        pause,
        seek,
        skipBack,
        skipForward,
        showLrc,
        hideLrc,
        notice,
        showList,
        hideList,
        addList,
        removeList,
        switchList,
        clearList,
        destroy,
        playClicks,
        pauseClicks,
        seekClicks,
        skipBackClicks,
        skipForwardClicks,
        showLrcClicks,
        hideLrcClicks,
        showNoticeClicks,
        hideNoticeClicks,
        listShowClicks,
        listHideClicks,
        listAddClicks,
        listRemoveClicks,
        listSwitchClicks,
        listClearClicks,
        destroyClicks,
        currentPlayAudioInfo,
        currentPauseAudioInfo,
        currentSeekAudioInfo,
        currentNoticeInfo,
        currentListAddAudioInfo,
        currentListRemoveAudioInfo,
        currentListSwitchAudioInfo,
        setProps,
        loading_state
    } = props;

    const containerId = uuidv4();

    const ap = useRef(null);

    const onInit = (aplayer) => {
        ap.current = aplayer;
    };

    const onPlay = () => {
        setProps({ currentPlayAudioInfo: ap.current.list.audios[ap.current.list.index] });
        setProps({ playClicks: playClicks + 1 })
    };

    const onPause = () => {
        setProps({ currentPauseAudioInfo: ap.current.list.audios[ap.current.list.index] });
        setProps({ pauseClicks: pauseClicks + 1 })
    };

    const onSeeked = () => {
        setProps({ currentSeekAudioInfo: ap.current.list.audios[ap.current.list.index] });
        setProps({ seekClicks: seekClicks + 1 })
    };

    const onLrcshow = (e) => {
        setProps({ showLrcClicks: showLrcClicks + 1 })
    };

    const onLrchide = (e) => {
        setProps({ hideLrcClicks: hideLrcClicks + 1 })
    };

    const onNoticeshow = (e) => {
        setProps({ currentNoticeInfo: e });
        setProps({ showNoticeClicks: showNoticeClicks + 1 })
    };

    const onNoticehide = (e) => {
        setProps({ hideNoticeClicks: hideNoticeClicks + 1 })
    };

    const onListshow = () => {
        setProps({ listShowClicks: listShowClicks + 1 })
    };

    const onListHide = () => {
        setProps({ listHideClicks: listHideClicks + 1 })
    };

    const onListAdd = (e) => {
        setProps({ currentListAddAudioInfo: e });
        setProps({ listAddClicks: listAddClicks + 1 })
    };

    const onListRemove = (e) => {
        setProps({ currentListRemoveAudioInfo: ap.current.list.audios[e.index] });
        setProps({ listRemoveClicks: listRemoveClicks + 1 })
    };

    const onListSwitch = (e) => {
        setProps({ currentListSwitchAudioInfo: ap.current.list.audios[e.index] });
        setProps({ listSwitchClicks: listSwitchClicks + 1 })
    };

    const onListClear = (e) => {
        setProps({ listClearClicks: listClearClicks + 1 })
    };

    const onDestroy = (e) => {
        setProps({ destroyClicks: destroyClicks + 1 })
    };

    useEffect(() => {
        if (play) {
            ap.current.play();
            setProps({ play: false });
        }
    }, [play])

    useEffect(() => {
        if (pause) {
            ap.current.pause();
            setProps({ pause: false });
        }
    }, [pause])

    useEffect(() => {
        if (seek.isSeek && seek.time) {
            ap.current.seek(seek.time);
            setProps({ seek: { isSeek: false, time: undefined } });
        }
    }, [seek])

    useEffect(() => {
        if (skipBack) {
            ap.current.skipBack();
            setProps({ skipBackClicks: skipBackClicks + 1 });
            setProps({ skipBack: false });
        }
    }, [skipBack])

    useEffect(() => {
        if (skipForward) {
            ap.current.skipForward();
            setProps({ skipForwardClicks: skipForwardClicks + 1 });
            setProps({ skipForward: false });
        }
    }, [skipForward])

    useEffect(() => {
        if (showLrc && ap.current.list.audios[ap.current.list.index].lrc) {
            ap.current.lrc.show();
            setProps({ showLrc: false });
        }
    }, [showLrc])

    useEffect(() => {
        if (hideLrc && ap.current.list.audios[ap.current.list.index].lrc) {
            ap.current.lrc.hide();
            setProps({ hideLrc: false });
        }
    }, [hideLrc])

    useEffect(() => {
        if (notice.isShow && notice.text) {
            ap.current.notice(notice.text, notice.time, notice.opacity);
            setProps({ notice: { isShow: false, text: undefined, time: 2000, opacity: 0.8 } });
        }
    }, [notice])

    useEffect(() => {
        if (showList) {
            ap.current.list.show();
            setProps({ showList: false });
        }
    }, [showList])

    useEffect(() => {
        if (hideList) {
            ap.current.list.hide();
            setProps({ hideList: false });
        }
    }, [hideList])

    useEffect(() => {
        if (addList.isAdd && addList.audio) {
            ap.current.list.add(addList.audio);
            setProps({ addList: { isAdd: false, audio: undefined } });
        }
    }, [addList])

    useEffect(() => {
        if (removeList.isRemove && removeList.index) {
            ap.current.list.remove(removeList.index);
            setProps({ removeList: { isRemove: false, index: undefined } });
        }
    }, [removeList])

    useEffect(() => {
        if (switchList.isSwitch && switchList.index) {
            ap.current.list.switch(switchList.index);
            setProps({ switchList: { isSwitch: false, index: undefined } });
        }
    }, [switchList])

    useEffect(() => {
        if (clearList) {
            ap.current.list.clear();
            setProps({ clearList: false });
        }
    }, [clearList])

    useEffect(() => {
        if (destroy) {
            ap.current.destroy();
            setProps({ destroy: false });
        }
    }, [destroy])

    const customAudioType = {
        'hls': function (audioElement, audio, player) {
            if (Hls.isSupported()) {
                const hls = new Hls();
                hls.loadSource(audio.url);
                hls.attachMedia(audioElement);
            }
            else if (audioElement.canPlayType('application/x-mpegURL') || audioElement.canPlayType('application/vnd.apple.mpegURL')) {
                audioElement.src = audio.url;
            }
            else {
                player.notice('Error: HLS is not supported.');
            }
        }
    };

    return (
        <div id={containerId}>
            <ReactAplayer
                id={id}
                className={
                    isString(className) ?
                        className :
                        (className ? useCss(className) : undefined)
                }
                style={style}
                key={key}
                container={document.getElementById(containerId)}
                fixed={fixed}
                mini={mini}
                autoplay={autoplay}
                theme={theme}
                loop={loop}
                order={order}
                preload={preload}
                volume={volume}
                audio={audio}
                customAudioType={customAudioType}
                mutex={mutex}
                lrcType={lrcType}
                listFolded={listFolded}
                listMaxHeight={listMaxHeight}
                storageName={storageName}
                onInit={onInit}
                onPlay={onPlay}
                onPause={onPause}
                onSeeked={onSeeked}
                onLrcshow={onLrcshow}
                onLrchide={onLrchide}
                onNoticeshow={onNoticeshow}
                onNoticehide={onNoticehide}
                onListshow={onListshow}
                onListhide={onListHide}
                onListadd={onListAdd}
                onListremove={onListRemove}
                onListswitch={onListSwitch}
                onListclear={onListClear}
                onDestroy={onDestroy}
                loading_state={loading_state}
            />
        </div>
    )
}

export default FefferyAPlayer;

FefferyAPlayer.defaultProps = defaultProps;
FefferyAPlayer.propTypes = propTypes;