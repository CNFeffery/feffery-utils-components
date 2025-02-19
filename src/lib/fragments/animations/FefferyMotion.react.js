// 组件核心
import { motion } from "framer-motion";
// 辅助库
import useCss from '../../hooks/useCss'
import { isString } from 'lodash';
import { useLoading } from "../../components/utils";
// 参数类型
import { propTypes, defaultProps } from "../../components/animations/FefferyMotion.react";

/**
 * 动画编排组件FefferyMotion
 */
const FefferyMotion = ({
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
    setProps
}) => {

    // 针对transition.repeat为'infinity'时进行特殊处理
    if (transition && transition.repeat && transition.repeat === 'infinity') {
        transition.repeat = Infinity
    }

    const component_loading = useLoading();

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
                    data-dash-is-loading={component_loading} >
                    {children}
                </motion.div>
            )
    );
}

export default FefferyMotion;

FefferyMotion.defaultProps = defaultProps;
FefferyMotion.propTypes = propTypes;