import { useAutoAnimate } from '@formkit/auto-animate/react';
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { propTypes, defaultProps } from '../../components/animations/FefferyAutoAnimate.react';

/**
 * 自动动画组件FefferyAutoAnimate
 */
const FefferyAutoAnimate = (props) => {
    // 取得必要属性或参数
    const {
        id,
        key,
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
            key={key}
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

export default FefferyAutoAnimate;

FefferyAutoAnimate.defaultProps = defaultProps;
FefferyAutoAnimate.propTypes = propTypes;