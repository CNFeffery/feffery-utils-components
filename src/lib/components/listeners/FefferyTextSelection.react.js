import React, { useEffect } from 'react';
import { useTextSelection } from 'ahooks';
import PropTypes from 'prop-types';

// 定义文字选中监听组件FefferyTextSelection
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

// 定义参数或属性
FefferyTextSelection.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 设置目标监听容器id
     */
    targetId: PropTypes.string,

    /**
     * 设置目标监听容器对应的css选择器
     */
    targetSelector: PropTypes.string,

    /**
     * 设置目标监听规则类型，可选的有'id'、'selector'
     * 默认：'id'
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

// 设置默认参数
FefferyTextSelection.defaultProps = {
    targetType: 'id'
}

export default FefferyTextSelection;