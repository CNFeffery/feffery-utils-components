import React, { useState, useRef, useEffect } from 'react';
import "ninja-keys";
import './styles.css'

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


const footerHtmlCn = <div className="modal-footer" slot="footer">
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


// 定义快捷方式面板部件FefferyShortcutPanel，api参数参考https://github.com/ssleptsov/ninja-keys
const FefferyShortcutPanel = (props) => {
    // 取得必要属性或参数
    let {
        id,
        style,
        data,
        placeholder,
        disableHotkeys,
        openHotkey,
        hotKeysJoinedView,
        theme,
        locale,
        setProps,
    } = props;

    data = data || [
        {
            id: "Home",
            title: "Open Home",
            hotkey: "cmd+h",
            handler: () => {
                console.log("navigation to home");
            }
        },
        {
            id: "Open Projects",
            title: "Open Projects",
            hotkey: "cmd+p",
            handler: () => {
                console.log("navigation to projects");
            }
        },
        {
            id: "Theme",
            title: "Change theme...",
            children: [
                'Light Theme', 'Dark Theme'
            ]
        },
        {
            id: "Light Theme",
            title: "Change theme to Light",
            parent: 'Theme',
            handler: () => {
                console.log("theme light");
            }
        },
        {
            id: "Dark Theme",
            title: "Change theme to Dark",
            parent: 'Theme',
            keywords: "lol",
            handler: () => {
                console.log("theme dark");
            }
        }
    ]

    // 填充handler缺省时的默认逻辑
    data = data.map(
        item => {
            return typeof item.handler === typeof '' || item.hasOwnProperty('children') ?
                item : {
                    ...item,
                    ...{
                        handler: () => {
                            setProps({
                                triggeredHotkey: item.id + ' ' + Date.parse(new Date()).toString()
                            })
                        }
                    }
                }
        }
    )

    const ninjaKeys = useRef(null);
    const [hotkeys, setHotkeys] = useState(
        data.map(
            item => typeof item.handler === typeof '' ?
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

    // 返回向页面注入的快捷键监听
    return (
        <ninja-keys id={id}
            class={theme || 'light'}
            style={style}
            ref={ninjaKeys}
            placeholder={placeholder}
            disableHotkeys={disableHotkeys}
            openHotkey={openHotkey}
            hotKeysJoinedView={true}
            hideBreadcrumbs={true} >
            {locale === 'en' ? footerHtmlEn : footerHtmlCn}
        </ ninja-keys>
    );
}

// 定义参数或属性
FefferyShortcutPanel.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置语言，可选的有'en'、'cn'
    locale: PropTypes.oneOf(['en', 'cn']),

    // 用于定义热键节点的数据结构
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
    ),

    // 监听记录最近一次被触发的热键id以及对应触发时间的秒级时间戳信息
    triggeredHotkey: PropTypes.oneOfType([
        PropTypes.string
    ]),

    // 定义输入框提示内容
    placeholder: PropTypes.string,

    // 设置是否禁用热键，默认为false
    disableHotkeys: PropTypes.bool,

    // 设置唤出指令面板的快捷键组合，默认为'cmd+k,ctrl+k'
    openHotkey: PropTypes.string,

    // 设置主题，可选的有'light'、'dark'
    theme: PropTypes.oneOf(['light', 'dark']),

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
    locale: 'cn',
    theme: 'light'
}

export default FefferyShortcutPanel;