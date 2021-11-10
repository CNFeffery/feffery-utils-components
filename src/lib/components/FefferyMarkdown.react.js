import React, { useState } from 'react';
import PropTypes from 'prop-types';
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import remarkMath from 'remark-math'
import rehypeKatex from 'rehype-katex'
import rehypeRaw from 'rehype-raw'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { CopyToClipboard } from "react-copy-to-clipboard";
import { AiOutlineCheck, AiOutlineCopy } from "react-icons/ai";
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
    twilight
} from 'react-syntax-highlighter/dist/esm/styles/prism';

import 'katex/dist/katex.min.css'
import 'github-markdown-css'
import './styles.css'


// 定义markdown渲染组件FefferyMarkdown，api参数参考https://github.com/remarkjs/react-markdown
const FefferyMarkdown = (props) => {
    // 取得必要属性或参数
    let {
        id,
        markdownStr,
        codeStyle,
        renderHtml,
        linkTarget,
        setProps
    } = props;

    const str2style = new Map([
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
        ['twilight', twilight]
    ])

    return (
        <div className='markdown-body' style={{ marginBottom: '10px' }}>
            <ReactMarkdown id={id}
                linkTarget={linkTarget}
                remarkPlugins={[remarkGfm, remarkMath]}
                rehypePlugins={renderHtml ? [rehypeRaw, rehypeKatex] : [rehypeKatex]}
                components={{
                    code: ({ node, inline, className, children, ...props }) => {
                        const [isCopied, setIsCopied] = useState(false);
                        const match = /language-(\w+)/.exec(className || '')
                        return !inline && match ? (
                            <div style={{ position: 'relative' }}>
                                <CopyToClipboard
                                    onCopy={() => {
                                        setIsCopied(true);
                                        setTimeout(() => setIsCopied(false), 1500);
                                    }}
                                    style={
                                        {
                                            position: 'absolute',
                                            right: '5px',
                                            top: '5px',
                                            padding: '6px',
                                            margin: 0,
                                            background: 'transparent',
                                            border: 'none transparent',
                                            cursor: 'pointer',
                                            zIndex: 999
                                        }
                                    }
                                    text={String(children).replace(/\n$/, '')}
                                >
                                    <button type="button" aria-label="Copy to Clipboard Button">
                                        {isCopied ? <AiOutlineCheck style={{ color: 'rgb(91, 199, 38)', fontSize: '18px' }} />
                                            : <AiOutlineCopy style={{ color: 'rgb(24, 144, 255)', fontSize: '18px' }} />}
                                    </button>
                                </CopyToClipboard>
                                <SyntaxHighlighter
                                    children={String(children).replace(/\n$/, '')}
                                    style={str2style.get(codeStyle)}
                                    showLineNumbers={true}
                                    language={match[1]}
                                    PreTag="div"
                                    {...props} />
                            </div>
                        ) : (
                            <code className={className} {...props}>
                                {children}
                            </code>
                        )
                    }
                }}>
                {markdownStr}
            </ReactMarkdown>
        </div>
    );
}

// 定义参数或属性
FefferyMarkdown.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置要渲染的原始markdown内容
    markdownStr: PropTypes.string,

    // 设置代码风格，默认为'coy-without-shadows'
    codeStyle: PropTypes.string,

    // 设置是否渲染markdown中的html源码，默认为false
    renderHtml: PropTypes.bool,

    // 设置markdown中链接的跳转方式，默认为'_blank'
    linkTarget: PropTypes.string,

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
FefferyMarkdown.defaultProps = {
    linkTarget: '_blank',
    codeStyle: 'coy-without-shadows'
}

export default FefferyMarkdown;