// react核心
import PropTypes from 'prop-types';

/**
 * 动态样式组件FefferyStyle
 */
const FefferyStyle = ({
    id,
    key,
    rawStyle,
    setProps
}) => {
    return (<style jsx="true" id={id} key={key} >{rawStyle}</style>);
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
    setProps: PropTypes.func
};

export default FefferyStyle;