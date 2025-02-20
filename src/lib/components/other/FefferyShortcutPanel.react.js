import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyShortcutPanel = React.lazy(() => import(/* webpackChunkName: "feffery_shortcut_panel" */ '../../fragments/other/FefferyShortcutPanel.react'));

/**
 * 快捷指令面板部件FefferyShortcutPanel
 */
const FefferyShortcutPanel = ({
    locale = 'zh',
    theme = 'light',
    openHotkey = 'cmd+k,ctrl+k',
    open = false,
    close = false,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyShortcutPanel {
                ...{
                    locale,
                    theme,
                    openHotkey,
                    open,
                    close,
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyShortcutPanel.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置语言，可选项有`'en'`、`'zh'`
     * 默认值：`'zh'`
     */
    locale: PropTypes.oneOf(['en', 'zh']),

    /**
     * 配置指令面板子项
     * 例：
     * [
     *      {
     *          id: "Home",
     *          title: "Open Home",
     *          hotkey: "cmd+h",
     *          handler: () => {
     *              console.log("navigation to home");
     *          }
     *      },
     *      {
     *          id: "Open Projects",
     *          title: "Open Projects",
     *          hotkey: "cmd+p",
     *          handler: () => {
     *              console.log("navigation to projects");
     *          }
     *      },
     *      {
     *          id: "Theme",
     *          title: "Change theme...",
     *          children: [
     *              'Light Theme', 'Dark Theme'
     *          ]
     *      },
     *      {
     *          id: "Light Theme",
     *          title: "Change theme to Light",
     *          parent: 'Theme',
     *          handler: () => {
     *              console.log("theme light");
     *          }
     *      },
     *      {
     *          id: "Dark Theme",
     *          title: "Change theme to Dark",
     *          parent: 'Theme',
     *          keywords: "lol",
     *          handler: () => {
     *              console.log("theme dark");
     *          }
     *      }
     *  ]
     */
    data: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 当前子项的唯一标识，会在顶端热键面包屑中进行显示
             */
            id: PropTypes.string.isRequired,

            /**
             * 必填，当前子项标题信息
             */
            title: PropTypes.string.isRequired,

            /**
             * 配置当前子项对应快捷键
             */
            hotkey: PropTypes.string,

            /**
             * 传入字符型的`javascript`函数体源码，在当前子项被激活时触发
             */
            handler: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.func
            ]),

            /**
             * 当前子项所属上一层级节点的`id`信息
             */
            parent: PropTypes.string,

            /**
             * 当前子项被搜索时对应的目标关键词
             */
            keywords: PropTypes.string,

            /**
             * 当前子项节点下一层级对应的节点`id`信息数组
             */
            children: PropTypes.arrayOf(PropTypes.string),

            /**
             * 分组标题文字
             */
            section: PropTypes.string
        })
    ).isRequired,

    /**
     * 监听记录最近一次被触发的子项`id`以及对应触发时间的时间戳信息
     */
    triggeredHotkey: PropTypes.exact({
        /**
         * 触发子项`id`
         */
        id: PropTypes.string,
        /**
         * 触发时间戳
         */
        timestamp: PropTypes.number
    }),

    /**
     * 定义输入框提示内容，默认会根据`locale`赋以不同的缺省值
     */
    placeholder: PropTypes.string,

    /**
     * 设置唤出指令面板的快捷键组合
     * 默认值：`'cmd+k,ctrl+k'`
     */
    openHotkey: PropTypes.string,

    /**
     * 设置主题，可选项有`'light'`、`'dark'`
     * 默认值：`'light'`
     */
    theme: PropTypes.oneOf(['light', 'dark']),

    /**
     * 更新为`true`时手动展开指令面板
     */
    open: PropTypes.bool,

    /**
     * 更新为`true`时手动关闭指令面板
     */
    close: PropTypes.bool,

    /**
     * 配置指令面板相关样式参数
     */
    panelStyles: PropTypes.exact({
        /**
         * 面板宽度
         * 默认值：`'640px'`
         */
        width: PropTypes.string,
        /**
         * 面板选项滚动区背景色
         * 默认值：`'rgba(255, 255, 255, 0.5)'`
         */
        overflowBackground: PropTypes.string,
        /**
         * 面板字体颜色
         * 默认值：`'rgb(60, 65, 73)'`
         */
        textColor: PropTypes.string,
        /**
         * 面板字体大小
         * 默认值：`'16px'`
         */
        fontSize: PropTypes.string,
        /**
         * 面板到顶端的距离
         * 默认值：`'20%'`
         */
        top: PropTypes.string,
        /**
         * 面板主色
         * 默认值：`'rgb(110, 94, 210)'`
         */
        accentColor: PropTypes.string,
        /**
         * 面板次要背景色
         * 默认值：`'rgb(239, 241, 244)'`
         */
        secondaryBackgroundColor: PropTypes.string,
        /**
         * 面板次要文字颜色
         * 默认值：`'rgb(107, 111, 118)'`
         */
        secondaryTextColor: PropTypes.string,
        /**
         * 面板选中项背景色
         * 默认值：`'rgb(248, 249, 251)'`
         */
        selectedBackground: PropTypes.string,
        /**
         * 面板选项区高度
         * 默认值：`'300px'`
         */
        actionsHeight: PropTypes.string,
        /**
         * 面板分组标签文字颜色
         * 默认值：`'rgb(144, 149, 157)'`
         */
        groupTextColor: PropTypes.string,
        /**
         * 面板`z-index`
         * 默认值：`1`
         */
        zIndex: PropTypes.number
    }),

    /**
     * 监听用户当前已输入搜索内容
     */
    searchValue: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyShortcutPanel;

export const propTypes = FefferyShortcutPanel.propTypes;
export const defaultProps = FefferyShortcutPanel.defaultProps;