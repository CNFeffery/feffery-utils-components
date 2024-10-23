import PropTypes from 'prop-types';

/**
 * 动态样式组件FefferyStyle
 */
const FefferyStyle = (props) => {

    const {
        id,
        key,
        rawStyle,
        setProps,
        loading_state
    } = props;

    return (<style
        jsx="true"
        id={id}
        key={key}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >{rawStyle}</style>);
}

FefferyStyle.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置要添加到文档中的原生`css`字符
     */
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