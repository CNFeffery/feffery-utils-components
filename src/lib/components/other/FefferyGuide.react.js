// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 组件核心
import Guide from 'byte-guide'
// 辅助库
import { isString } from 'lodash';

/**
 * 引导部件FefferyGuide
 */
const FefferyGuide = (props) => {
    let {
        id,
        className,
        style,
        key,
        locale,
        steps,
        localKey,
        closable,
        modalClassName,
        maskClassName,
        mask,
        arrow,
        hotspot,
        stepText,
        nextText,
        prevText,
        showPreviousBtn,
        okText,
        step,
        setProps,
        loading_state
    } = props;

    return (
        <Guide id={id}
            className={className}
            style={style}
            key={key}
            lang={locale}
            steps={steps}
            localKey={localKey}
            closable={closable}
            modalClassName={modalClassName}
            maskClassName={maskClassName}
            mask={mask}
            arrow={arrow}
            hotspot={hotspot}
            stepText={isString(stepText)
                ? eval(stepText) : stepText}
            nextText={nextText}
            prevText={prevText}
            showPreviousBtn={showPreviousBtn}
            okText={okText}
            step={step}
            onClose={() => {
                // 修复引导结束后页面整体无法滚动的问题
                document.documentElement.style.overflow = 'auto'
            }}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

FefferyGuide.propTypes = {

    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 当前组件css类名
     */
    className: PropTypes.string,

    /**
     * 设置语言，可选项有`'zh'`、`'en'`
     * 默认值：`'zh'`
     */
    locale: PropTypes.oneOf(['zh', 'en']),

    /**
     * 必填，用于构造每一步锚定的页面元素
     */
    steps: PropTypes.arrayOf(
        PropTypes.exact({
            /**
             * 对应当前步骤锚定的元素对应的`css`选择器
             */
            selector: PropTypes.string,

            /**
             * 当`selector`参数缺省时，可用`targetPos`参数基于绝对位置进行步骤锚定
             */
            targetPos: PropTypes.exact({
                /**
                 * 设置距离顶部的像素距离
                 */
                top: PropTypes.number,
                /**
                 * 设置距离左端的像素距离
                 */
                left: PropTypes.number,
                /**
                 * 设置锚定范围像素宽度
                 */
                width: PropTypes.number,
                /**
                 * 设置锚定范围像素高度
                 */
                height: PropTypes.number
            }),

            /**
             * 设置展示面板的标题内容
             */
            title: PropTypes.node,

            /**
             * 设置展示面板的描述内容
             */
            content: PropTypes.node,

            /**
             * 设置展示面板相对锚点的方位，可选项有`'top'`、`'bottom'`、`'left'`、`'right'`、`'top-left'`、`'top-right'`、`'bottom-left'`、`'bottom-right'`、`'left-top'`、`'left-bottom'`、`'right-top'`、`'right-bottom'`
             * 默认值：`'bottom'`
             */
            placement: PropTypes.oneOf([
                'top', 'bottom', 'left', 'right', 'top-left', 'top-right',
                'bottom-left', 'bottom-right', 'left-top', 'left-bottom',
                'right-top', 'right-bottom'
            ]),

            /**
             * 设置展示面板的像素偏移量
             */
            offset: PropTypes.exact({
                /**
                 * 水平方向偏移像素距离
                 */
                x: PropTypes.number,
                /**
                 * 竖直方向偏移像素距离
                 */
                y: PropTypes.number
            })
        })
    ).isRequired,

    /**
     * 用于设置本地缓存唯一标识`key`，从而辅助应用判断是否已展示过该引导页
     */
    localKey: PropTypes.string.isRequired,

    /**
     * 设置是否允许跳过引导
     * 默认值：`true`
     */
    closable: PropTypes.bool,

    /**
     * 弹窗css类名
     */
    modalClassName: PropTypes.string,

    /**
     * 蒙版层css类名
     */
    maskClassName: PropTypes.string,

    /**
     * 是否展示蒙版层
     * 默认值：`true`
     */
    mask: PropTypes.bool,

    /**
     * 展示面板是否添加箭头
     * 默认值：`true`
     */
    arrow: PropTypes.bool,

    /**
     * 展示面板是否展示热点标识
     * 默认值：`false`
     */
    hotspot: PropTypes.bool,

    /**
     * 自定义步骤信息展示内容的回调函数
     * 默认值：`"(stepIndex, stepCount) => { return '第${stepIndex}步，共${stepCount}步'; }"`
     */
    stepText: PropTypes.string,

    /**
     * “下一步”按钮文案信息
     */
    nextText: PropTypes.string,

    /**
     * “上一步”按钮文案信息
     */
    prevText: PropTypes.string,

    /**
     * 是否显示“上一步”按钮
     * 默认值：`true`
     */
    showPreviousBtn: PropTypes.bool,

    /**
     * 确认按钮的文案信息
     */
    okText: PropTypes.string,

    /**
     * 设置初始化时的起始步骤，为`-1`时则不显示引导组件
     * 默认值：`0`
     */
    step: PropTypes.number,

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
    setProps: PropTypes.func
};

FefferyGuide.defaultProps = {
    locale: 'zh',
    showPreviousBtn: true,
    mask: true
}

export default FefferyGuide;