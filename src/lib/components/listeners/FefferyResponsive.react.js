import { useEffect } from 'react';
import { useResponsive } from 'ahooks';
import PropTypes from 'prop-types';

// 定义页面响应式监听组件FefferyResponsive
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

// 定义参数或属性
FefferyResponsive.propTypes = {
    /**
     * 组件id
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

// 设置默认参数
FefferyResponsive.defaultProps = {
}

export default FefferyResponsive;