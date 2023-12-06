import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyShortcutPanel = React.lazy(() => import(/* webpackChunkName: "feffery_shortcut_panel" */ '../fragments/FefferyShortcutPanel.react'));

const FefferyShortcutPanel = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyShortcutPanel {...props} />
        </Suspense>
    );
}

// 定义参数或属性
FefferyShortcutPanel.propTypes = {
    /**
     * 部件id
     */
    id: PropTypes.string,

    /**
     * 设置语言，可选的有'en'、'zh'，默认为'zh'
     */
    locale: PropTypes.oneOf(['en', 'zh']),

    /**用于定义热键节点的数据结构
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
             * 用于定义当前热键的唯一id，会在顶端热键面包屑中进行显示
             */
            id: PropTypes.string.isRequired,

            /**
             * 用于定义当前热键的标题信息
             */
            title: PropTypes.string.isRequired,

            /**
             * 用于定义当前热键对应的快捷键方式
             */
            hotkey: PropTypes.string,

            /**
             * 用于传入字符型的js函数体源码，作为当前热键被触发时的行为
             */
            handler: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.func
            ]),

            /**
             * 用于设置当前热键上一层级节点的id信息
             */
            parent: PropTypes.string,

            /**
             * 用于设置当前热键被搜索时对应的关键词
             */
            keywords: PropTypes.string,

            /**
             * 用于设置当前热键节点下一层级对应的节点id信息数组
             */
            children: PropTypes.arrayOf(PropTypes.string),

            /**
             * 用于设置分组标题文字
             */
            section: PropTypes.string
        })
    ).isRequired,

    /**
     * 监听记录最近一次被触发的热键id以及对应触发时间的时间戳信息
     */
    triggeredHotkey: PropTypes.exact({
        /**
         * 触发指令菜单项id
         */
        id: PropTypes.string,
        /**
         * 触发时间戳信息
         */
        timestamp: PropTypes.number
    }),

    /**
     * 定义输入框提示内容，默认会根据locale赋以不同的缺省值
     */
    placeholder: PropTypes.string,

    /**
     * 设置唤出指令面板的快捷键组合，默认为'cmd+k,ctrl+k'
     */
    openHotkey: PropTypes.string,

    /**
     * 设置主题，可选的有'light'、'dark'，默认为'light'
     */
    theme: PropTypes.oneOf(['light', 'dark']),

    /**
     * 传入true时手动展开指令面板，默认为false
     */
    open: PropTypes.bool,

    /**
     * 传入true时手动关闭指令面板，默认为false
     */
    close: PropTypes.bool,

    /**
     * 用于配置指令面板相关样式参数
     */
    panelStyles: PropTypes.exact({
        /**
         * 设置面板宽度，默认为'640px'
         */
        width: PropTypes.string,
        /**
         * 设置面板选项滚动区背景色，默认为'rgba(255, 255, 255, 0.5)'
         */
        overflowBackground: PropTypes.string,
        /**
         * 设置面板字体颜色，默认为'rgb(60, 65, 73)'
         */
        textColor: PropTypes.string,
        /**
         * 设置面板字体大小，默认为'16px'
         */
        fontSize: PropTypes.string,
        /**
         * 设置面板距离顶端距离，默认为'20%'
         */
        top: PropTypes.string,
        /**
         * 设置面板主色，默认为'rgb(110, 94, 210)'
         */
        accentColor: PropTypes.string,
        /**
         * 设置面板次要背景色，默认为'rgb(239, 241, 244)'
         */
        secondaryBackgroundColor: PropTypes.string,
        /**
         * 设置面板次要文字颜色，默认为'rgb(107, 111, 118)'
         */
        secondaryTextColor: PropTypes.string,
        /**
         * 设置面板选中项背景色，默认为'rgb(248, 249, 251)'
         */
        selectedBackground: PropTypes.string,
        /**
         * 设置面板选项区高度，默认为'300px'
         */
        actionsHeight: PropTypes.string,
        /**
         * 设置面板分组标签文字颜色，默认为'rgb(144, 149, 157)'
         */
        groupTextColor: PropTypes.string,
        /**
         * 设置面板的z-index信息，默认为1
         */
        zIndex: PropTypes.number
    }),

    /**
     * 用于监听用户当前已输入搜索内容
     */
    searchValue: PropTypes.string,

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
    setProps: PropTypes.func
};

// 设置默认参数
FefferyShortcutPanel.defaultProps = {
    locale: 'zh',
    theme: 'light',
    openHotkey: 'cmd+k,ctrl+k',
    open: false,
    close: false
}

export default FefferyShortcutPanel;

export const propTypes = FefferyShortcutPanel.propTypes;
export const defaultProps = FefferyShortcutPanel.defaultProps;