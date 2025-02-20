// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useLocation } from 'react-use';

/**
 * 地址监听组件FefferyLocation
 */
const FefferyLocation = ({
    setProps
}) => {

    const state = useLocation();

    useEffect(() => {
        if (state) {
            // 更新地址相关信息状态
            setProps({
                href: state.href,
                pathname: state.pathname,
                search: state.search,
                hash: state.hash,
                host: state.host,
                hostname: state.hostname,
                port: state.port,
                protocol: state.protocol,
                trigger: state.trigger
            })
        }
    }, [state])

    return <></>;
}

FefferyLocation.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,


    /**
     * 监听最新的`href`信息
     */
    href: PropTypes.string,

    /**
     * 监听最新的`pathname`信息
     */
    pathname: PropTypes.string,

    /**
     * 监听最新的`search`信息
     */
    search: PropTypes.string,

    /**
     * 监听最新的`hash`信息
     */
    hash: PropTypes.string,

    /**
     * 监听最新的`host`信息
     */
    host: PropTypes.string,

    /**
     * 监听最新的`hostname`信息
     */
    hostname: PropTypes.string,

    /**
     * 监听最新的`port`信息
     */
    port: PropTypes.string,

    /**
     * 监听最新的`protocol`信息
     */
    protocol: PropTypes.string,

    /**
     * 监听最近一次地址更新行为触发类型，`'load'`表示页面重载行为，`'pushstate'`表示动态更新行为，`'popstate'`表示返回上一步地址
     */
    trigger: PropTypes.oneOf(['load', 'pushstate', 'popstate']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyLocation;