// react核心
import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import LazyLoad from 'react-lazyload';
// 辅助库
import { useLoading } from '../utils';


/**
 * FefferyLazyLoad wraps children with react-lazyload to support setProps
 */
const LazyLoadChildren = ({ children, setProps }) => {
    useEffect(() => {
        setProps({ visible: true });
    }, []);

    return <div className="lazyload-children">{children}</div>;
};

/**
 * 懒加载容器组件 FefferyLazyLoad
 */
const FefferyLazyLoad = ({
    id,
    children,
    style,
    className,
    key,
    height,
    offset,
    throttle,
    debounce,
    once,
    overflow,
    resize,
    scroll,
    placeholder,
    scrollContainer,
    unmountIfInvisible,
    visible = false,
    setProps
}) => {
    return (
        <LazyLoad
            id={id}
            style={style}
            className={className}
            key={key}
            height={height}
            offset={offset}
            throttle={throttle}
            once={once}
            overflow={overflow}
            resize={resize}
            scroll={scroll}
            debounce={debounce}
            placeholder={placeholder}
            scrollContainer={scrollContainer}
            unmountIfInvisible={unmountIfInvisible}
            data-dash-is-loading={useLoading()}
        >
            <LazyLoadChildren setProps={setProps}>
                {children}
            </LazyLoadChildren>
        </LazyLoad>
    );
};


FefferyLazyLoad.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 组件型，设置内嵌元素内容
     */
    children: PropTypes.node,

    /**
     * 当前组件css样式
     */
    style: PropTypes.object,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * Height of the component placeholder on the first render.
     * Can be a number or a string like '100%'.
     * Helps LazyLoad calculate visibility more precisely.
     */
    height: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),

    /**
     * Preload or delay load a component based on its distance from the viewport.
     * Can be a number (applied to both left and top) or an array [leftOffset, topOffset].
     */
    offset: PropTypes.oneOfType([
        PropTypes.number,
        PropTypes.arrayOf(PropTypes.number)
    ]),

    /**
     * 当前组件css类名，支持[动态css](/advanced-classname)
     */
    className: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    /**
     * Enable built-in debounce or throttle for scroll/resize events.
     * Can be a number (milliseconds to wait) or true (defaults to 300ms).
     * NOTICE: Apply this prop consistently to all LazyLoad components.
     */
    throttle: PropTypes.number,
    debounce: PropTypes.bool,

    /**
     * If true, LazyLoad will load the component only once and stop listening to scroll/resize events.
     * Useful for images or simple components.
     */
    once: PropTypes.bool,

    /**
     * If true, LazyLoad works inside overflow containers.
     * Make sure the container has a position property other than static.
     */
    overflow: PropTypes.bool,

    /**
     * If true, listen and react to resize events.
     * Important for supporting legacy IE carefully.
     */
    resize: PropTypes.bool,

    /**
     * If true, listen and react to scroll events.
     */
    scroll: PropTypes.bool,

    /**
     * Specify a placeholder for the lazy loaded component.
     * Remember to set appropriate height or minHeight for better performance.
     */
    placeholder: PropTypes.node,

    /**
     * Pass a query selector string the scroll container.
     * If not provided, LazyLoad will attach to the window's scroll events.
     */
    scrollContainer: PropTypes.string,

    /**
     * If true, unmount the lazy loaded component when it is no longer visible.
     * Placeholder will be rendered instead.
     */
    unmountIfInvisible: PropTypes.bool,

    /**
     * 监听容器是否已出现在用户视图中
     */
    visible: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FefferyLazyLoad;