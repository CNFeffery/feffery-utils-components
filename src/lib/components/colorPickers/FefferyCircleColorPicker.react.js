import { CirclePicker } from 'react-color';
import PropTypes from 'prop-types';
import '../styles.css';

// 定义Circle风格色彩选择器FefferyBlockColorPicker，文档参考：https://casesandberg.github.io/react-color/
const FefferyCircleColorPicker = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        width,
        circleSize,
        circleSpacing,
        color,
        colors,
        setProps,
        loading_state
    } = props;

    return (
        <CirclePicker id={id}
            className={className}
            style={style}
            width={width}
            circleSize={circleSize}
            circleSpacing={circleSpacing}
            color={color}
            colors={colors}
            onChangeComplete={(c, e) => setProps({ color: c.hex })}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

// 定义参数或属性
FefferyCircleColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置组件整体宽度，默认为'252px'
    width: PropTypes.string,

    // 设置圆圈的像素尺寸，默认为28
    circleSize: PropTypes.number,

    // 设置圆圈之间的像素间隔大小，默认为14
    circleSpacing: PropTypes.number,

    // 对应当前选中的16进制色彩字符串
    color: PropTypes.string,

    // 设置可选的16进制色彩值数组，默认为["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]
    colors: PropTypes.arrayOf(PropTypes.string),

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
FefferyCircleColorPicker.defaultProps = {
    circleSpacing: 14,
    circleSize: 28,
    width: '252px',
    colors: ["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]
}

export default FefferyCircleColorPicker;