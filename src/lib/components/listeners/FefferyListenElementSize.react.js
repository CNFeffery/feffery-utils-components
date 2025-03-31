// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 辅助库
import { isNaN } from 'lodash';
// 组件核心
import { useSize } from 'ahooks';

/**
 * 元素尺寸监听组件FefferyListenElementSize
 */
const FefferyListenElementSize = ({
    target,
    setProps
}) => {

    const size = useSize(() => document.getElementById(target));

    useEffect(() => {
        if (size) {
            setProps({
                width: size.width,
                height: size.height
            });
        }
    }, [size]);

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
    setProps: PropTypes.func
};

export default FefferyListenElementSize;