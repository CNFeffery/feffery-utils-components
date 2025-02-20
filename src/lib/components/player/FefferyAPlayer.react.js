import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyAPlayer = React.lazy(() => import(/* webpackChunkName: "feffery_aplayer" */ '../../fragments/player/FefferyAPlayer.react'));

/**
 * 音频播放组件FefferyAPlayer
 */
const FefferyAPlayer = ({
    fixed = false,
    mini = false,
    autoplay = false,
    theme = '#b7daff',
    loop = 'all',
    order = 'list',
    preload = 'auto',
    volume = 0.7,
    audio = [{ type: 'auto' }],
    mutex = true,
    lrcType = 0,
    listFolded = false,
    storageName = 'aplayer-setting',
    play = false,
    pause = false,
    seek = { isSeek: false },
    skipBack = false,
    skipForward = false,
    showLrc = false,
    hideLrc = false,
    notice = { isShow: false, time: 2000, opacity: 0.8 },
    showList = false,
    hideList = false,
    addList = { isAdd: false },
    removeList = { isRemove: false },
    switchList = { isSwitch: false },
    clearList = false,
    destroy = false,
    playClicks = 0,
    pauseClicks = 0,
    seekClicks = 0,
    skipBackClicks = 0,
    skipForwardClicks = 0,
    showLrcClicks = 0,
    hideLrcClicks = 0,
    showNoticeClicks = 0,
    hideNoticeClicks = 0,
    listShowClicks = 0,
    listHideClicks = 0,
    listAddClicks = 0,
    listRemoveClicks = 0,
    listSwitchClicks = 0,
    listClearClicks = 0,
    destroyClicks = 0,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyAPlayer {
                ...{
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
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyAPlayer.propTypes = {
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
     * 是否开启吸底模式
     * 默认值：`false`
     */
    fixed: PropTypes.bool,

    /**
     * 是否开启迷你模式
     * 默认值：`false`
     */
    mini: PropTypes.bool,

    /**
     * 音频是否自动播放
     * 默认值：`false`
     */
    autoplay: PropTypes.bool,

    /**
     * 设置主题色
     * 默认值：`'#b7daff'`
     */
    theme: PropTypes.string,

    /**
     * 设置音频循环播放, 可选值: `'all'`、`'one'`、`'none'`
     * 默认值：`'all'`
     */
    loop: PropTypes.oneOf(['all', 'one', 'none']),

    /**
     * 设置音频循环顺序, 可选值: `'list'`、`'random'`
     * 默认值：`'list'`
     */
    order: PropTypes.oneOf(['list', 'random']),

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
         * 设置音频`lrc`歌词
         */
        lrc: PropTypes.string,
        /**
         * 设置切换到此音频时的主题色，比上面的`theme`优先级高
         */
        theme: PropTypes.string,
        /**
         * 设置音频类型，可选的有`'auto'`、`'hls'`、`'normal'`
         * 默认值：`'auto'`
         */
        type: PropTypes.oneOf(['auto', 'hls', 'normal'])
    })),

    /**
     * 是否互斥，阻止多个播放器同时播放，当前播放器播放时暂停其他播放器
     * 默认值：`true`
     */
    mutex: PropTypes.bool,

    /**
     * 有三种方式来给`APlayer`传递歌词，使用`lrcType`参数指明使用哪种方式，然后把歌词放到`audio.lrc`参数或者`HTML`里
     * `1`表示把歌词放到`JS`字符串里面，`2`表示把歌词放到`HTML`里面，`3`表示把歌词放到`LRC`文件里，音频播放时会加载对应的`LRC`文件
     * `audio.lrc`支持下面格式的歌词：
     * `[mm:ss]APlayer[mm:ss.xx]is`
     * `[mm:ss.xxx]amazing`
     * `[mm:ss.xx][mm:ss.xx]APlayer`
     * `[mm:ss.xx]<mm:ss.xx>is`
     * `[mm:ss.xx]amazing[mm:ss.xx]APlayer`
     */
    lrcType: PropTypes.oneOf([0, 1, 2, 3]),

    /**
     * 列表是否默认折叠
     * 默认值：`false`
     */
    listFolded: PropTypes.bool,

    /**
     * 设置列表最大高度
     */
    listMaxHeight: PropTypes.number,

    /**
     * 存储播放器设置的`localStorage key`
     * 默认值：`'aplayer-setting'`
     */
    storageName: PropTypes.string,

    /**
     * 播放音频，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    play: PropTypes.bool,

    /**
     * 暂停音频，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    pause: PropTypes.bool,

    /**
     * 跳转到特定时间，时间的单位为秒，每次`isSeek`设置为`true`后执行完相应操作后会自动置为`false`
     */
    seek: PropTypes.exact({
        /**
         * 是否跳转到特定时间
         */
        isSeek: PropTypes.bool,
        /**
         * 跳转到的时间
         */
        time: PropTypes.number,
    }),

    /**
     * 切换到上一首音频，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    skipBack: PropTypes.bool,

    /**
     * 切换到下一首音频，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    skipForward: PropTypes.bool,

    /**
     * 显示歌词，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    showLrc: PropTypes.bool,

    /**
     * 隐藏歌词，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    hideLrc: PropTypes.bool,

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
     * 显示播放列表，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    showList: PropTypes.bool,

    /**
     * 隐藏播放列表，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    hideList: PropTypes.bool,

    /**
     * 增加音频到播放列表，每次`isAdd`设置为`true`后执行完相应操作后会自动置为`false`
     */
    addList: PropTypes.exact({
        /**
         * 是否增加音频到播放列表
         */
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
             * 设置音频`lrc`歌词
             */
            lrc: PropTypes.string,
            /**
             * 设置切换到此音频时的主题色，比上面的`theme`优先级高
             */
            theme: PropTypes.string,
            /**
             * 设置音频类型，可选的有`'auto'`、`'hls'`、`'normal'`
             * 默认值：`'auto'`
             */
            type: PropTypes.oneOf(['auto', 'hls', 'normal'])
        })),
    }),

    /**
     * 删除播放列表中的音频，每次`isRemove`设置为`true`后执行完相应操作后会自动置为`false`
     */
    removeList: PropTypes.exact({
        /**
         * 是否删除播放列表中的音频
         */
        isRemove: PropTypes.bool,
        /**
         * 音频索引
         */
        index: PropTypes.number,
    }),

    /**
     * 切换播放列表，每次`isSwitch`设置为`true`后执行完相应操作后会自动置为`false`
     */
    switchList: PropTypes.exact({
        /**
         * 是否切换播放列表
         */
        isSwitch: PropTypes.bool,
        /**
         * 音频索引
         */
        index: PropTypes.number,
    }),

    /**
     * 清空播放列表，每次设置为`true`后执行完相应操作后会自动置为`false`
     */
    clearList: PropTypes.bool,

    /**
     * 销毁播放器，每次设置为`true`后执行完相应操作后会自动置为`false`
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

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyAPlayer;

export const propTypes = FefferyAPlayer.propTypes;
export const defaultProps = FefferyAPlayer.defaultProps;