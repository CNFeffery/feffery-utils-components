// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useRoute } from "wouter";

/**
 * 路由匹配组件FefferyRouteMatch
 */
const FefferyRouteMatch = ({
    pattern,
    updateParamsWhenMatch = true,
    setProps
}) => {

    const [_match, _params] = useRoute(pattern);

    // 路由匹配情况变化时，更新相关事件信息
    useEffect(() => {
        if (updateParamsWhenMatch) {
            if (_match) {
                // 同时更新match和params
                setProps({ match: _match, params: _params });
            } else {
                // 仅更新match
                setProps({ match: _match });
            }
        } else {
            // 同时更新match和params
            setProps({ match: _match, params: _params });
        }
    }, [_match])

    return <></>;
}

FefferyRouteMatch.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 必填，目标路由匹配模式规则
     */
    pattern: PropTypes.oneOfType([
        PropTypes.string
    ]).isRequired,

    /**
     * 监听当前地址是否匹配目标路由
     */
    match: PropTypes.bool,

    /**
     * 当前地址匹配目标路由时，监听对应的相关参数信息
     */
    params: PropTypes.object,

    /**
     * 是否仅在当前地址匹配目标路由时，对`params`进行更新
     * 默认值：`true`
     */
    updateParamsWhenMatch: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyRouteMatch;