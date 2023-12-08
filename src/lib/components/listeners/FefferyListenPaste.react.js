import { useEffect, useCallback } from 'react';
import { useHover } from 'ahooks';
import PropTypes from 'prop-types';

// 定义全局粘贴监听组件FefferyListenPaste
const FefferyListenPaste = (props) => {
    let {
        pasteCount,
        enableListenPaste,
        targetContainerId,
        setProps,
        loading_state
    } = props;

    const isHovering = useHover(() => document.getElementById(targetContainerId));

    // 用于全局监听文本粘贴事件
    const handlePaste = useCallback((event) => {
        // 当enableListenPaste为true时会强制监听事件
        // 当enableListenPaste为false时，会结合是否定义了targetContainerId
        // 以及目标容器是否处于鼠标悬停状态来决定是否监听事件
        if (enableListenPaste || (targetContainerId && isHovering)) {
            const clipboardData = event.clipboardData;
            const pastedData = clipboardData.getData('text');
            if (pastedData) {
                setProps({
                    pasteText: pastedData,
                    pasteCount: pasteCount + 1
                })
            }
        }
    }, [pasteCount, enableListenPaste, targetContainerId, isHovering])

    useEffect(() => {

        document.addEventListener('paste', handlePaste);
        return () => {
            document.removeEventListener('paste', handlePaste);
        };
    }, [handlePaste]);

    return <></>;
}

// 定义参数或属性
FefferyListenPaste.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 监听最近一次文本粘贴事件对应的粘贴内容
     */
    pasteText: PropTypes.string,

    /**
     * 监听累计监听到的粘贴事件发生次数
     * 默认：0
     */
    pasteCount: PropTypes.number,

    /**
     * 用于设置是否为当前组件启用粘贴事件监听
     * 默认：false
     */
    enableListenPaste: PropTypes.bool,

    /**
     * 用于设置要监听绑定的目标容器id，设置此参数后，粘贴事件监听仅在目标容器被鼠标悬停时生效
     */
    targetContainerId: PropTypes.string,

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
FefferyListenPaste.defaultProps = {
    pasteCount: 0,
    enableListenPaste: false
}

export default FefferyListenPaste;