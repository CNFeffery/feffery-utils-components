import { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * CSS变量更新组件FefferyCssVar
 */
const FefferyCssVar = (props) => {
    // 取得必要属性或参数
    const {
        id,
        cssVars,
        setProps,
        loading_state
    } = props;

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
FefferyCssVar.defaultProps = {
}

export default FefferyCssVar;