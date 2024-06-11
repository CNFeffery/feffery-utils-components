import { useHover } from 'ahooks';
import PropTypes from 'prop-types';

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
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用key值
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

// 设置默认参数
FefferyListenHover.defaultProps = {
}

export default FefferyListenHover;