// react核心
import PropTypes from 'prop-types';
// 组件核心
import CountUp from 'react-countup';

/**
 * 数字递增组件FefferyCountUp
 */
const FefferyCountUp = (props) => {
    const {
        id,
        className,
        style,
        key,
        end,
        start,
        duration,
        decimals,
        enableScrollSpy,
        scrollSpyDelay,
        scrollSpyOnce,
        separator,
        setProps,
        loading_state
    } = props;

    if (enableScrollSpy) {
        // #70 
        // 参考资料：https://stackoverflow.com/questions/76977652/countup-target-is-null-or-undefined-null-react-js
        return (
            <CountUp
                key={key}
                end={end}
                start={start}
                duration={duration}
                decimals={decimals}
                enableScrollSpy={enableScrollSpy}
                scrollSpyDelay={scrollSpyDelay}
                scrollSpyOnce={scrollSpyOnce}
                separator={separator}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                } >
                {
                    ({ countUpRef }) => (
                        <span id={id}
                            className={className}
                            style={style}
                            ref={countUpRef}
                        />
                    )
                }
            </CountUp>
        )
    }

    return (
        <CountUp
            id={id}
            className={className}
            style={style}
            key={key}
            end={end}
            start={start}
            duration={duration}
            decimals={decimals}
            separator={separator}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            }
        />
    )
}

FefferyCountUp.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 必填，数字递增目标值，每次更新此参数后会重新触发递增动画
     */
    end: PropTypes.number.isRequired,

    /**
     * 数字递增起始值，每次更新此参数后会重新触发递增动画
     * 默认值：`0`
     */
    start: PropTypes.number,

    /**
     * 数字递增动画耗时，单位：秒，每次更新此参数后会重新触发递增动画
     * 默认值：`2`
     */
    duration: PropTypes.number,

    /**
     * 小数精度
     * 默认值：`0`
     */
    decimals: PropTypes.number,

    /**
     * 是否在当前元素进入视口后才开始执行递增动画
     * 默认值：`true`
     */
    enableScrollSpy: PropTypes.bool,

    /**
     * 当`enableScrollSpy=True`时，设置当前元素进入视口后延时多久开始执行递增动画，单位：毫秒
     * 默认值：`0`
     */
    scrollSpyDelay: PropTypes.number,

    /**
     * 是否仅进行一次视口出现后启用动画行为
     * 默认值：`true`
     */
    scrollSpyOnce: PropTypes.bool,

    /**
     * 自定义千分符
     * 默认值：`','`
     */
    separator: PropTypes.string,

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

FefferyCountUp.defaultProps = {
    start: 0,
    duration: 2,
    decimals: 0,
    enableScrollSpy: true,
    scrollSpyDelay: 0,
    scrollSpyOnce: true,
    separator: ','
}

export default FefferyCountUp;