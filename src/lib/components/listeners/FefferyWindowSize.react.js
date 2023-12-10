import { useEffect } from 'react';
import { useWindowSize } from 'react-use';
import PropTypes from 'prop-types';

// 定义浏览器窗口尺寸监听组件FefferyWindowSize
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

// 定义参数或属性
FefferyWindowSize.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 监听当前浏览器窗口像素宽度
     */
    _width: PropTypes.number,

    /**
     * 监听当前浏览器窗口高度
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

// 设置默认参数
FefferyWindowSize.defaultProps = {
}

export default FefferyWindowSize;