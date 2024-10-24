import { useEffect } from 'react';
import PropTypes from 'prop-types';
import devtoolsDetector from 'devtools-detector';

/**
 * 调试守护组件FefferyDebugGuardian
 */
const FefferyDebugGuardian = (props) => {

    const {
        detectInterval,
        strategy,
        jsString
    } = props;

    // 组件挂载时开始每隔500毫秒检查一次debugger是否激活
    useEffect(() => {
        // 递归debug
        let recursiveDebug = () => {
            (function () { }
            ["constructor"]("debugger")())
            recursiveDebug();
        }

        if (!devtoolsDetector.isLaunch()) {
            devtoolsDetector.addListener(
                isOpen => {
                    if (isOpen) {
                        if (strategy === 'infinite-debugger') {
                            try {
                                recursiveDebug();
                            } catch (err) { }
                        } else if (strategy === 'debugger-then-auto-close') {
                            window.open("", "_self").close()
                        } else if (strategy === 'debugger-then-execute-js') {
                            try {
                                eval(jsString)
                            } catch (exception) { console.error(exception) }
                        }
                    }
                }
            );
            devtoolsDetector.setDetectDelay(detectInterval || 1000);
            devtoolsDetector.launch();

            return () => devtoolsDetector.isLaunch() && devtoolsDetector.stop();
        }
    }, [strategy])

    return <></>;
}

FefferyDebugGuardian.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 设置后台轮询检测的间隔时长，单位：毫秒
     * 默认值：`1000`
     */
    detectInterval: PropTypes.number,

    /**
     * 设置当检测到开发者工具被打开时的应对策略，可选的有`'infinite-debugger'`（无限debugger）、`'debugger-then-auto-close'`（激活debugger后自动关闭）、`'debugger-then-execute-js'`（激活debugger后执行js）
     * 默认值：`'infinite-debugger'`
     */
    strategy: PropTypes.oneOf(['infinite-debugger', 'debugger-then-auto-close', 'debugger-then-execute-js']),

    /**
     * 当`strategy`为`'debugger-then-execute-js'`时，设置要执行的js代码
     */
    jsString: PropTypes.string,

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
    detectInterval: 1000,
    strategy: 'infinite-debugger'
}

export default FefferyDebugGuardian;