import { useEffect } from 'react';
import PropTypes from 'prop-types';

// 定义css变量快捷操作组件FefferyCssVar
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
            let docStyle = document.documentElement.style;
            for (let key in Object.keys(cssVars)) {
                // 更新当前迭代到的css变量
                docStyle.setProperty(key, cssVars[key])
            }
        }
    }, [cssVars])

    return <div
        id={id}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />;
}


// 定义参数或属性
FefferyCssVar.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 定义要更新的css变量键值对信息
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