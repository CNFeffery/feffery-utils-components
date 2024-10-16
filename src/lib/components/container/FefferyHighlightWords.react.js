// react核心
import PropTypes from 'prop-types';
// 组件核心
import Highlighter from "react-highlight-words";

/**
 * 关键词高亮组件FefferyHighlightWords
 */
const FefferyHighlightWords = (props) => {
    const {
        id,
        className,
        style,
        caseSensitive,
        highlightClassName,
        highlightStyle,
        useRegex,
        searchWords,
        textToHighlight,
        unhighlightClassName,
        unhighlightStyle,
        setProps,
        loading_state
    } = props;

    return (
        <Highlighter id={id}
            className={className}
            style={style}
            caseSensitive={caseSensitive}
            highlightClassName={highlightClassName}
            highlightStyle={highlightStyle}
            searchWords={searchWords}
            textToHighlight={textToHighlight}
            unhighlightClassName={unhighlightClassName}
            unhighlightStyle={unhighlightStyle}
            autoEscape={!useRegex}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } >
            { }
        </Highlighter>
    );
}

FefferyHighlightWords.propTypes = {
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
     * 当前组件css类名
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 是否启用大小写敏感
     * 默认值：`false`
     */
    caseSensitive: PropTypes.bool,

    /**
     * 高亮部分元素css样式
     */
    highlightStyle: PropTypes.object,

    /**
     * 高亮部分元素css类名
     * 默认值：`'feffery-highlight-words-highlight'`
     */
    highlightClassName: PropTypes.string,

    /**
     * 是否开启正则表达式模式
     * 默认值：`false`
     */
    useRegex: PropTypes.bool,

    /**
     * 设置要进行高亮的目标字符或正则表达式数组
     */
    searchWords: PropTypes.arrayOf(PropTypes.string),

    /**
     * 原始文本内容
     */
    textToHighlight: PropTypes.string,

    /**
     * 非高亮部分元素css样式
     */
    unhighlightStyle: PropTypes.object,

    /**
     * 非高亮部分元素css类名
     */
    unhighlightClassName: PropTypes.string,

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
    })
};

FefferyHighlightWords.defaultProps = {
    caseSensitive: false,
    useRegex: false,
    highlightClassName: 'feffery-highlight-words-highlight'
}

export default FefferyHighlightWords;