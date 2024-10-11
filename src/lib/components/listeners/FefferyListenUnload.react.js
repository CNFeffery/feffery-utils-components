import { useEffect } from 'react';
import PropTypes from 'prop-types';

// 定义页面关闭监听组件FefferyListenUnload
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

// 定义参数或属性
FefferyListenUnload.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 监听页面重载或关闭事件，每次页面关闭时会触发更新为true
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

// 设置默认参数
FefferyListenUnload.defaultProps = {
    confirmBeforeUnload: false
}

export default FefferyListenUnload;