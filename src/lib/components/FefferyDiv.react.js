import React, { useEffect, useCallback } from 'react';
import { useResizeDetector } from 'react-resize-detector';

// 定义进阶div容器组件FefferyDiv
const FefferyDiv = (props) => {
    // 取得必要属性或参数
    const {
        id,
        children,
        style,
        className,
        setProps,
        loading_state
    } = props;

    const onResize = useCallback(() => {
    }, []);

    const { width, height, ref } = useResizeDetector({ onResize });

    useEffect(() => {
        // 监听div容器尺寸变化从而刷新_width，_height属性值
        setProps({
            _width: width,
            _height: height
        });
    }, [width, height]);

    return <div
        id={id}
        style={style}
        className={className}
        ref={ref}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >
        {children}
    </ div>;
}


// 定义参数或属性
FefferyDiv.propTypes = {
    // 部件id
    id: PropTypes.string,

    children: PropTypes.node,

    style: PropTypes.object,

    className: PropTypes.string,

    // 监听容器像素宽度变化
    _width: PropTypes.number,

    // 监听容器像素高度变化
    _height: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,

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
    })
};

// 设置默认参数
FefferyDiv.defaultProps = {
}

export default FefferyDiv;