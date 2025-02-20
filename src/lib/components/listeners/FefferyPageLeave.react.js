// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { usePageLeave } from '@reactuses/core';

/**
 * 鼠标离开页面监听组件FefferyPageLeave
 */
const FefferyPageLeave = ({
    setProps
}) => {

    const _isLeft = usePageLeave();

    useEffect(() => {
        setProps({ isLeft: _isLeft })
    }, [_isLeft]);

    return <></>;
}

FefferyPageLeave.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听鼠标是否离开当前页面
     */
    isLeft: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyPageLeave;