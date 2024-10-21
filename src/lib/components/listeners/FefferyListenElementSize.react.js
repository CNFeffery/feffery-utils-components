// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useElementSize } from '@reactuses/core';

/**
 * 元素尺寸监听组件FefferyListenElementSize
 */
const FefferyListenElementSize = (props) => {
    let {
        target,
        width,
        height,
        setProps,
        loading_state
    } = props;

    const [_width, _height] = useElementSize(() => target ? document.getElementById(target) : document);

    useEffect(() => {
        if (width !== parseInt(_width)) {
            setProps({ width: _width })
        }
    }, [_width])

    useEffect(() => {
        if (height !== parseInt(_height)) {
            setProps({ height: _height })
        }
    }, [_height])

    return <></>;
}

FefferyListenElementSize.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 必填，设置尺寸监听目标元素`id`
     */
    target: PropTypes.string.isRequired,

    /**
     * 监听目标元素像素宽度
     */
    width: PropTypes.number,

    /**
     * 监听目标元素像素高度
     */
    height: PropTypes.number,

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

FefferyListenElementSize.defaultProps = {
}

export default FefferyListenElementSize;