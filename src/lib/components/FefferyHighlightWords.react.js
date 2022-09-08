import Highlighter from "react-highlight-words";
import PropTypes from 'prop-types';
import './styles.css';

// 定义关键词高亮组件FefferyHighlightWords，文档参考：https://github.com/bvaughn/react-highlight-words#readme
const FefferyHighlightWords = (props) => {
    // 取得必要属性或参数
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

// 定义参数或属性
FefferyHighlightWords.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置是否大小写敏感，默认为false
    caseSensitive: PropTypes.bool,

    // 设置高亮部分的css样式类，默认为'feffery-highlight-words-highlight'
    highlightClassName: PropTypes.string,

    // 设置高亮部分的css样式
    highlightStyle: PropTypes.object,

    // 设置是否开启正则表达式模式，默认为false
    useRegex: PropTypes.bool,

    // 设置要进行高亮的字符（或正则模式数组），当useRegex为true时会视作正则模式数组
    searchWords: PropTypes.arrayOf(PropTypes.string),

    // 设置文本内容字符串
    textToHighlight: PropTypes.string,

    // 设置非高亮部分的css样式类
    unhighlightClassName: PropTypes.string,

    // 设置非高亮部分的css样式
    unhighlightStyle: PropTypes.object,

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

// 设置默认参数
FefferyHighlightWords.defaultProps = {
    caseSensitive: false,
    useRegex: false,
    highlightClassName: 'feffery-highlight-words-highlight'
}

export default FefferyHighlightWords;