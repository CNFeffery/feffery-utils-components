import React, { useState } from 'react';
import PropTypes from 'prop-types';
import {
    CheckOutlined,
    CopyOutlined
} from '@ant-design/icons';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { CopyToClipboard } from "react-copy-to-clipboard";
import {
    a11yDark,
    atomDark,
    coldarkCold,
    coldarkDark,
    coy,
    coyWithoutShadows,
    darcula,
    dracula,
    nord,
    okaidia,
    prism,
    solarizedlight,
    twilight,
    duotoneSea,
    duotoneDark,
    duotoneLight,
    duotoneSpace,
    ghcolors,
    gruvboxDark,
    materialDark,
    nightOwl,
    oneLight,
    pojoaque,
    solarizedDarkAtom,
    synthwave84,
    zTouch
} from 'react-syntax-highlighter/dist/esm/styles/prism';

import './styles.css'

const str2theme = new Map([
    ['a11y-dark', a11yDark],
    ['atom-dark', atomDark],
    ['coldark-cold', coldarkCold],
    ['coldark-dark', coldarkDark],
    ['coy', coy],
    ['coy-without-shadows', coyWithoutShadows],
    ['darcula', darcula],
    ['dracula', dracula],
    ['nord', nord],
    ['okaidia', okaidia],
    ['prism', prism],
    ['solarizedlight', solarizedlight],
    ['twilight', twilight],
    ['duotone-sea', duotoneSea],
    ['duotone-dark', duotoneDark],
    ['duotone-light', duotoneLight],
    ['duotone-space', duotoneSpace],
    ['gh-colors', ghcolors],
    ['gruvbox-dark', gruvboxDark],
    ['material-dark', materialDark],
    ['night-owl', nightOwl],
    ['one-light', oneLight],
    ['pojoaque', pojoaque],
    ['solarized-dark-atom', solarizedDarkAtom],
    ['synthwave84', synthwave84],
    ['z-touch', zTouch]
])

// 定义代码语法高亮组件FefferySyntaxHighlighter，api参数参考https://github.com/react-syntax-highlighter/react-syntax-highlighter
const FefferySyntaxHighlighter = (props) => {
    // 取得必要属性或参数
    let {
        id,
        codeTheme,
        codeBlockStyle,
        codeStyle,
        showLineNumbers,
        setProps
    } = props;

    const [isCopied, setIsCopied] = useState(false);

    codeTheme = codeTheme || 'gh-colors'
    let currentCodeStyle = str2theme.get(codeTheme)
    if (codeTheme === 'gh-colors') {
        currentCodeStyle = {
            ...currentCodeStyle,
            'pre[class*="language-"]': {
                ...currentCodeStyle['pre[class*="language-"]'],
                'background': '#f6f8fa'
            }
        }
    }

    currentCodeStyle = {
        ...currentCodeStyle,
        'pre[class*="language-"]': {
            ...currentCodeStyle['pre[class*="language-"]'],
            'borderRadius': '5px',
            ...codeBlockStyle
        },
        'code[class*="language-"]': {
            ...currentCodeStyle['code[class*="language-"]'],
            'fontSize': '14px',
            ...codeStyle
        }
    }

    return (
        <div id={id} style={{ position: 'relative' }}>
            <CopyToClipboard
                onCopy={() => {
                    setIsCopied(true);
                    setTimeout(() => setIsCopied(false), 1500);
                }}
                style={
                    {
                        position: 'absolute',
                        right: '9px',
                        top: '7px',
                        padding: '4px',
                        margin: 0,
                        background: 'transparent',
                        border: '1px solid rgba(27,31,36,0.15)',
                        cursor: 'pointer',
                        zIndex: 999,
                        borderRadius: '5px',
                        lineHeight: '16px',
                    }
                }
                text={String(children).replace(/\n$/, '')}
            >
                <button
                    type="button"
                    aria-label="Copy to Clipboard Button"
                    className={'copy-to-clipboard-button'}
                >
                    {isCopied ? <CheckOutlined style={{ color: 'rgb(91, 199, 38)', fontSize: '16px' }} />
                        : <CopyOutlined style={{ color: '#57606a', fontSize: '16px' }} />}
                </button>
            </CopyToClipboard>
            <SyntaxHighlighter
                children={String(children).replace(/\n$/, '')}
                style={currentCodeStyle}
                showLineNumbers={showLineNumbers}
                language={match[1]}
                PreTag="div"
                {...props} />
        </div>
    );
}

// 定义参数或属性
FefferySyntaxHighlighter.propTypes = {
    // id
    id: PropTypes.string,

    // 设置代码风格主题，默认为'gh-colors'
    codeTheme: PropTypes.oneOf([
        'a11y-dark', 'atom-dark', 'coldark-cold', 'coldark-dark', 'coy', 'coy-without-shadows', 'darcula', 'dracula',
        'nord', 'okaidia', 'prism', 'solarizedlight', 'twilight', 'duotone-sea', 'duotone-dark', 'duotone-light',
        'duotone-space', 'gh-colors', 'gruvbox-dark', 'material-dark', 'night-owl', 'one-light', 'pojoaque',
        'solarized-dark-atom', 'synthwave84', 'z-touch'
    ]),

    // 额外设置代码块容器css样式
    codeBlockStyle: PropTypes.object,

    // 额外设置代码内容css样式
    codeStyle: PropTypes.object,

    // 设置代码块是否显示行号，默认为true
    showLineNumbers: PropTypes.bool,

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
FefferySyntaxHighlighter.defaultProps = {
    codeTheme: 'gh-colors',
    showLineNumbers: true
}

export default FefferySyntaxHighlighter;