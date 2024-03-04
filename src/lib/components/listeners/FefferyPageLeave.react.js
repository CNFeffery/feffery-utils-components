import { useEffect } from 'react';
import { usePageLeave } from '@reactuses/core';
import PropTypes from 'prop-types';

// 定义鼠标离开页面监听组件FefferyPageLeave
const FefferyPageLeave = (props) => {
    const {
        setProps
    } = props;

    const _isLeft = usePageLeave();

    useEffect(() => {
        setProps({ isLeft: _isLeft })
    }, [_isLeft]);

    return <></>;
}

// 定义参数或属性
FefferyPageLeave.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 强制刷新用
     */
    key: PropTypes.string,

    /**
     * 监听鼠标是否离开当前页面
     */
    isLeft: PropTypes.bool,

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
FefferyPageLeave.defaultProps = {
}

export default FefferyPageLeave;