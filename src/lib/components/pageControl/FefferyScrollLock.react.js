// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useScrollLock } from '@reactuses/core';
// 辅助库
import { isUndefined } from 'lodash';

/**
 * 滚动锁定组件FefferyScrollLock
 */
const FefferyScrollLock = ({
    target,
    locked = false,
    setProps
}) => {

    const [_locked, setLocked] = useScrollLock(target ? document.getElementById(target) : document.body);

    useEffect(() => {
        if (setLocked && !isUndefined(locked)) {
            // 更新滚动锁定状态
            setLocked(locked);
        }
    }, [locked])

    return <></>;
}

FefferyScrollLock.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 设置滚动锁定目标元素`id`，默认将锁定整个页面
     */
    target: PropTypes.string,

    /**
     * 设置针对目标是否开启滚动锁定
     * 默认值：`false`
     */
    locked: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyScrollLock;