// react核心
import { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useCountDown } from 'ahooks';

/**
 * 倒计时组件FefferyCountDown
 */
const FefferyCountDown = ({
    delay,
    interval = 1,
    setProps
}) => {

    const [targetDate, setTargetDate] = useState(null);

    useEffect(() => {
        if (delay) {
            setTargetDate(Date.now() + 1000 * delay)
        }
    }, [delay])

    const [_countdown] = useCountDown({
        targetDate: targetDate,
        interval: interval * 1000,
        onEnd: () => {
            setProps({
                delay: null,
                countdown: 0
            })
        }
    });

    useEffect(() => {
        if (_countdown && delay) {
            setProps({
                countdown: Math.round(_countdown / 1000)
            })
        }
    }, [_countdown])

    return <></>;
}

FefferyCountDown.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 用于设置距离下一次超时事件触发的倒计时间隔，单位：秒，每次有效的`delay`对应超时事件结束后都会被重置为空值
     */
    delay: PropTypes.number,

    /**
     * 设置倒计时时间间隔，单位：秒
     * 默认值：`1`
     */
    interval: PropTypes.number,

    /**
     * 监听当前剩余时间秒数
     */
    countdown: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyCountDown;