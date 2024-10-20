// react核心
import React, { useRef, useEffect } from 'react';
import PropTypes from 'prop-types';
// 组件核心
import { useInViewport } from 'ahooks';
// 辅助库
import { isUndefined } from 'lodash';

/**
 * 元素可见性检查组件FefferyInViewport
 */
const FefferyInViewport = (props) => {
    const {
        id,
        inViewport,
        threshold,
        children,
        style,
        className,
        setProps,
        loading_state
    } = props;

    const ref = useRef(null);

    const [_inViewport, ratio] = useInViewport(ref, {
        threshold: threshold
    });

    useEffect(() => {
        // 若设置了阈值
        if (!isUndefined(threshold)) {
            // 本身可见的元素，可见部分比例开始小于阈值时
            if (inViewport && ratio < threshold) {
                setProps({
                    inViewport: false
                })
            }
            // 本身不可见的元素，可见部分比例开始大于等于阈值时
            else if (!inViewport && ratio >= threshold) {
                setProps({
                    inViewport: true
                })
            }
        } else {
            setProps({
                inViewport: _inViewport
            })
        }
    }, [_inViewport, ratio])

    return (<div
        id={id}
        style={style}
        className={className}
        children={children}
        ref={ref}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />);
}

FefferyInViewport.propTypes = {
    /**
     * 组件唯一id
     */
    id: PropTypes.string,

    /**
     * 对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果
     */
    key: PropTypes.string,

    /**
     * 组件型，需要进行可见性监听的目标元素
     */
    children: PropTypes.node,

    /**
     * 监听当前元素是否出现在可视范围内
     */
    inViewport: PropTypes.bool,

    /**
     * 触发元素可见性状态切换的比例阈值
     */
    threshold: PropTypes.number,

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

FefferyInViewport.defaultProps = {
}

export default FefferyInViewport;