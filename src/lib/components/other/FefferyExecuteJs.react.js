// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * js执行组件FefferyExecuteJs
 */
const FefferyExecuteJs = ({
    jsString,
    mode = 'default',
    delay,
    interval,
    targetSelector,
    targetWaitTimeout,
    setProps
}) => {

    useEffect(() => {
        // delay模式
        if (mode === 'delay') {
            // 延时执行原生js程序
            if (jsString) {
                setTimeout(
                    () => {
                        try { eval(jsString) }
                        catch (exception) { console.error(exception) }
                        // 重置jsString
                        setProps({
                            jsString: null
                        })
                    },
                    delay
                )
            }
        } else if (mode === 'interval') {
            // 定时执行原生js程序
            if (jsString) {
                // 创建轮询器
                const _interval = setInterval(
                    () => {
                        try { eval(jsString) }
                        catch (exception) { console.error(exception) }
                    },
                    interval
                )
                // jsString更新或组件卸载时，销毁轮询器
                return () => clearInterval(_interval);
            }
        } else if (mode === 'wait-until-element-rendered') {
            // 等待目标元素渲染后执行
            if (jsString) {
                // 记录逻辑开始时间戳
                const startTime = Date.now()

                // 创建定时器
                let _interval = setInterval(
                    () => {
                        // 若目标元素出现
                        if (document.querySelector(targetSelector)) {
                            clearInterval(_interval)
                            _interval = false;
                            try { eval(jsString) }
                            catch (exception) { console.error(exception) }
                            // 重置jsString
                            setProps({
                                jsString: null
                            })
                        }
                        // 若距离startTime时长超出targetWaitTimeout限制，则强制终止轮询检查过程
                        if (targetWaitTimeout && Date.now() - startTime > targetWaitTimeout) {
                            clearInterval(_interval)
                            _interval = false;
                            // 重置jsString
                            setProps({
                                jsString: null
                            })
                        }
                    },
                    200 // 默认200毫秒检测一次目标元素出现情况
                )

                // 若jsString更新或组件卸载时，轮询器仍然未被清除，则进行清除
                return () => !_interval && clearInterval(_interval)
            }
        } else {
            // 执行原生js程序
            if (jsString) {
                try { eval(jsString) }
                catch (exception) { console.error(exception) }
                // 重置jsString
                setProps({
                    jsString: null
                })
            }
        }
    }, [jsString])

    return <></>;
}

FefferyExecuteJs.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置要执行的`javascript`代码字符串
     */
    jsString: PropTypes.string,

    /**
     * 设置执行模式，可选项有`'default'`（立即执行）、`'delay'`（延迟执行）、`'interval'`（定时轮询执行）、`'wait-until-element-rendered'`（等待目标元素渲染后执行）
     * 默认值：`'default'`
     */
    mode: PropTypes.oneOf(['default', 'delay', 'interval', 'wait-until-element-rendered']),

    /**
     * `delay`模式下，设置延时执行时长，单位：毫秒
     */
    delay: PropTypes.number,

    /**
     * `interval`模式下，设置轮询执行间隔时长，单位：毫秒
     */
    interval: PropTypes.number,

    /**
     * `wait-until-element-rendered`模式下，设置需要等待渲染完成的目标元素`css`选择器
     */
    targetSelector: PropTypes.string,

    /**
     * `wait-until-element-rendered`模式下，设置目标元素渲染检测最大等待时长，单位：毫秒，默认无限制
     */
    targetWaitTimeout: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyExecuteJs;