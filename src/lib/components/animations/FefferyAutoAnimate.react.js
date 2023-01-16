import { useAutoAnimate } from '@formkit/auto-animate/react'
import useCss from '../../hooks/useCss'
import { isString } from 'lodash';
import PropTypes from 'prop-types';

// 定义自动动画组件FefferyAutoAnimate，api参数参考：https://github.com/formkit/auto-animate
const FefferyAutoAnimate = (props) => {
    // 取得必要属性或参数
    const {
        id,
        children,
        style,
        className,
        duration,
        easing,
        setProps,
        loading_state
    } = props;

    const [parent, enableAnimations] = useAutoAnimate({
        duration: duration * 1000,
        easing: easing
    })

    return (
        <div
            id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            ref={parent}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } >
            {children}
        </div>
    );
}

// 定义参数或属性
FefferyAutoAnimate.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 要进行动画效果编排的目标元素
    children: PropTypes.node,

    // css样式
    style: PropTypes.object,

    // css类名
    className: PropTypes.string,

    // 配置动画时长，单位：秒
    // 默认为0.25
    duration: PropTypes.number,

    // 设置过渡动画函数，同css中的easing-function，默认为'ease-in-out'
    easing: PropTypes.string,

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
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyAutoAnimate.defaultProps = {
    duration: 0.25,
    easing: 'ease-in-out'
}

export default FefferyAutoAnimate;