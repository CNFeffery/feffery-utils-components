import { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * 调试守护组件FefferyDebugGuardian
 */
const FefferyDebugGuardian = (props) => {

    // 组件挂载时开始每隔1秒检查一次debugger是否激活
    useEffect(() => {
        let check = function () {
            let doCheck = (a) => {
                if (("" + a / a)["length"] !== 1 || a % 20 === 0) {
                    (function () { }
                    ["constructor"]("debugger")())
                } else {
                    (function () { }
                    ["constructor"]("debugger")())
                }
                doCheck(++a)
            }
            try {
                doCheck(0)
            } catch (err) { }
        };
        setInterval(function () {
            check()
        }, 1000);
        // 立即执行一次
        check();
    }, [])

    return <></>;
}

// 定义参数或属性
FefferyDebugGuardian.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

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
FefferyDebugGuardian.defaultProps = {
}

export default FefferyDebugGuardian;