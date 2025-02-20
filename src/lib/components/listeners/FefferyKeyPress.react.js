// react核心
import PropTypes from 'prop-types';
// 组件核心
import { useKeyPress } from 'ahooks';

/**
 * 按键事件监听组件FefferyKeyPress
 */
const FefferyKeyPress = ({
    keys,
    pressedCounts = 0,
    setProps
}) => {

    useKeyPress(
        keys,
        (e) => {
            e.preventDefault() // 阻止浏览器默认行为
            setProps({
                pressedCounts: pressedCounts + 1
            })
        }
    );

    return <></>;
}

FefferyKeyPress.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 必填，用于设置要监听的按键组合
     */
    keys: PropTypes.string.isRequired,

    /**
     * 记录设置的按键或按键组合事件已被触发的次数
     * 默认值：`0`
     */
    pressedCounts: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyKeyPress;