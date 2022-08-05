import React, { useRef, useEffect } from 'react';
import { useInViewport } from 'ahooks';

// 定义元素可见检查组件FefferyInViewport
const FefferyInViewport = (props) => {

    const ref = useRef(null);

    const [_inViewport] = useInViewport(ref);

    useEffect(() => {
        console.log(_inViewport)
        setProps({
            inViewport: _inViewport
        })
    }, [_inViewport])

    // 取得必要属性或参数
    let {
        id,
        children,
        style,
        className,
        setProps,
        loading_state
    } = props;

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
    // 部件id
    id: PropTypes.string,

    children: PropTypes.node,

    // 监听当前元素是否出现在可视范围内
    inViewport: PropTypes.bool,

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

export default React.memo(FefferyInViewport);