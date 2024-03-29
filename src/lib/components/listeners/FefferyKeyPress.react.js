import { useKeyPress } from 'ahooks';
import PropTypes from 'prop-types';

// 定义按键事件监听组件FefferyKeyPress
const FefferyKeyPress = (props) => {
    const {
        keys,
        pressedCounts,
        setProps,
        loading_state
    } = props;

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

// 定义参数或属性
FefferyKeyPress.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 必填，用于设置要监听的按键组合
     */
    keys: PropTypes.string.isRequired,

    /**
     * 记录设置的按键或按键组合事件已被触发的次数
     * 默认：0
     */
    pressedCounts: PropTypes.number,

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
FefferyKeyPress.defaultProps = {
    pressedCounts: 0
}

export default FefferyKeyPress;