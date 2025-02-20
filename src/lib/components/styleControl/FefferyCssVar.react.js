// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * CSS变量更新组件FefferyCssVar
 */
const FefferyCssVar = ({
    id,
    cssVars,
    setProps
}) => {

    useEffect(() => {
        // 更新css变量
        if (cssVars) {
            for (let key of Object.keys(cssVars)) {
                // 更新当前迭代到的css变量
                document.documentElement.style.setProperty(key, cssVars[key])
            }
        }
    }, [cssVars])

    return <></>;
}

FefferyCssVar.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 定义要更新的`css`变量键值对信息
     */
    cssVars: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyCssVar;