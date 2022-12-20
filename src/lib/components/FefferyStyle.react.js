import PropTypes from 'prop-types';

// 定义动态样式组件FefferyStyle
const FefferyStyle = (props) => {

    const {
        id,
        rawStyle,
        setProps,
        loading_state
    } = props;

    return (<style
        jsx="true"
        id={id}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >{rawStyle}</style>);
}

// 定义参数或属性
FefferyStyle.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置要添加到文档中的原生css字符
    rawStyle: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

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
FefferyStyle.defaultProps = {
}

export default FefferyStyle;