import { useEffect } from 'react';
import { useLocation } from 'react-use';
import PropTypes from 'prop-types';

// 定义地址监听组件FefferyLocation
const FefferyLocation = (props) => {

    const {
        id,
        setProps,
        loading_state
    } = props;

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

    return (<div
        id={id}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />);
}

// 定义参数或属性
FefferyLocation.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 用于监听最新的href信息
    href: PropTypes.string,

    // 用于监听最新的pathname信息
    pathname: PropTypes.string,

    // 用于监听最新的search信息
    search: PropTypes.string,

    // 用于监听最新的hash信息
    hash: PropTypes.string,

    // 用于监听最新的host信息
    host: PropTypes.string,

    // 用于监听最新的hostname信息
    hostname: PropTypes.string,

    // 用于监听最新的port信息
    port: PropTypes.string,

    // 用于监听最新的protocol信息
    protocol: PropTypes.string,

    // 用于监听最近一次地址更新行为触发类型
    // 'load'表示页面重载行为，'pushstate'表示动态更新行为，'popstate'表示返回上一步地址
    trigger: PropTypes.oneOf(['load', 'pushstate', 'popstate']),

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
FefferyLocation.defaultProps = {
}

export default FefferyLocation;