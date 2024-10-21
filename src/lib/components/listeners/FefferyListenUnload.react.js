// raect核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';

/**
 * 页面关闭监听组件FefferyListenUnload
 */
const FefferyListenUnload = (props) => {
    let {
        confirmBeforeUnload,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        const handleTabClose = (e) => {
            if (confirmBeforeUnload) {
                e.returnValue = !1;
            }
            setProps({
                unloaded: true
            })
        };

        window.addEventListener('beforeunload', handleTabClose);

        return () => {
            window.removeEventListener('beforeunload', handleTabClose);
        };
    }, []);

    return <></>;
}

FefferyListenUnload.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听页面重载或关闭事件，每次页面关闭时会触发更新为`true`
     */
    unloaded: PropTypes.bool,

    /**
     * 是否在用户重载或关闭当前页面时，添加二次确认
     * 默认值：`false`
     */
    confirmBeforeUnload: PropTypes.bool,

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

FefferyListenUnload.defaultProps = {
    confirmBeforeUnload: false
}

export default FefferyListenUnload;