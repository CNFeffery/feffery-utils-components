// react核心
import PropTypes from 'prop-types';
// 组件核心
import { useTimeout } from 'ahooks';

/**
 * 定时执行组件FefferyTimeout
 */
const FefferyTimeout = ({
    delay,
    timeoutCount = 0,
    setProps
}) => {

    useTimeout(() => {
        setProps({
            timeoutCount: timeoutCount + 1,
            delay: undefined
        });
    }, delay);

    return <></>;
}

FefferyTimeout.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听超时事件完成次数
     * 默认值：`0`
     */
    timeoutCount: PropTypes.number,

    /**
     * 设置距离下一次超时事件触发的倒计时间隔，单位：毫秒，每次有效的`delay`对应超时事件结束后都会被重置为空值
     */
    delay: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyTimeout;