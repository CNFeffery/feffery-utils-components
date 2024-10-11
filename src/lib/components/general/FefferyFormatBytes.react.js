import PropTypes from 'prop-types';
import SlFormatBytes from '@shoelace-style/shoelace/dist/react/format-bytes';

/**
 * 字节格式化组件FefferyFormatBytes
 */
const FefferyFormatBytes = (props) => {
    const {
        id,
        style,
        className,
        value,
        unit,
        display,
        setProps,
        loading_state
    } = props;

    return <SlFormatBytes id={id}
        style={style}
        className={className}
        value={value}
        unit={unit}
        display={display} />;
}

FefferyFormatBytes.propTypes = {
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
    className: PropTypes.string,

    /**
     * 待格式化的原始字节数值
     * 默认值：`0`
     */
    value: PropTypes.number,

    /**
     * 展示单位，可选项有`'byte'`、`'bit'`
     * 默认值：`'byte'`
     */
    unit: PropTypes.oneOf(['byte', 'bit']),

    /**
     * 展示类型，可选项有`'long'`、`'short'`、`'narrow'`
     * 默认值：`'short'`
     */
    display: PropTypes.oneOf(['long', 'short', 'narrow']),

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

FefferyFormatBytes.defaultProps = {
    value: 0,
    unit: 'byte',
    display: 'short'
}

export default FefferyFormatBytes;