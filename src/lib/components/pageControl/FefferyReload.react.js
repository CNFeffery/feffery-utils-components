import { useEffect } from 'react';
import PropTypes from 'prop-types';

// 定义页面重载组件FefferyReload
const FefferyReload = (props) => {
    const {
        id,
        reload,
        delay,
        setProps,
        loading_state
    } = props;

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


// 定义参数或属性
FefferyReload.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 执行页面重载操作的标志，当设置为true时会进行页面重载
     */
    reload: PropTypes.bool,

    /**
     * 设置重载执行的延时时长（单位：毫秒）
     */
    delay: PropTypes.number,

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
FefferyReload.defaultProps = {
}

export default FefferyReload;