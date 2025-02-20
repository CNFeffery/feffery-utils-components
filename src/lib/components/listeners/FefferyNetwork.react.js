// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useNetwork } from 'ahooks';

/**
 * 网络状态信息监听组件FefferyNetwork
 */
const FefferyNetwork = ({
    setProps
}) => {

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
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
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
     * 设备使用与所述网络进行通信的连接的类型，可选项有`'bluetooth'`、`'cellular'`、`'ethernet'`、`'none'`、`'wifi'`、`'wimax'`、`'other'`、`'unknown'`
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
     * 网络连接的类型，可选项有`'slow-2g'`、`'2g'`、`'3g'`、`'4g'`
     */
    effectiveType: PropTypes.oneOf(['slow-2g', '2g', '3g', '4g']),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyNetwork;