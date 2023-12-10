import { useEffect } from 'react';
import { useMouse } from 'ahooks';
import PropTypes from 'prop-types';

// 定义鼠标位置监听组件FefferyMousePosition
const FefferyMousePosition = (props) => {
    let {
        setProps,
        loading_state
    } = props;

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

// 定义参数或属性
FefferyMousePosition.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 监听当前鼠标位置相关信息
     */
    position: PropTypes.object,

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
FefferyMousePosition.defaultProps = {
}

export default FefferyMousePosition;