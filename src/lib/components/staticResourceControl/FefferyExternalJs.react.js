// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useExternal } from 'ahooks';

/**
 * 外部js资源动态注入组件FefferyExternalJs
 */
const FefferyExternalJs = ({
    jsUrl = '',
    setProps
}) => {

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

FefferyExternalJs.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置对应绑定的js静态文件资源`url`
     * 默认值：`''`
     */
    jsUrl: PropTypes.string,

    /**
     * 监听最近一次资源变更操作后对应的状态
     */
    recentlyStatus: PropTypes.oneOf([
        'unset', 'loading', 'ready', 'error'
    ]),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyExternalJs;