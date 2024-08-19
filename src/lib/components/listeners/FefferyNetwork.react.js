import { useEffect } from 'react';
import { useNetwork } from 'ahooks';
import PropTypes from 'prop-types';

/**
 * 网络状态信息监听组件FefferyNetwork
 */
const FefferyNetwork = (props) => {
    const {
        id,
        key,
        online,
        since,
        rtt,
        type,
        downlink,
        downlinkMax,
        saveData,
        effectiveType,
        setProps,
        loading_state
    } = props;

    const networkState = useNetwork();

    useEffect(() => {
        setProps({
            ...JSON.parse(JSON.stringify(networkState))
        });
    }, [networkState]);

    return <></>;
}

FefferyNetwork.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用key值
     */
    key: PropTypes.string,

    /**
     * 网络是否为在线
     */
    online: PropTypes.bool,

    /**
     * `online`最后改变时间
     */
    since: PropTypes.string,

    /**
     * 当前连接下评估的往返时延
     */
    rtt: PropTypes.number,

    /**
     * 设备使用与所述网络进行通信的连接的类型，可选项有'bluetooth'、'cellular'、'ethernet'、'none'、'wifi'、'wimax'、'other'、'unknown'
     */
    type: PropTypes.oneOf(['bluetooth', 'cellular', 'ethernet', 'none', 'wifi', 'wimax', 'other', 'unknown']),

    /**
     * 有效带宽估算（单位：兆比特/秒）
     */
    downlink: PropTypes.number,

    /**
     * 最大下行速度（单位：兆比特/秒）
     */
    downlinkMax: PropTypes.number,

    /**
     * 用户代理是否设置了减少数据使用的选项
     */
    saveData: PropTypes.bool,

    /**
     * 网络连接的类型，可选的值有'slow-2g'、'2g'、'3g'、'4g'
     */
    effectiveType: PropTypes.oneOf(['slow-2g', '2g', '3g', '4g']),

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
FefferyNetwork.defaultProps = {
}

export default FefferyNetwork;