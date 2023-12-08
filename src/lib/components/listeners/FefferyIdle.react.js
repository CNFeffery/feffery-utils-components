import { useEffect } from 'react';
import { useIdle } from 'react-use';
import PropTypes from 'prop-types';

// 定义闲置状态监听组件FefferyIdle
const FefferyIdle = (props) => {

    const {
        id,
        waitDuration,
        setProps,
        loading_state
    } = props;

    const _isIdle = useIdle(waitDuration);

    useEffect(() => {
        setProps({ isIdle: _isIdle })
    }, [_isIdle]);

    return <></>;
}

// 定义参数或属性
FefferyIdle.propTypes = {
    // 组件id
    id: PropTypes.string,

    // 监听当前应用是否处于闲置状态
    isIdle: PropTypes.bool,

    // 设置经过多长时间（单位：毫秒）没有操作后视作闲置状态
    // 默认为3000
    waitDuration: PropTypes.number,

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
FefferyIdle.defaultProps = {
    waitDuration: 3000
}

export default FefferyIdle;