import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyMotion = React.lazy(() => import(/* webpackChunkName: "feffery_motion" */ '../../fragments/animations/FefferyMotion.react'));

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
    destroyWhenAnimated = false,
    setProps,
    ...others
}) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyMotion {
                ...{
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
                    ...others
                }
            } />
        </Suspense>
    );
}

FefferyMotion.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，要进行动画效果编排的目标元素
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * 设置当前组件初始化样式，传入`false`时用于禁用初始化动画，传入字符串时用于设置样式组别名
     */
    initial: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.bool,
        PropTypes.string
    ]),

    /**
     * 设置从初始状态进行转化的目标样式，传入字符串时用于设置样式组别名
     */
    animate: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.string
    ]),

    /**
     * 设置当前元素从页面卸载时的目标样式，传入字符串时用于设置样式组别名
     */
    exit: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.string
    ]),

    /**
     * 设置鼠标悬停时的目标样式，传入字符串时用于设置样式组别名
     */
    whileHover: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.string
    ]),

    /**
     * 设置鼠标点按时的目标样式，传入字符串时用于设置样式组别名
     */
    whileTap: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.string
    ]),

    /**
     * 配置过渡动画相关参数
     * 默认为：`{type: "spring", damping: 10, stiffness: 100}`
     */
    transition: PropTypes.exact({
        /**
         * 设置过渡动画的开始延时时长，单位：秒
         * 默认：`0`
         */
        delay: PropTypes.number,

        /**
         * 设置动画重复次数，特殊的，`'infinity'`表示无限循环
         */
        repeat: PropTypes.oneOfType([
            PropTypes.number,
            PropTypes.oneOf(['infinity'])
        ]),

        /**
         * 设置动画的重复方式，可选的有`'loop'`、`'reverse'`、`'mirror'`
         */
        repeatType: PropTypes.oneOf(['loop', 'reverse', 'mirror']),

        /**
         * 设置动画每次重复的延时，单位：秒
         */
        repeatDelay: PropTypes.number,

        /**
         * 动画过渡类型，可选的有`'spring'`（弹簧运动型）、`'tween'`（补间型）
         * 默认：'tween'
         */
        type: PropTypes.oneOf(['spring', 'tween']),

        /**
         * 设置过渡动画时长，单位：秒
         */
        duration: PropTypes.number,

        /**
         * `transition.type='tween'`时，用于设置过渡动画函数，可选的有`'linear'`、`'easeIn'`、`'easeOut'`、`'easeInOut'`、`'circIn'`、`'circOut'`、`'circInOut'`、`'backIn'`、`'backOut'`、`'backInOut'`、`'anticipate'`
         */
        ease: PropTypes.oneOf([
            'linear', 'easeIn', 'easeOut', 'easeInOut',
            'circIn', 'circOut', 'circInOut', 'backIn',
            'backOut', 'backInOut', 'anticipate'
        ]),

        /**
         * 针对分段过渡动画设置每段的时长比例，以`duration`为`1`单位
         */
        times: PropTypes.arrayOf(PropTypes.number)
    }),

    /**
     * 设置当前组件进入视口后的目标样式，传入字符串时用于设置样式组别名
     */
    whileInView: PropTypes.oneOfType([
        PropTypes.object,
        PropTypes.string
    ]),

    /**
     * 配置视口检测相关参数
     */
    viewport: PropTypes.exact({
        /**
         * 设置是否只进行一次视口检测，当设置为`true`时，当前元素进入视口后将维持`whileInView`所设置的样式
         * 默认：`false`
         */
        once: PropTypes.bool,

        /**
         * 设置用于辅助进行目标元素视口检测的外边界提前量，可设置例如`'200px'`统一为上右下左添加外边界，也可设置例如`'0px -20px 0px 100px'`分别控制不同方向
         * 默认：`'0px'`
         */
        margin: PropTypes.string,

        /**
         * 设置元素移入视口检测策略，设置为`'some'`时表示元素部分进入视口则视作进入，设置为`'all'`时表示元素全部进入视口才视作进入
         */
        amount: PropTypes.oneOf(['some', 'all'])
    }),

    /**
     * 用于编排具有别名的样式组
     */
    variants: PropTypes.objectOf(PropTypes.object),

    /**
     * 监听当前组件的`animate`目标动画过程是否已完成
     */
    animated: PropTypes.bool,

    /**
     * 是否在动画完成后销毁当前组件
     * 默认值：`false`
     */
    destroyWhenAnimated: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

export default FefferyMotion;

export const propTypes = FefferyMotion.propTypes;
export const defaultProps = FefferyMotion.defaultProps;