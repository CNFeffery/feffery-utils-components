// react核心
import PropTypes from 'prop-types';
// 组件核心
import SlFormatNumber from '@shoelace-style/shoelace/dist/react/format-number';

/**
 * 数值格式化组件FefferyFormatNumber
 */
const FefferyFormatNumber = ({
    id,
    style,
    className,
    value = 0,
    type = 'decimal',
    noGrouping = false,
    minimumFractionDigits,
    maximumFractionDigits,
    setProps
}) => {

    return <SlFormatNumber id={id}
        style={style}
        className={className}
        value={value}
        type={type}
        noGrouping={noGrouping}
        minimumFractionDigits={minimumFractionDigits}
        maximumFractionDigits={maximumFractionDigits} />;
}

FefferyFormatNumber.propTypes = {
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
     * 格式化类型，可选项有`'decimal'`、`'percent'`
     * 默认值：`'decimal'`
     */
    type: PropTypes.oneOf(['decimal', 'percent']),

    /**
     * 是否关闭千分位符
     * 默认值：`false`
     */
    noGrouping: PropTypes.bool,

    /**
     * 最小小数位数
     */
    minimumFractionDigits: PropTypes.number,

    /**
     * 最大小数位数
     */
    maximumFractionDigits: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyFormatNumber;