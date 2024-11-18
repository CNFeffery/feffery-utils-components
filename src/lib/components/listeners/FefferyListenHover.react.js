// react核心
import PropTypes from 'prop-types';
// 组件核心
import { useHover } from 'ahooks';

/**
 * 鼠标悬停监听组件FefferyListenHover
 */
const FefferyListenHover = (props) => {
    const {
        targetSelector,
        setProps,
        loading_state
    } = props;

    useHover(
        () => document.querySelector(targetSelector),
        {
            onChange: (e) => {
                setProps({
                    isHovering: e
                })
            }
        }
    )

    return <></>;
}

FefferyListenHover.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 必填，监听目标选择器字符串
     */
    targetSelector: PropTypes.string.isRequired,

    /**
     * 监听目标元素是否处于鼠标悬停状态
     */
    isHovering: PropTypes.bool,

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

FefferyListenHover.defaultProps = {
}

export default FefferyListenHover;