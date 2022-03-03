import { Component } from 'react';
import { CirclePicker } from 'react-color';

// 定义circle型取色器FefferyCircleColorPicker
export default class FefferyCircleColorPicker extends Component {
    render() {
        // 取得必要属性或参数
        const {
            id,
            className,
            style,
            width,
            colors,
            circleSize,
            circleSpacing,
            color,
            setProps,
            loading_state
        } = this.props;

        return (
            <CirclePicker id={id}
                className={className}
                style={style}
                color={color}
                width={width}
                colors={colors}
                circleSize={circleSize}
                circleSpacing={circleSpacing}
                onChangeComplete={(c, event) => {
                    setProps({
                        color: c.hex
                    })
                }}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                } />
        );
    }
}


// 定义参数或属性
FefferyCircleColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置取色盘的宽度，默认为'252px'
    width: PropTypes.string,

    // 设置取色盘中供选择的色彩数组
    // 默认值为["#f44336", "#e91e63", "#9c27b0", "#673ab7", "#3f51b5", "#2196f3", "#03a9f4", "#00bcd4", "#009688", "#4caf50", "#8bc34a", "#cddc39", "#ffeb3b", "#ffc107", "#ff9800", "#ff5722", "#795548", "#607d8b"]
    colors: PropTypes.arrayOf(PropTypes.string),

    // 设取色盘中的圆形像素尺寸，默认为28
    circleSize: PropTypes.number,

    // 设置取色盘中圆形之间的间隔像素大小，默认为14
    circleSpacing: PropTypes.number,

    // 对应当前选中的颜色
    color: PropTypes.string,

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
}