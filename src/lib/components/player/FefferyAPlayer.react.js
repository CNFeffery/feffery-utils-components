import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyAPlayer = React.lazy(() => import(/* webpackChunkName: "aplayer" */ '../../fragments/player/FefferyAPlayer.react'));

const FefferyAPlayer = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyAPlayer {...props} />
        </Suspense>
    );
}

// 定义参数或属性，API参数参考https://github.com/MoePlayer/react-aplayer#props
FefferyAPlayer.propTypes = {
    /**
     * 播放器id 
     */
    id: PropTypes.string,

    /**
     * 设置播放器的css类名 
     */
    className: PropTypes.string,

    /**
     * 设置播放器的样式
     */
    style: PropTypes.object,

    /**
     * 设置播放器的key，强制刷新组件
     */
    key: PropTypes.string,

    /**
     * 是否开启吸底模式，默认为false
     */
    fixed: PropTypes.bool,

    /**
     * 是否开启迷你模式，默认为false
     */
    mini: PropTypes.bool,

    /**
     * 音频是否自动播放，默认为false
     */
    autoplay: PropTypes.bool,

    /**
     * 设置主题色，默认为'#b7daff'
     */
    theme: PropTypes.string,

    /**
     * 设置音频循环播放, 可选值: 'all', 'one', 'none'，默认为'all'
     */
    loop: PropTypes.oneOf(['all', 'one', 'none']),

    /**
     * 设置音频循环顺序, 可选值: 'list', 'random'，默认为'list'
     */
    order: PropTypes.oneOf(['list', 'random']),

    /**
     * 设置音频预加载，可选值: 'none', 'metadata', 'auto'，默认为'auto'
     */
    preload: PropTypes.oneOf(['none', 'metadata', 'auto']),

    /**
     * 默认音量，请注意播放器会记忆用户设置，用户手动设置音量后默认音量即失效
     */
    volume: PropTypes.number,

    /**
     * 设置音频信息
     */
    audio: PropTypes.arrayOf(PropTypes.exact({
        /**
         * 设置音频名称
         */
        name: PropTypes.string,
        /**
         * 设置音频作者
         */
        artist: PropTypes.string,
        /**
         * 设置音频链接
         */
        url: PropTypes.string,
        /**
         * 设置音频封面
         */
        cover: PropTypes.string,
        /**
         * 设置音频lrc歌词
         */
        lrc: PropTypes.string,
        /**
         * 设置切换到此音频时的主题色，比上面的 theme 优先级高
         */
        theme: PropTypes.string,
        /**
         * 设置音频类型，可选的有'auto'、'hls'、'normal'，默认为'auto'
         */
        type: PropTypes.oneOf(['auto', 'hls', 'normal'])
    })),

    /**
     * 是否互斥，阻止多个播放器同时播放，当前播放器播放时暂停其他播放器，默认为true
     */
    mutex: PropTypes.bool,

    /**
     * 有三种方式来给APlayer传递歌词，使用lrcType参数指明使用哪种方式，然后把歌词放到audio.lrc参数或者HTML里
     * 1表示把歌词放到JS字符串里面，2表示把歌词放到HTML里面，3表示把歌词放到 LRC 文件里，音频播放时会加载对应的 LRC 文件
     * audio.lrc支持下面格式的歌词：
     * [mm:ss]APlayer[mm:ss.xx]is
     * [mm:ss.xxx]amazing
     * [mm:ss.xx][mm:ss.xx]APlayer
     * [mm:ss.xx]<mm:ss.xx>is
     * [mm:ss.xx]amazing[mm:ss.xx]APlayer
     */
    lrcType: PropTypes.oneOf([0, 1, 2, 3]),

    /**
     * 列表是否默认折叠，默认为false
     */
    listFolded: PropTypes.bool,

    /**
     * 设置列表最大高度
     */
    listMaxHeight: PropTypes.number,

    /**
     * 存储播放器设置的 localStorage key，默认为'aplayer-setting'
     */
    storageName: PropTypes.string,

    /**
     * 播放音频，每次设置为true后执行完相应操作后会自动置为false
     */
    play: PropTypes.bool,

    /**
     * 暂停音频，每次设置为true后执行完相应操作后会自动置为false
     */
    pause: PropTypes.bool,

    /**
     * 跳转到特定时间，时间的单位为秒，每次isSeek设置为true后执行完相应操作后会自动置为false
     */
    seek: PropTypes.exact({
        isSeek: PropTypes.bool,
        /**
         * 跳转到的时间
         */
        time: PropTypes.number,
    }),

    /**
     * 切换到上一首音频，每次设置为true后执行完相应操作后会自动置为false
     */
    skipBack: PropTypes.bool,

    /**
     * 切换到下一首音频，每次设置为true后执行完相应操作后会自动置为false
     */
    skipForward: PropTypes.bool,

    /**
     * 显示歌词，每次设置为true后执行完相应操作后会自动置为false
     */
    showLrc: PropTypes.bool,

    /**
     * 隐藏歌词，每次设置为true后执行完相应操作后会自动置为false
     */
    hideLrc: PropTypes.bool,

    /**
     * 显示通知信息，每次isShow设置为true后执行完相应操作后会自动置为false
     */
    notice: PropTypes.exact({
        isShow: PropTypes.bool,
        /**
         * 通知内容
         */
        text: PropTypes.string,
        /**
         * 通知持续时间，单位为毫秒，设置时间为 0 可以取消通知自动隐藏
         */
        time: PropTypes.number,
        /**
         * 通知透明度
         */
        opacity: PropTypes.number,
    }),

    /**
     * 显示播放列表，每次设置为true后执行完相应操作后会自动置为false
     */
    showList: PropTypes.bool,

    /**
     * 隐藏播放列表，每次设置为true后执行完相应操作后会自动置为false
     */
    hideList: PropTypes.bool,

    /**
     * 增加音频到播放列表，每次isAdd设置为true后执行完相应操作后会自动置为false
     */
    addList: PropTypes.exact({
        isAdd: PropTypes.bool,
        /**
         * 音频信息
         */
        audio: PropTypes.arrayOf(PropTypes.exact({
            /**
             * 设置音频名称
             */
            name: PropTypes.string,
            /**
             * 设置音频作者
             */
            artist: PropTypes.string,
            /**
             * 设置音频链接
             */
            url: PropTypes.string,
            /**
             * 设置音频封面
             */
            cover: PropTypes.string,
            /**
             * 设置音频lrc歌词
             */
            lrc: PropTypes.string,
            /**
             * 设置切换到此音频时的主题色，比上面的 theme 优先级高
             */
            theme: PropTypes.string,
            /**
             * 设置音频类型，可选的有'auto'、'hls'、'normal'，默认为'auto'
             */
            type: PropTypes.oneOf(['auto', 'hls', 'normal'])
        })),
    }),

    /**
     * 删除播放列表中的音频，每次isDelete设置为true后执行完相应操作后会自动置为false
     */
    removeList: PropTypes.exact({
        isRemove: PropTypes.bool,
        /**
         * 音频索引
         */
        index: PropTypes.number,
    }),

    /**
     * 切换播放列表，每次isSwitch设置为true后执行完相应操作后会自动置为false
     */
    switchList: PropTypes.exact({
        isSwitch: PropTypes.bool,
        /**
         * 音频索引
         */
        index: PropTypes.number,
    }),

    /**
     * 清空播放列表，每次设置为true后执行完相应操作后会自动置为false
     */
    clearList: PropTypes.bool,

    /**
     * 销毁播放器，每次设置为true后执行完相应操作后会自动置为false
     */
    destroy: PropTypes.bool,

    /**
     * 监听参数，播放音频的次数
     */
    playClicks: PropTypes.number,

    /**
     * 监听参数，暂停音频的次数
     */
    pauseClicks: PropTypes.number,

    /**
     * 监听参数，跳转到特定时间的次数
     */
    seekClicks: PropTypes.number,

    /**
     * 监听参数，通过函数切换到上一首音频的次数
     */
    skipBackClicks: PropTypes.number,

    /**
     * 监听参数，通过函数切换到下一首音频的次数
     */
    skipForwardClicks: PropTypes.number,

    /**
     * 监听参数，显示歌词的次数
     */
    showLrcClicks: PropTypes.number,

    /**
     * 监听参数，隐藏歌词的次数
     */
    hideLrcClicks: PropTypes.number,

    /**
     * 监听参数，显示通知的次数
     */
    showNoticeClicks: PropTypes.number,

    /**
     * 监听参数，隐藏通知的次数
     */
    hideNoticeClicks: PropTypes.number,

    /**
     * 监听参数，显示播放列表的次数
     */
    listShowClicks: PropTypes.number,

    /**
     * 监听参数，隐藏播放列表的次数
     */
    listHideClicks: PropTypes.number,

    /**
     * 监听参数，添加音频到播放列表的次数
     */
    listAddClicks: PropTypes.number,

    /**
     * 监听参数，删除音频的次数
     */
    listRemoveClicks: PropTypes.number,

    /**
     * 监听参数，切换到播放列表里的其他音频的次数
     */
    listSwitchClicks: PropTypes.number,

    /**
     * 监听参数，清空播放列表的次数
     */
    listClearClicks: PropTypes.number,

    /**
     * 监听参数，播放器销毁的次数
     */
    destroyClicks: PropTypes.number,

    /**
     * 监听参数，当前播放的音频信息
     */
    currentPlayAudioInfo: PropTypes.object,

    /**
     * 监听参数，当前暂停的音频信息
     */
    currentPauseAudioInfo: PropTypes.object,

    /**
     * 监听参数，当前改动进度条的音频信息
     */
    currentSeekAudioInfo: PropTypes.object,

    /**
     * 监听参数，当前显示的通知信息
     */
    currentNoticeInfo: PropTypes.object,

    /**
     * 监听参数，当前列表执行添加操作的音频信息
     */
    currentListAddAudioInfo: PropTypes.object,

    /**
     * 监听参数，当前列表执行移除操作的音频信息
     */
    currentListRemoveAudioInfo: PropTypes.object,

    /**
     * 监听参数，当前列表切换到的音频信息
     */
    currentListSwitchAudioInfo: PropTypes.object,

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
FefferyAPlayer.defaultProps = {
    fixed: false,
    mini: false,
    autoplay: false,
    theme: '#b7daff',
    loop: 'all',
    order: 'list',
    preload: 'auto',
    volume: 0.7,
    audio: [{
        type: 'auto'
    }],
    mutex: true,
    lrcType: 0,
    listFolded: false,
    storageName: 'aplayer-setting',
    play: false,
    pause: false,
    seek: {
        isSeek: false
    },
    skipBack: false,
    skipForward: false,
    showLrc: false,
    hideLrc: false,
    notice: {
        isShow: false,
        time: 2000,
        opacity: 0.8
    },
    showList: false,
    hideList: false,
    addList: {
        isAdd: false
    },
    removeList: {
        isRemove: false
    },
    switchList: {
        isSwitch: false
    },
    clearList: false,
    destroy: false,
    playClicks: 0,
    pauseClicks: 0,
    seekClicks: 0,
    skipBackClicks: 0,
    skipForwardClicks: 0,
    showLrcClicks: 0,
    hideLrcClicks: 0,
    showNoticeClicks: 0,
    hideNoticeClicks: 0,
    listShowClicks: 0,
    listHideClicks: 0,
    listAddClicks: 0,
    listRemoveClicks: 0,
    listSwitchClicks: 0,
    listClearClicks: 0,
    destroyClicks: 0
}

export default FefferyAPlayer;

export const propTypes = FefferyAPlayer.propTypes;
export const defaultProps = FefferyAPlayer.defaultProps;