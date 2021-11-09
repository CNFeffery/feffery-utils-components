import React from 'react';
import PropTypes from 'prop-types';
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import remarkMath from 'remark-math'
import rehypeKatex from 'rehype-katex'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { coyWithoutShadows } from 'react-syntax-highlighter/dist/esm/styles/prism';

import 'katex/dist/katex.min.css'
import 'github-markdown-css'
import './styles.css'


// 定义markdown渲染组件FefferyMarkdown，api参数参考https://github.com/remarkjs/react-markdown
const FefferyMarkdown = (props) => {
    // 取得必要属性或参数
    let {
        id,
        markdownStr,
        skipHtml,
        linkTarget,
        setProps
    } = props;

    return (
        <div className='markdown-body' style={{ marginBottom: '10px' }}>
            <ReactMarkdown id={id}
                skipHtml={skipHtml}
                linkTarget={linkTarget}
                remarkPlugins={[remarkGfm, remarkMath]}
                rehypePlugins={[rehypeKatex]}
                components={{
                    code: ({ node, inline, className, children, ...props }) => {
                        const match = /language-(\w+)/.exec(className || '')
                        return !inline && match ? (
                            <SyntaxHighlighter
                                children={String(children).replace(/\n$/, '')}
                                style={coyWithoutShadows}
                                showLineNumbers={true}
                                language={match[1]}
                                PreTag="div"
                                {...props}
                            />
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

    // 设置是否忽略markdown中html源码的渲染，默认为false
    skipHtml: PropTypes.bool,

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
    linkTarget: '_blank'
}

export default FefferyMarkdown;