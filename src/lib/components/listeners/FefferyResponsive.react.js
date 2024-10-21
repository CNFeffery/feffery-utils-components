// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useResponsive } from 'ahooks';

/**
 * 页面响应式监听组件FefferyResponsive
 */
const FefferyResponsive = (props) => {
    const {
        setProps,
        loading_state
    } = props;

    const _responsive = useResponsive();

    useEffect(() => {
        setProps({ responsive: _responsive })
    }, [_responsive]);

    return <></>;
}

FefferyResponsive.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 监听当前页面尺寸下对应各断点像素宽度的满足情况
     */
    responsive: PropTypes.object,

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

FefferyResponsive.defaultProps = {
}

export default FefferyResponsive;