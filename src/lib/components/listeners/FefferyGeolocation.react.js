import { useEffect } from 'react';
import { useGeolocation } from 'react-use';
import PropTypes from 'prop-types';

// 定义地理位置监听组件FefferyGeolocation
const FefferyGeolocation = (props) => {

    const {
        id,
        setProps,
        loading_state
    } = props;

    const _state = useGeolocation();

    useEffect(() => {
        setProps({ geoLocationInfo: _state })
    }, [_state]);

    return <></>;
}

// 定义参数或属性
FefferyGeolocation.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 监听当前用户地理位置相关信息
    geoLocationInfo: PropTypes.object,

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
FefferyGeolocation.defaultProps = {
}

export default FefferyGeolocation;