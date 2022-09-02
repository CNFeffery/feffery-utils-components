import Wheel from '@uiw/react-color-wheel';
import { hsvaToHex, hexToHsva } from '@uiw/color-convert'
import PropTypes from 'prop-types';
import '../styles.css';

// 定义Wheel风格色彩选择器FefferyWheelColorPicker，文档参考：https://uiwjs.github.io/react-color/#/wheel
const FefferyWheelColorPicker = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        color,
        setProps,
        loading_state
    } = props;

    return (
        <Wheel id={id}
            className={className}
            style={style}
            color={color ? hexToHsva(color) : hexToHsva('#fffc51')}
            onChange={(c) => setProps({ color: hsvaToHex(c.hsva) })}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

// 定义参数或属性
FefferyWheelColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 对应当前选中的16进制色彩字符串
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
FefferyWheelColorPicker.defaultProps = {
    color: '#fffc51'
}

export default FefferyWheelColorPicker;