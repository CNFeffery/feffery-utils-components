// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useIdle } from 'react-use';

/**
 * 闲置状态监听组件FefferyIdle
 */
const FefferyIdle = ({
    waitDuration = 3000,
    setProps
}) => {

    const _isIdle = useIdle(waitDuration);

    useEffect(() => {
        setProps({ isIdle: _isIdle })
    }, [_isIdle]);

    return <></>;
}

FefferyIdle.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听当前应用是否处于闲置状态
     */
    isIdle: PropTypes.bool,

    /**
     * 设置经过多长时间没有操作后视作闲置状态，单位：毫秒
     * 默认值：`3000`
     */
    waitDuration: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyIdle;