// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useScroll } from 'ahooks';
// 辅助库
import { round } from 'lodash';

/**
 * 滚动条监听组件FefferyListenScroll
 */
const FefferyListenScroll = (props) => {
    let {
        target,
        setProps,
        loading_state
    } = props;

    const _position = useScroll(() => target ? document.getElementById(target) : document);

    useEffect(() => {
        if (_position) {
            setProps({
                position: { left: round(_position.left), top: round(_position.top) }
            })
        }
    }, [_position])

    return <></>;
}

FefferyListenScroll.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置滚动条监听目标元素`id`，默认为整个页面
     */
    target: PropTypes.string,

    /**
     * 监听目标滚动条的水平及竖直方向上的像素偏移量
     */
    position: PropTypes.object,

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

FefferyListenScroll.defaultProps = {
}

export default FefferyListenScroll;