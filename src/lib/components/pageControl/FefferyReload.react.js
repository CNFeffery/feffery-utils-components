// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * 页面重载组件FefferyReload
 */
const FefferyReload = ({
    reload,
    delay,
    setProps
}) => {

    useEffect(() => {
        // 执行页面重载操作
        if (reload) {
            if (delay) {
                // 延时重载
                setTimeout(
                    () => window.location.reload(),
                    delay
                )
            } else {
                // 立即重载
                window.location.reload()
            }
        }
    }, [reload])

    return <></>;
}

FefferyReload.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 执行页面重载操作的标志，当设置为`true`时会进行页面重载
     */
    reload: PropTypes.bool,

    /**
     * 设置重载执行的延时时长（单位：毫秒）
     */
    delay: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyReload;