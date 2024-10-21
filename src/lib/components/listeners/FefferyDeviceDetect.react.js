// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import {
    isMobile,
    isAndroid,
    isIOS,
    isChrome,
    isFirefox,
    isSafari,
    isIE,
    isEdge,
    osVersion,
    osName,
    browserVersion,
    fullBrowserVersion,
    browserName,
    getUA,
    deviceType
} from 'react-device-detect';

/**
 * 设备信息检测组件FefferyDeviceDetect
 */
const FefferyDeviceDetect = (props) => {
    const {
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        setProps({
            deviceInfo: {
                isMobile,
                isAndroid,
                isIOS,
                isChrome,
                isFirefox,
                isSafari,
                isIE,
                isEdge,
                osVersion,
                osName,
                browserVersion,
                fullBrowserVersion,
                browserName,
                ua: getUA,
                deviceType
            }
        })
    }, [])

    return <></>;
}

FefferyDeviceDetect.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听当前访问设备的全部信息
     */
    deviceInfo: PropTypes.exact({
        /**
         * 检测是否为手机、平板等移动设备
         */
        isMobile: PropTypes.bool,
        /**
         * 检测是否为安卓系统
         */
        isAndroid: PropTypes.bool,
        /**
         * 检测是否为ios系统
         */
        isIOS: PropTypes.bool,
        /**
         * 检测是否为Chrome浏览器
         */
        isChrome: PropTypes.bool,
        /**
         * 检测是否为Firefox浏览器
         */
        isFirefox: PropTypes.bool,
        /**
         * 检测是否为Safari浏览器
         */
        isSafari: PropTypes.bool,
        /**
         * 检测是否为IE浏览器
         */
        isIE: PropTypes.bool,
        /**
         * 检测是否为Edge浏览器
         */
        isEdge: PropTypes.bool,
        /**
         * 检测系统版本
         */
        osVersion: PropTypes.string,
        /**
         * 检测系统名称
         */
        osName: PropTypes.string,
        /**
         * 检测浏览器缩略版本
         */
        browserVersion: PropTypes.string,
        /**
         * 检测完整的浏览器版本
         */
        fullBrowserVersion: PropTypes.string,
        /**
         * 检测浏览器名称
         */
        browserName: PropTypes.string,
        /**
         * 检测`User-Agent`信息
         */
        ua: PropTypes.string,
        /**
         * 检测设备类型
         */
        deviceType: PropTypes.string
    }),

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
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

FefferyDeviceDetect.defaultProps = {
}

export default FefferyDeviceDetect;