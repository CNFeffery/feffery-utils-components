// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useTextSelection } from 'ahooks';

/**
 * 文字选中监听组件FefferyTextSelection
 */
const FefferyTextSelection = (props) => {
    const {
        targetId,
        targetSelector,
        targetType,
        setProps
    } = props;

    // 根据不同的定位目标规则类型进行目标容器的绑定
    const selection = useTextSelection(
        targetType === 'selector' ?
            document.querySelector(targetSelector) :
            document.getElementById(targetId)
    );

    useEffect(() => {
        if (selection?.text) {
            setProps({
                selectedTextInfo: {
                    timestamp: Date.now(),
                    ...selection
                }
            })
        }
    }, [selection])

    return <></>;
}

FefferyTextSelection.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置目标监听容器`id`
     */
    targetId: PropTypes.string,

    /**
     * 设置目标监听容器对应的`css`选择器
     */
    targetSelector: PropTypes.string,

    /**
     * 设置目标监听规则类型，可选项有`'id'`、`'selector'`
     * 默认值：`'id'`
     */
    targetType: PropTypes.oneOf(['id', 'selector']),

    /**
     * 监听最近一次目标容器内文本选中事件相关信息
     */
    selectedTextInfo: PropTypes.object,

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

FefferyTextSelection.defaultProps = {
    targetType: 'id'
}

export default FefferyTextSelection;