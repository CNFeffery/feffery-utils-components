// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useResponsive } from 'ahooks';

/**
 * 页面响应式监听组件FefferyResponsive
 */
const FefferyResponsive = ({
    setProps
}) => {

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
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听当前页面尺寸下对应各断点像素宽度的满足情况
     */
    responsive: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyResponsive;