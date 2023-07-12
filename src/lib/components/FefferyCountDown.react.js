import { useEffect, useState } from 'react';
import { useCountDown } from 'ahooks';
import PropTypes from 'prop-types';

// 定义倒计时组件FefferyCountDown
const FefferyCountDown = (props) => {

    const {
        id,
        delay,
        interval,
        setProps,
        loading_state
    } = props;

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

// 定义参数或属性
FefferyCountDown.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 用于设置距离下一次超时事件触发的倒计时间隔（单位：秒）
    // 每次有效的delay对应超时事件结束后都会被重置为undefined
    delay: PropTypes.number,

    // 设置倒计时时间间隔（单位：秒），默认为1
    interval: PropTypes.number,

    // 监听当前剩余时间秒数，默认为0
    countdown: PropTypes.number,

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
FefferyCountDown.defaultProps = {
    interval: 1
}

export default FefferyCountDown;