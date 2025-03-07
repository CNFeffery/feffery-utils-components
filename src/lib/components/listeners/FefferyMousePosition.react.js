// react核心
import { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useMouse } from 'ahooks';

/**
 * 鼠标位置监听组件FefferyMousePosition
 */
const FefferyMousePosition = ({
    setProps
}) => {

    const mouse = useMouse();

    useEffect(() => {
        if (mouse) {
            setProps({
                position: {
                    screenX: mouse.screenX,
                    screenY: mouse.screenY,
                    clientX: mouse.clientX,
                    clientY: mouse.clientY,
                    pageX: mouse.pageX,
                    pageY: mouse.pageY
                }
            })
        }
    }, [mouse])

    return <></>;
}

FefferyMousePosition.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 监听当前鼠标位置相关信息
     */
    position: PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyMousePosition;