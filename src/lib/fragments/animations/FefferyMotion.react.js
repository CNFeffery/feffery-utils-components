import { motion } from "framer-motion";
import useCss from '../../hooks/useCss'
import { isString } from 'lodash';
import { propTypes, defaultProps } from "../../components/animations/FefferyMotion.react";

// 定义动画编排组件FefferyMotion，api参数参考：https://github.com/framer/motion
// 备注：
// 1.针对style、initial、animate等接受样式定义的参数，除了标准的css属性外，还额外可用以下快捷方式属性：
// 位置移动类：x、y、z、translateX、translateY、translateZ
// 缩放类：scale、scaleX、scaleY
// 旋转类：rotate、rotateX、rotateY、rotateZ
// 倾斜类：skew、skewX、skewY
// 透视类：transformPerspective
// 元素变形原点：originX、originY、originZ
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
        setProps,
        loading_state
    } = props;

    // 针对transition.repeat为'infinity'时进行特殊处理
    if (transition && transition.repeat && transition.repeat === 'infinity') {
        transition.repeat = Infinity
    }

    return (
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
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } >
            {children}
        </motion.div>
    );
}

export default FefferyMotion;

FefferyMotion.defaultProps = defaultProps;
FefferyMotion.propTypes = propTypes;