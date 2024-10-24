// react核心
import React from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { ReactCompareSlider, ReactCompareSliderHandle } from 'react-compare-slider';

/**
 * 卷帘比较组件FefferyCompareSlider
 */
const FefferyCompareSlider = (props) => {
    const {
        id,
        style,
        className,
        firstItem,
        secondItem,
        position,
        onlyHandleDraggable,
        boundsPadding,
        direction,
        buttonStyle,
        linesStyle,
        rootStyle,
        setProps,
        loading_state
    } = props;

    return (
        <ReactCompareSlider
            id={id}
            style={style}
            className={className}
            itemOne={firstItem}
            itemTwo={secondItem}
            position={position}
            onlyHandleDraggable={onlyHandleDraggable}
            boundsPadding={boundsPadding}
            portrait={direction === 'vertical'}
            onPositionChange={(e) => setProps({ position: e })}
            handle={
                <ReactCompareSliderHandle
                    buttonStyle={buttonStyle}
                    linesStyle={linesStyle}
                    style={rootStyle}
                    portrait={direction === 'vertical'} />
            }
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

// 定义参数或属性
FefferyCompareSlider.propTypes = {
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
     * 组件型，设置进行比较的第一个元素
     */
    firstItem: PropTypes.node,

    /**
     * 组件型，设置进行比较的第二个元素
     */
    secondItem: PropTypes.node,

    /**
     * 设置或监听当前卷帘比较组件的卷帘位置百分比，取值在`0`到`100`之间
     * 默认值：`50`
     */
    position: PropTypes.number,

    /**
     * 是否仅拖拽控件部分可用于调整卷帘
     * 默认值：`true`
     */
    onlyHandleDraggable: PropTypes.bool,

    /**
     * 设置卷帘移动到两侧时，进行留白的像素距离
     * 默认值：`0`
     */
    boundsPadding: PropTypes.number,

    /**
     * 设置卷帘方向，可选项有`'horizontal'`、`'vertical'`
     * 默认值：`'horizontal'`
     */
    direction: PropTypes.oneOf(['horizontal', 'vertical']),

    /**
     * 拖拽控件按钮部分`css`样式
     */
    buttonStyle: PropTypes.object,

    /**
     * 拖拽控件线条部分`css`样式
     */
    linesStyle: PropTypes.object,

    /**
     * 拖拽控件根元素部分`css`样式
     */
    rootStyle: PropTypes.object,

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

FefferyCompareSlider.defaultProps = {
    position: 50,
    onlyHandleDraggable: true,
    boundsPadding: 0,
    direction: 'horizontal',
}

export default React.memo(FefferyCompareSlider);