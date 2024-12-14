import { useEffect } from 'react';
import { useWebNotification } from '@reactuses/core';
import PropTypes from 'prop-types';

/**
 * web通知组件FefferyWebNotification
 */
const FefferyWebNotification = (props) => {
    const {
        message,
        setProps,
        loading_state
    } = props;

    const { isSupported: _isSupported, show } = useWebNotification(true);

    useEffect(() => {
        setProps({ isSupported: _isSupported })
    }, [_isSupported])

    useEffect(() => {
        if (_isSupported && message) {
            show(message);
            // 重置message
            setProps({ message: null });
        }
    }, [message])

    return <></>;
}

FefferyWebNotification.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置要发送的信息内容，每次成功发送后都会重置为空
     */
    message: PropTypes.string,

    /**
     * 监听用户浏览器中是否支持web通知
     */
    isSupported: PropTypes.bool,

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

FefferyWebNotification.defaultProps = {
}

export default FefferyWebNotification;