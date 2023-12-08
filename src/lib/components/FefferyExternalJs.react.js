import React, { useEffect } from 'react';
import { useExternal } from 'ahooks';
import PropTypes from 'prop-types';

// 定义外部js资源动态注入组件FefferyExternalJs
const FefferyExternalJs = (props) => {

    const {
        id,
        jsUrl,
        setProps,
        loading_state
    } = props;

    const status = useExternal(jsUrl, {
        type: 'js'
    });

    useEffect(() => {
        // 更新最近一次资源变更状态
        if (status) {
            setProps({
                recentlyStatus: status
            })
        }
    }, [status])

    return <></>;
}

// 定义参数或属性
FefferyExternalJs.propTypes = {
    // 组件id
    id: PropTypes.string,

    // 设置对应绑定的js静态文件资源url，默认为''
    jsUrl: PropTypes.string,

    // 监听最近一次资源变更操作后对应的状态
    recentlyStatus: PropTypes.oneOf([
        'unset', 'loading', 'ready', 'error'
    ]),

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
FefferyExternalJs.defaultProps = {
    jsUrl: ''
}

export default FefferyExternalJs;