import { useEffect } from 'react';
import { createPortal } from 'react-dom';
import PropTypes from 'prop-types';

/**
 * 传送门组件FefferyPortal
 */
const FefferyPortal = (props) => {
    const {
        id,
        key,
        children,
        targetSelector,
        setProps,
        loading_state
    } = props;

    if (children && targetSelector) {
        return createPortal(children, document.querySelector(targetSelector));
    }
    return <></>;
}

FefferyPortal.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 辅助强制刷新用
     */
    key: PropTypes.string,

    /**
     * 需要传送的子元素
     */
    children: PropTypes.node,

    /**
     * 传送目标对应的css选择器
     */
    targetSelector: PropTypes.string,

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
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyPortal.defaultProps = {
}

export default FefferyPortal;