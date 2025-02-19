// 组件核心
import { useAutoAnimate } from '@formkit/auto-animate/react';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/animations/FefferyAutoAnimate.react';

/**
 * 自动动画组件FefferyAutoAnimate
 */
const FefferyAutoAnimate = ({
    id,
    children,
    style,
    className,
    duration,
    easing,
    setProps
}) => {

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
            data-dash-is-loading={useLoading()} >
            {children}
        </div>
    );
}

export default FefferyAutoAnimate;

FefferyAutoAnimate.defaultProps = defaultProps;
FefferyAutoAnimate.propTypes = propTypes;