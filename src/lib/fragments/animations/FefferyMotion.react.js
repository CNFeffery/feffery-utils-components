import { motion } from "framer-motion";
import useCss from '../../hooks/useCss'
import { isString } from 'lodash';
import { propTypes, defaultProps } from "../../components/animations/FefferyMotion.react";

/**
 * 动画编排组件FefferyMotion
 */
const FefferyMotion = (props) => {
    // 取得必要属性或参数
    const {
        id,
        children,
        style,
        className,
        key,
        initial,
        animate,
        exit,
        whileHover,
        whileTap,
        transition,
        whileInView,
        viewport,
        variants,
        animated,
        destroyWhenAnimated,
        setProps,
        loading_state
    } = props;

    // 针对transition.repeat为'infinity'时进行特殊处理
    if (transition && transition.repeat && transition.repeat === 'infinity') {
        transition.repeat = Infinity
    }

    return (
        destroyWhenAnimated && animated ?
            null :
            (
                <motion.div
                    id={id}
                    className={
                        isString(className) ?
                            className :
                            (className ? useCss(className) : undefined)
                    }
                    style={style}
                    key={key}
                    initial={initial}
                    animate={animate}
                    exit={exit}
                    whileHover={whileHover}
                    whileTap={whileTap}
                    transition={transition}
                    whileInView={whileInView}
                    viewport={viewport}
                    variants={variants}
                    onAnimationComplete={() => setProps({ animated: true })}
                    data-dash-is-loading={
                        (loading_state && loading_state.is_loading) || undefined
                    } >
                    {children}
                </motion.div>
            )
    );
}

export default FefferyMotion;

FefferyMotion.defaultProps = defaultProps;
FefferyMotion.propTypes = propTypes;