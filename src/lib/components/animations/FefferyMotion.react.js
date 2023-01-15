import { motion } from "framer-motion";
import useCss from '../../hooks/useCss'
import { isString } from 'lodash';
import PropTypes from 'prop-types';

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

// 定义参数或属性
FefferyMotion.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 要进行动画效果编排的目标元素
    children: PropTypes.node,

    // css样式
    style: PropTypes.object,

    // css类名
    className: PropTypes.string,

    // 设置当前组件初始化时的样式
    initial: PropTypes.oneOfType([
        PropTypes.object,
        // 设置为false用于禁用初始化动画
        PropTypes.bool,
        // 传递单个样式组的别名
        PropTypes.string
    ]),

    // 设置从初始状态进行转化的目标样式
    animate: PropTypes.oneOfType([
        PropTypes.object,
        // 传递单个样式组的别名
        PropTypes.string
    ]),

    // 设置当前元素从页面卸载时的目标样式
    exit: PropTypes.oneOfType([
        PropTypes.object,
        // 传递单个样式组的别名
        PropTypes.string
    ]),

    // 设置鼠标悬停时的目标样式
    whileHover: PropTypes.oneOfType([
        PropTypes.object,
        // 传递单个样式组的别名
        PropTypes.string
    ]),

    // 设置鼠标点按时的目标样式
    whileTap: PropTypes.oneOfType([
        PropTypes.object,
        // 传递单个样式组的别名
        PropTypes.string
    ]),

    // 配置过渡动画
    // 默认为：
    // {
    //     type: "spring",
    //     damping: 10,
    //     stiffness: 100
    // }
    transition: PropTypes.exact({
        // 设置过渡动画的开始延时时长，单位：秒，默认为0
        delay: PropTypes.number,

        // 设置动画重复次数，特殊的，'infinity'表示无限循环
        repeat: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.oneOf(['infinity'])
        ]),

        // 设置动画的重复方式，可选的有'loop'、'reverse'、'mirror'
        repeatType: PropTypes.oneOf(['loop', 'reverse', 'mirror']),

        // 设置动画每次重复的延时，单位：秒
        repeatDelay: PropTypes.number,

        // 动画过渡类型
        // 可选的有'spring'（弹簧运动型）、'tween'（补间型）
        // 默认为'tween'
        type: PropTypes.oneOf(['spring', 'tween']),

        // 设置过渡动画时长，单位：秒
        duration: PropTypes.number,

        // transition.type='tween'时，用于设置过渡动画函数
        // 可选的有'linear'、'easeIn'、'easeOut'、
        // 'easeInOut'、'circIn'、'circOut'、'circInOut'、'backIn'、
        // 'backOut'、'backInOut'、'anticipate'
        ease: PropTypes.oneOf([
            'linear', 'easeIn', 'easeOut', 'easeInOut',
            'circIn', 'circOut', 'circInOut', 'backIn',
            'backOut', 'backInOut', 'anticipate'
        ]),

        // 针对分段过渡动画设置每段的时长比例
        // 以duration为1单位
        times: PropTypes.arrayOf(PropTypes.number)
    }),

    // 设置当前组件进入视口后的目标样式
    whileInView: PropTypes.oneOfType([
        PropTypes.object,
        // 传递单个样式组的别名
        PropTypes.string
    ]),

    // 配置视口检测
    viewport: PropTypes.exact({
        // 设置是否只进行一次视口检测，默认为false
        // 当设置为true时，当前元素进入视口后将维持whileInView所设置的样式
        once: PropTypes.bool,

        // 设置用于辅助进行目标元素视口检测的外边界提前量
        // 可设置例如"200px"统一为上右下左添加外边界
        // 也可设置例如"0px -20px 0px 100px"分别控制不同方向
        // 默认为"0px"
        margin: PropTypes.string,

        // 设置元素移入视口检测策略
        // 设置为"some"时表示元素部分进入视口则视作进入
        // 设置为"all"时表示元素全部进入视口才视作进入
        amount: PropTypes.oneOf(['some', 'all'])
    }),

    // 用于编排具有别名的样式组
    variants: PropTypes.object,

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
FefferyMotion.defaultProps = {
}

export default FefferyMotion;