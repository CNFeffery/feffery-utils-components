import React, { useEffect } from 'react';
import { useExternal } from 'ahooks';
import PropTypes from 'prop-types';

/**
 * 外部css资源动态注入组件FefferyExternalCss
 */
const FefferyExternalCss = (props) => {

    const {
        id,
        cssUrl,
        setProps,
        loading_state
    } = props;

    const status = useExternal(cssUrl, {
        type: 'css'
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

FefferyExternalCss.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置对应绑定的css静态文件资源`url`
     * 默认值：`''`
     */
    cssUrl: PropTypes.string,

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
FefferyExternalCss.defaultProps = {
    cssUrl: ''
}

export default FefferyExternalCss;