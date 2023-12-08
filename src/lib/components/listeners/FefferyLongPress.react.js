import React from 'react';
import { useLongPress } from 'ahooks';
import PropTypes from 'prop-types';

// 定义长按事件监听组件FefferyLongPress
const FefferyLongPress = (props) => {

    const {
        id,
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

// 定义参数或属性
FefferyLongPress.propTypes = {
    // 组件id
    id: PropTypes.string,

    // 设置当前长按监听组件的监听目标元素id
    targetId: PropTypes.string,

    // 监听目标组件累计被长按次数，默认为0
    pressCounts: PropTypes.number,

    // 设置符合长按行为的持续时长，单位：毫秒
    // 默认：300
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

// 设置默认参数
FefferyLongPress.defaultProps = {
    pressCounts: 0,
    delay: 300
}

export default React.memo(FefferyLongPress);