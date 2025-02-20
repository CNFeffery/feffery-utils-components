// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useLongPress } from 'ahooks';

/**
 * 长按事件监听组件FefferyLongPress
 */
const FefferyLongPress = ({
    targetId,
    pressCounts = 0,
    delay = 300,
    setProps
}) => {

    useLongPress(
        () => {
            setProps({
                pressCounts: pressCounts + 1,
                isLongPressing: true
            })
        },
        () => document.getElementById(targetId),
        {
            delay: delay,
            onLongPressEnd: () => setProps({ isLongPressing: false })
        }
    )

    return <></>;
}

FefferyLongPress.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置当前长按监听组件的监听目标元素`id`
     */
    targetId: PropTypes.string,

    /**
     * 监听目标组件累计被长按次数
     * 默认值：`0`
     */
    pressCounts: PropTypes.number,

    /**
     * 监听目标组件是否正处于长按状态
     */
    isLongPressing: PropTypes.bool,

    /**
     * 设置符合长按行为的持续时长，单位：毫秒
     * 默认值：`300`
     */
    delay: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default React.memo(FefferyLongPress);