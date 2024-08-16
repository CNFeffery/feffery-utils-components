import React from 'react';
import { ReactCompareSlider, ReactCompareSliderHandle } from 'react-compare-slider';
import PropTypes from 'prop-types';

// 定义卷帘比较组件FefferyCompare
const FefferyCompareSlider = (props) => {
    // 取得必要属性或参数
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
    // 组件id
    id: PropTypes.string,

    // css样式
    style: PropTypes.object,

    // css类名
    className: PropTypes.string,

    // 设置进行比较的第一个元素
    firstItem: PropTypes.node,

    // 设置进行比较的第二个元素
    secondItem: PropTypes.node,

    // 设置或监听当前卷帘比较组件的卷帘位置百分比，取值应在0到100之间，默认为50
    position: PropTypes.number,

    // 设置是否仅拖拽控件部分可用于调整卷帘，默认为true
    onlyHandleDraggable: PropTypes.bool,

    // 设置卷帘移动到两侧时，进行留白的像素距离，默认为0
    boundsPadding: PropTypes.number,

    // 设置卷帘方向，可选的有'horizontal'和'vertical'，默认为'horizontal'
    direction: PropTypes.oneOf(['horizontal', 'vertical']),

    // 针对拖拽控件设置相关样式参数
    /**
     * 设置拖拽控件按钮部分的css样式
     */
    buttonStyle: PropTypes.object,

    /**
     * 设置拖拽控件线条部分的css样式
     */
    linesStyle: PropTypes.object,

    /**
     * 设置拖拽控件根元素部分的css样式
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

// 设置默认参数
FefferyCompareSlider.defaultProps = {
    position: 50,
    onlyHandleDraggable: true,
    boundsPadding: 0,
    direction: 'horizontal',
}

export default React.memo(FefferyCompareSlider);