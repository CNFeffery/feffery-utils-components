import React, { useRef, useEffect } from 'react';
import { propTypes, defaultProps } from '../../components/other/FefferyShortcutPanel.react';
import { isString } from 'lodash';
import "ninja-keys";
import FefferyStyle from '../../components/styleControl/FefferyStyle.react';

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
        panelStyles,
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

    useEffect(() => {
        if (ninjaKeys.current) {
            ninjaKeys.current.addEventListener("change", (event) => {
                setProps({
                    searchValue: event.detail.search
                })
            });
        }
    }, []);

    useEffect(() => {
        if (ninjaKeys.current) {
            ninjaKeys.current.data = data.map(
                item => isString(item.handler) ?
                    {
                        ...item,
                        ...{
                            handler: eval(item.handler)
                        }
                    } : item
            );
        }
    }, [data]);

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

    panelStyles = {
        ...{
            width: '640px',
            overflowBackground: 'rgba(255, 255, 255, 0.5)',
            textColor: 'rgb(60, 65, 73)',
            fontSize: '16px',
            top: '20%',
            accentColor: 'rgb(110, 94, 210)',
            secondaryBackgroundColor: 'rgb(239, 241, 244)',
            secondaryTextColor: 'rgb(107, 111, 118)',
            selectedBackground: 'rgb(248, 249, 251)',
            actionsHeight: '300px',
            groupTextColor: 'rgb(144, 149, 157)',
            zIndex: 1
        },
        ...panelStyles
    }

    // 返回向页面注入的快捷键监听
    return (
        <>
            <FefferyStyle
                rawStyle={
                    `
ninja-keys {
    --ninja-width: ${panelStyles.width};
    --ninja-overflow-background: ${panelStyles.overflowBackground};
    --ninja-text-color: ${panelStyles.textColor};
    --ninja-font-size: ${panelStyles.fontSize};
    --ninja-top: ${panelStyles.top};
    --ninja-accent-color: ${panelStyles.accentColor};
    --ninja-secondary-background-color: ${panelStyles.secondaryBackgroundColor};
    --ninja-secondary-text-color: ${panelStyles.secondaryTextColor};
    --ninja-selected-background: ${panelStyles.selectedBackground};
    --ninja-actions-height: ${panelStyles.actionsHeight};
    --ninja-group-text-color: ${panelStyles.groupTextColor};
    --ninja-z-index: ${panelStyles.zIndex};
}
`
                }
            />
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
        </>
    );
}

export default FefferyShortcutPanel;

FefferyShortcutPanel.defaultProps = defaultProps;
FefferyShortcutPanel.propTypes = propTypes;