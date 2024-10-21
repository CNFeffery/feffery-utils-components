// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useWindowSize } from 'react-use';

/**
 * 浏览器窗口尺寸监听组件FefferyWindowSize
 */
const FefferyWindowSize = (props) => {
    const {
        setProps,
        loading_state
    } = props;

    const { width, height } = useWindowSize();

    useEffect(() => {
        setProps({
            _width: width,
            _height: height
        })
    }, [width, height]);

    return <></>;
}

FefferyWindowSize.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听当前浏览器窗口像素宽度
     */
    _width: PropTypes.number,

    /**
     * 监听当前浏览器窗口像素高度
     */
    _height: PropTypes.number,

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

FefferyWindowSize.defaultProps = {
}

export default FefferyWindowSize;