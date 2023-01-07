import React, { useState, useRef, useEffect } from 'react';
import PropTypes from 'prop-types';
import { isString } from 'lodash';
import "ninja-keys";

const footerHtmlEn = <div class="modal-footer" slot="footer">
    <span class="help">
        <span className="ninja-examplekey esc">enter</span>
        to select
    </span>
    <span className="help">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            className="ninja-examplekey"
            viewBox="0 0 24 24"
        >
            <path d="M0 0h24v24H0V0z" fill="none" />
            <path
                d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"
            />
        </svg>
        <svg
            xmlns="http://www.w3.org/2000/svg"
            className="ninja-examplekey"
            viewBox="0 0 24 24"
        >
            <path d="M0 0h24v24H0V0z" fill="none" />
            <path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z" />
        </svg>
        to navigate
    </span>
    <span className="help">
        <span className="ninja-examplekey esc">esc</span>
        to close
    </span>
    <span className="help">
        <span className="ninja-examplekey esc">backspace</span>
        move to parent
    </span>
</div>


const footerHtmlZh = <div className="modal-footer" slot="footer">
    <span className="help">
        <span className="ninja-examplekey esc">enter</span>
        选择
    </span>
    <span className="help">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            className="ninja-examplekey"
            viewBox="0 0 24 24"
        >
            <path d="M0 0h24v24H0V0z" fill="none" />
            <path
                d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"
            />
        </svg>
        <svg
            xmlns="http://www.w3.org/2000/svg"
            className="ninja-examplekey"
            viewBox="0 0 24 24"
        >
            <path d="M0 0h24v24H0V0z" fill="none" />
            <path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z" />
        </svg>
        上下切换
    </span>
    <span className="help">
        <span className="ninja-examplekey esc">esc</span>
        关闭面板
    </span>
    <span className="help">
        <span className="ninja-examplekey esc">backspace</span>
        回到上一级
    </span>
</div>

const locale2footer = new Map([
    ['en', footerHtmlEn],
    ['zh', footerHtmlZh]
])

const locale2placeholder = new Map([
    ['en', 'Type a command or search...'],
    ['zh', '输入指令或进行搜索...']
])

// 定义快捷方式面板部件FefferyShortcutPanel，api参数参考https://github.com/ssleptsov/ninja-keys
const FefferyShortcutPanel = (props) => {
    // 取得必要属性或参数
    let {
        id,
        data,
        placeholder,
        openHotkey,
        theme,
        locale,
        open,
        close,
        setProps,
        loading_state
    } = props;

    // 填充handler缺省时的默认逻辑
    data = data.map(
        item => {
            return isString(item.handler) || item.hasOwnProperty('children') ?
                item : {
                    ...item,
                    ...{
                        handler: () => {
                            setProps({
                                triggeredHotkey: {
                                    id: item.id,
                                    timestamp: Date.parse(new Date())
                                }
                            })
                        }
                    }
                }
        }
    )

    const ninjaKeys = useRef(null);
    const [hotkeys, setHotkeys] = useState(
        data.map(
            item => isString(item.handler) ?
                {
                    ...item,
                    ...{
                        handler: eval(item.handler)
                    }
                } : item
        )
    );

    useEffect(() => {
        if (ninjaKeys.current) {
            ninjaKeys.current.data = hotkeys;
        }
    }, []);

    // 自主控制指令面板打开/关闭
    useEffect(() => {
        if (ninjaKeys.current && open) {
            ninjaKeys.current.open()
            // 重置
            setProps({
                open: false
            })
        }
    }, [open])

    useEffect(() => {
        if (ninjaKeys.current && close) {
            ninjaKeys.current.close()
            // 重置
            setProps({
                close: false
            })
        }
    }, [close])

    // 返回向页面注入的快捷键监听
    return (
        <ninja-keys id={id}
            class={theme}
            ref={ninjaKeys}
            placeholder={placeholder || locale2placeholder.get(locale)}
            openHotkey={openHotkey}
            hotKeysJoinedView={true}
            hideBreadcrumbs={true}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } >
            {locale2footer.get(locale)}
        </ ninja-keys>
    );
}

// 定义参数或属性
FefferyShortcutPanel.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置语言，可选的有'en'、'zh'，默认为'zh'
    locale: PropTypes.oneOf(['en', 'zh']),

    // 用于定义热键节点的数据结构
    // 例：
    // [
    //     {
    //         id: "Home",
    //         title: "Open Home",
    //         hotkey: "cmd+h",
    //         handler: () => {
    //             console.log("navigation to home");
    //         }
    //     },
    //     {
    //         id: "Open Projects",
    //         title: "Open Projects",
    //         hotkey: "cmd+p",
    //         handler: () => {
    //             console.log("navigation to projects");
    //         }
    //     },
    //     {
    //         id: "Theme",
    //         title: "Change theme...",
    //         children: [
    //             'Light Theme', 'Dark Theme'
    //         ]
    //     },
    //     {
    //         id: "Light Theme",
    //         title: "Change theme to Light",
    //         parent: 'Theme',
    //         handler: () => {
    //             console.log("theme light");
    //         }
    //     },
    //     {
    //         id: "Dark Theme",
    //         title: "Change theme to Dark",
    //         parent: 'Theme',
    //         keywords: "lol",
    //         handler: () => {
    //             console.log("theme dark");
    //         }
    //     }
    // ]
    data: PropTypes.arrayOf(
        PropTypes.exact({
            // 用于定义当前热键的唯一id，会在顶端热键面包屑中进行显示
            id: PropTypes.string.isRequired,

            // 用于定义当前热键的标题信息
            title: PropTypes.string.isRequired,

            // 用于定义当前热键对应的快捷键方式
            hotkey: PropTypes.string,

            // 用于传入字符型的js函数体源码，作为当前热键被触发时的行为
            handler: PropTypes.oneOfType([
                PropTypes.string,
                PropTypes.func
            ]),

            // 用于设置当前热键上一层级节点的id信息
            parent: PropTypes.string,

            // 用于设置当前热键被搜索时对应的关键词
            keywords: PropTypes.string,

            // 用于设置当前热键节点下一层级对应的节点id信息数组
            children: PropTypes.arrayOf(PropTypes.string),

            // 用于设置分组标题文字
            section: PropTypes.string
        })
    ).isRequired,

    // 监听记录最近一次被触发的热键id以及对应触发时间的时间戳信息
    triggeredHotkey: PropTypes.exact({
        // 触发指令菜单项id
        id: PropTypes.string,
        // 触发时间戳信息
        timestamp: PropTypes.number
    }),

    // 定义输入框提示内容，默认会根据locale赋以不同的缺省值
    placeholder: PropTypes.string,

    // 设置唤出指令面板的快捷键组合，默认为'cmd+k,ctrl+k'
    openHotkey: PropTypes.string,

    // 设置主题，可选的有'light'、'dark'，默认为'light'
    theme: PropTypes.oneOf(['light', 'dark']),

    // 传入true时手动展开指令面板，默认为false
    open: PropTypes.bool,

    // 传入true时手动关闭指令面板，默认为false
    close: PropTypes.bool,

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