// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useLongPress } from 'ahooks';

/**
 * 长按事件监听组件FefferyLongPress
 */
const FefferyLongPress = (props) => {
    const {
        targetId,
        pressCounts,
        delay,
        setProps,
        loading_state
    } = props;

    useLongPress(
        () => {
            setProps({
                pressCounts: pressCounts + 1
            })
        },
        () => document.getElementById(targetId),
        {
            delay: delay
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
     * 设置符合长按行为的持续时长，单位：毫秒
     * 默认值：`300`
     */
    delay: PropTypes.number,

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

FefferyLongPress.defaultProps = {
    pressCounts: 0,
    delay: 300
}

export default React.memo(FefferyLongPress);