import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyMusicPlayer = React.lazy(() => import(/* webpackChunkName: "feffery_music_player" */ '../../fragments/player/FefferyMusicPlayer.react'));

const FefferyMusicPlayer = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyMusicPlayer {...props} />
        </Suspense>
    );
}

// 定义参数或属性，API参数参考https://github.com/lijinke666/react-music-player#clipboard-api
FefferyMusicPlayer.propTypes = {
    /**
     * 音乐播放器id
     */
    id: PropTypes.string,

    /**
     * 设置音乐播放器的css类名
     */
    className: PropTypes.string,

    /**
     * 设置音乐播放器的样式
     */
    style: PropTypes.object,

    /**
     * 设置播放器的key，强制刷新组件
     */
    key: PropTypes.string,

    /**
     * 设置音乐播放器文件列表信息
     */
    audioLists: PropTypes.arrayOf(PropTypes.exact({
        /**
         * 音乐名称
         */
        name: PropTypes.string,
        /**
         * 音乐链接
         */
        musicSrc: PropTypes.string,
        /**
         * 音乐封面
         */
        cover: PropTypes.string,
        /**
         * 歌手
         */
        singer: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.node
        ]),
        /**
         * 歌曲时长
         */
        duration: PropTypes.number,
        /**
         * 歌词
         */
        lyric: PropTypes.string,
        /**
         * 额外的参数
         */
        extraParams: PropTypes.object
    })),

    /**
     * 设置音乐播放器主题的颜色，可选的有'light'、'dark'、'auto'，默认为'dark'
     */
    theme: PropTypes.oneOf(['light', 'dark', 'auto']),

    /**
     * 自定义主题颜色，默认为'#31c27c'
     */
    customizeThemeColor: PropTypes.string,

    /**
     * 主题为'light'时，设置相关按钮悬浮的颜色，默认为'#3ece89'
     */
    customizeLightThemeHoverColor: PropTypes.string,

    /**
     * 设置音乐播放器语言，可选的有'zh_CN'、'en_US'，默认为'zh_CN'
     */
    locale: PropTypes.oneOf(['zh_CN', 'en_US']),

    /**
     * 设置音乐播放器相关图标
     */
    icon: PropTypes.exact({
        /**
         * 设置pause图标
         */
        pause: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置play图标
         */
        play: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置destroy图标
         */
        destroy: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置close图标
         */
        close: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置delete图标
         */
        delete: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置download图标
         */
        download: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置toggle图标
         */
        toggle: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置lyric图标
         */
        lyric: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置volume图标
         */
        volume: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置mute图标
         */
        mute: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置next图标
         */
        next: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置prev图标
         */
        prev: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置playLists图标
         */
        playLists: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置reload图标
         */
        reload: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置loop图标
         */
        loop: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置order图标
         */
        order: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置orderLoop图标
         */
        orderLoop: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置shuffle图标
         */
        shuffle: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),

        /**
         * 设置loading图标
         */
        loading: PropTypes.oneOfType([
            PropTypes.node,
            PropTypes.string
        ]),
    }),

    /**
     * 设置音乐播放器mini模式的初始位置，默认为{top:0, left:0}
     */
    defaultPosition: PropTypes.exact({
        /**
         * 设置音乐播放器距离顶部的距离，默认为0
         */
        top: PropTypes.number,

        /**
         * 设置音乐播放器距离左侧的距离，默认为0
         */
        left: PropTypes.number,

        /**
         * 设置音乐播放器距离右侧的距离，默认为0
         */
        right: PropTypes.number,

        /**
         * 设置音乐播放器距离底部的距离，默认为0
         */
        bottom: PropTypes.number
    }),

    /**
     * 设置播放模式切换时提示语的显示时间（毫秒），默认为600
     */
    playModeShowTime: PropTypes.number,

    /**
     * 拖拽边界
     */
    bounds: PropTypes.oneOfType([
        PropTypes.oneOf(['body', 'parent']),
        PropTypes.exact({
            top: PropTypes.number,
            left: PropTypes.number,
            right: PropTypes.number,
            bottom: PropTypes.number
        })
    ]),

    /**
     * 设置是否在页面加载后立即加载音频，默认为false
     */
    preload: PropTypes.oneOfType([
        PropTypes.bool,
        PropTypes.oneOf(['auto'])
    ]),

    /**
     * 下次访问播放器时，是否保留最后状态，默认为false
     */
    remember: PropTypes.bool,

    /**
     * 设置背景是否显示磨砂玻璃效果，默认为false
     */
    glassBg: PropTypes.bool,

    /**
     * 设置音频是否可以被删除，默认为true
     */
    remove: PropTypes.bool,

    /**
     * 播放器的默认播放索引，默认为0
     */
    defaultPlayIndex: PropTypes.number,

    /**
     * 播放器的播放索引，默认为0
     */
    playIndex: PropTypes.number,

    /**
     * 音乐播放器选项的默认播放模式，可选的有'order'、'orderLoop'、'singleLoop'、'shufflePlay'，默认为order\
     */
    defaultPlayMode: PropTypes.oneOf(['order', 'orderLoop', 'singleLoop', 'shufflePlay']),

    /**
     * 设置播放器主题模式，可选的有'mini'、'full'，默认为mini
     */
    mode: PropTypes.oneOf(['mini', 'full']),

    /**
     * 默认的audioPlay句柄功能会在每次暂停后再次播放，如果只想触发一次，可以设置'true'，默认为false
     */
    once: PropTypes.bool,

    /**
     * 加载完成后是否播放音频。移动设备的自动播放策略更改无效，默认为true
     */
    autoplay: PropTypes.bool,

    /**
     * 是否可以在两种模式之间切换，full => mini 或 mini => full，默认为true
     */
    toggleMode: PropTypes.bool,

    /**
     * 播放器是否是可以拖拽的'mini'模式，默认为true
     */
    drag: PropTypes.bool,

    /**
     * 是否可以拖动或单击进度条以播放新进度，默认为true
     */
    seeked: PropTypes.bool,

    /**
     * 音频封面是否示'mini'模式，默认为true
     */
    showMiniModeCover: PropTypes.bool,

    /**
     * 音频进度圆条是否显示'mini'模式，默认为false
     */
    showMiniProcessBar: PropTypes.bool,

    /**
     * 是否显示音频加载进度条，默认为true
     */
    showProgressLoadBar: PropTypes.bool,

    /**
     * 是否显示播放器面板的播放按钮，默认为true
     */
    showPlay: PropTypes.bool,

    /**
     * 是否显示播放器面板的重新加载按钮，默认为true
     */
    showReload: PropTypes.bool,

    /**
     * 是否显示播放器面板的下载按钮，默认为true
     */
    showDownload: PropTypes.bool,

    /**
     * 是否显示播放器面板的播放模式切换按钮，默认为true
     */
    showPlayMode: PropTypes.bool,

    /**
     * 是否显示播放器面板的主题切换开关，默认为true
     */
    showThemeSwitch: PropTypes.bool,

    /**
     * 是否显示播放器面板的音频歌词按钮，默认为false
     */
    showLyric: PropTypes.bool,

    /**
     * https://web.dev/media-session/，默认为false
     */
    showMediaSession: PropTypes.bool,

    /**
     * 音频歌词类名
     */
    lyricClassName: PropTypes.string,

    /**
     * 可扩展的自定义内容
     */
    extendsContent: PropTypes.oneOfType([
        PropTypes.node,
        PropTypes.bool,
        PropTypes.string
    ]),

    /**
     * 音频播放器的默认音量，范围0-1，默认为1
     */
    defaultVolume: PropTypes.number,

    /**
     * 当前音频播放失败时是否尝试播放下一个音频，默认为true
     */
    loadAudioErrorPlayNext: PropTypes.bool,

    /**
     * 是否开启响应模式，如果设置为false，音频控制器始终显示桌面ui，默认为true
     */
    responsive: PropTypes.bool,

    /**
     * 如果没有可用的封面照片，是否自动隐藏封面照片，默认为false
     */
    autoHiddenCover: PropTypes.bool,

    /**
     * 是否将新播放列表替换为第一个加载的播放列表，并将 playIndex 重置为 0，默认为false
     */
    clearPriorAudioLists: PropTypes.bool,

    /**
     * 加载新播放列表后是否立即播放您的新播放列表，默认为false
     */
    autoPlayInitLoadPlayList: PropTypes.bool,

    /**
     * 是否可以通过空格键播放和暂停音频（桌面有效），默认为false
     */
    spaceBar: PropTypes.bool,

    /**
     * 是否显示销毁按钮，默认为false
     */
    showDestroy: PropTypes.bool,

    /**
     * https://github.com/lijinke666/react-music-player#bulb-quiet-update
     */
    quietUpdate: PropTypes.bool,

    /**
     * 尝试播放上一首歌曲时，如果歌曲的当前时间超过 1 秒，是否重新启动当前曲目，默认为false
     */
    restartCurrentOnPrev: PropTypes.bool,

    /**
     * 自定义挂载容器类名
     */
    customizeContainerId: PropTypes.string,

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
    bounds: 'body',
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

export const propTypes = FefferyMusicPlayer.propTypes;
export const defaultProps = FefferyMusicPlayer.defaultProps;