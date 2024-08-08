import PropTypes from 'prop-types';
import CountUp from 'react-countup';

// 定义数字递增组件FefferyCountUp
const FefferyCountUp = (props) => {
    // 取得必要属性或参数
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


// 定义参数或属性
FefferyCountUp.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * css类名
     */
    className: PropTypes.string,

    /**
     * 自定义css字典
     */
    style: PropTypes.object,

    /**
     * 强制刷新用
     */
    key: PropTypes.string,

    /**
     * 设置数字递增目标，必填
     * 对此参数的更新会重新触发递增动画
     */
    end: PropTypes.number.isRequired,

    /**
     * 设置数字递增起点，默认为0
     * 对此参数的更新会重新触发递增动画
     */
    start: PropTypes.number,

    /**
     * 设置数字递增动画耗时，单位：秒，默认为2
     * 对此参数的更新会重新触发递增动画
     */
    duration: PropTypes.number,

    /**
     * 设置小数精度，默认为0
     */
    decimals: PropTypes.number,

    /**
     * 设置是否在当前元素进入视口后才开始执行递增动画，默认为true
     */
    enableScrollSpy: PropTypes.bool,

    /**
     * 当enableScrollSpy为true时，设置当前元素进入视口后延时多久开始执行递增动画，单位：毫秒，默认为0
     */
    scrollSpyDelay: PropTypes.number,

    /**
     * 设置是否仅进行一次视口出现后启用动画行为，默认为true
     */
    scrollSpyOnce: PropTypes.bool,

    /**
     * 设置自定义千分符，默认为','
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

// 设置默认参数
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