// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useGeolocation } from 'react-use';

/**
 * 地理位置监听组件FefferyGeolocation
 */
const FefferyGeolocation = ({
    setProps
}) => {

    const _state = useGeolocation();

    useEffect(() => {
        setProps({ geoLocationInfo: _state })
    }, [_state]);

    return <></>;
}

FefferyGeolocation.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听当前用户地理位置相关信息
     */
    geoLocationInfo: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyGeolocation;