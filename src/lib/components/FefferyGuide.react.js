import React from 'react';
import Guide from 'byte-guide'
import './styles.css'

// 定义引导部件FefferyGuide，api参数参考https://github.com/bytedance/guide/blob/main/README.zh-CN.md
const FefferyGuide = (props) => {
    // 取得必要属性或参数
    let {
        id,
        className,
        style,
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
    } = props;

    // 返回向页面注入的快捷键监听
    return (
        <Guide id={id}
            className={className}
            style={style}
            lang={locale}
            steps={steps}
            localKey={localKey}
            closable={closable}
            modalClassName={modalClassName}
            maskClassName={maskClassName}
            mask={mask}
            arrow={arrow}
            hotspot={hotspot}
            stepText={typeof stepText === typeof ''
                ? eval(stepText) : stepText}
            nextText={nextText}
            prevText={prevText}
            showPreviousBtn={showPreviousBtn}
            okText={okText}
            step={step} />
    );
}

// 定义参数或属性
FefferyGuide.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置语言，可选的有'en'、'zh'
    locale: PropTypes.oneOf(['zh', 'en']),

    // 必填，用于构造每一步锚定的页面元素
    steps: PropTypes.arrayOf(
        PropTypes.exact({
            // 对应当前步骤锚定的元素对应的css选择器
            selector: PropTypes.string,

            // 当selector参数缺省时，可用targetPos参数基于绝对位置进行步骤锚定
            targetPos: PropTypes.exact({
                // 设置距离顶部的像素距离
                top: PropTypes.number,
                // 设置距离左端的像素距离
                left: PropTypes.number,
                // 设置锚定范围像素宽度
                width: PropTypes.number,
                // 设置锚定范围像素高度
                height: PropTypes.number
            }),

            // 设置展示面板的标题内容
            title: PropTypes.string,

            // 设置展示面板的描述内容
            content: PropTypes.string,

            // 设置展示面板相对锚点的方位，可选的有'bottom-left'、'left-bottom'、'bottom'，默认为'bottom'
            placement: PropTypes.oneOf([
                'bottom-left', 'left-bottom', 'bottom'
            ]),

            // 设置展示面板的像素偏移量
            offset: PropTypes.exact({
                // 水平方向偏移像素距离
                x: PropTypes.number,
                // 竖直方向偏移像素距离
                y: PropTypes.number
            })
        })
    ).isRequired,

    // 用于设置本地缓存唯一标识key，从而辅助应用判断是否已展示过该引导页
    localKey: PropTypes.string.isRequired,

    // 设置是否允许跳过引导，默认为true
    closable: PropTypes.bool,

    // 设置展示面板的类名
    modalClassName: PropTypes.string,

    // 设置蒙版层的类名
    maskClassName: PropTypes.string,

    // 设置是否展示蒙板层，默认为true
    mask: PropTypes.bool,

    // 设置展示面板是否添加箭头，默认为true
    arrow: PropTypes.bool,

    // 设置展示面板是否展示热点，默认为false
    hotspot: PropTypes.bool,

    // 自定义步骤信息展示内容的回调函数，默认为"(stepIndex, stepCount) => { return '第${stepIndex}步，共${stepCount}步'; }"
    stepText: PropTypes.string,

    // 设置“下一步”按钮的文案信息
    nextText: PropTypes.string,

    // 设置“上一步”按钮的文案信息
    prevText: PropTypes.string,

    // 设置是否显示“上一步”按钮，默认为true
    showPreviousBtn: PropTypes.bool,

    // 设置确认按钮的文案信息
    okText: PropTypes.string,

    // 设置初始化时的起始步骤，为-1时则不显示引导组件，默认为0
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

// 设置默认参数
FefferyGuide.defaultProps = {
    locale: 'zh',
    showPreviousBtn: true
}

export default FefferyGuide;