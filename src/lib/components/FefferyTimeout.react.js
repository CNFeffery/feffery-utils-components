import { useTimeout } from 'ahooks';
import PropTypes from 'prop-types';

// 定义定时执行组件FefferyTimeout
const FefferyTimeout = (props) => {

    const {
        id,
        delay,
        timeoutCount,
        setProps,
        loading_state
    } = props;

    useTimeout(() => {
        setProps({
            timeoutCount: timeoutCount + 1,
            delay: undefined
        });
    }, delay);

    return (<div
        id={id}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />);
}

// 定义参数或属性
FefferyTimeout.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 监听超时事件完成次数，默认为0
    timeoutCount: PropTypes.number,

    // 用于设置距离下一次超时事件触发的倒计时间隔（单位：毫秒）
    // 每次有效的delay对应超时事件结束后都会被重置为undefined
    delay: PropTypes.number,

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
FefferyTimeout.defaultProps = {
    timeoutCount: 0
}

export default FefferyTimeout;