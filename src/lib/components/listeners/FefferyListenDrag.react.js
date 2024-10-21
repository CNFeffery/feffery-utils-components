// react核心
import PropTypes from 'prop-types';
// 组件核心
import { useDrag } from 'ahooks';

/**
 * 拖拽事件监听组件FefferyListenDrag
 */
const FefferyListenDrag = (props) => {
    const {
        targetSelector,
        data,
        isDragging,
        setProps,
        loading_state
    } = props;

    useDrag(
        data,
        () => document.querySelector(targetSelector),
        {
            onDragStart: (e) => {
                setProps({
                    isDragging: true
                })
            },
            onDragEnd: (e) => {
                setProps({
                    isDragging: false
                })
            }
        }
    )

    return <></>;
}

FefferyListenDrag.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 拖拽事件监听目标选择器规则字符串
     */
    targetSelector: PropTypes.string,

    /**
     * 当前监听目标所携带的数据，配合**FefferyListenDrop**使用
     */
    data: PropTypes.any,

    /**
     * 监听目标是否处于拖拽中状态
     */
    isDragging: PropTypes.bool,

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

FefferyListenDrag.defaultProps = {
}

export default FefferyListenDrag;