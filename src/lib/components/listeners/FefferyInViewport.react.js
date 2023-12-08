import React, { useRef, useEffect } from 'react';
import { useInViewport } from 'ahooks';
import { isUndefined } from 'lodash';
import PropTypes from 'prop-types';

// 定义元素可见性检查组件FefferyInViewport
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

// 定义参数或属性
FefferyInViewport.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 需要进行可见性监听的目标元素
     */
    children: PropTypes.node,

    /**
     * 监听当前元素是否出现在可视范围内
     */
    inViewport: PropTypes.bool,

    /**
     * 用于设置触发元素可见性状态切换的比例阈值
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

// 设置默认参数
FefferyInViewport.defaultProps = {
}

export default FefferyInViewport;