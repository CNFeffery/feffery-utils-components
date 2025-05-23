// react核心
import { useEffect, useCallback } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useHover } from 'ahooks';

/**
 * 全局粘贴监听组件FefferyListenPaste
 */
const FefferyListenPaste = ({
    pasteCount = 0,
    enableListenPaste = false,
    targetContainerId,
    setProps
}) => {

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

FefferyListenPaste.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听最近一次文本粘贴事件对应的粘贴内容
     */
    pasteText: PropTypes.string,

    /**
     * 监听累计监听到的粘贴事件发生次数
     * 默认值：`0`
     */
    pasteCount: PropTypes.number,

    /**
     * 用于设置是否为当前组件启用粘贴事件监听
     * 默认值：`false`
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
    setProps: PropTypes.func
};

export default FefferyListenPaste;