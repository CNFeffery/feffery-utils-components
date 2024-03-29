import React from 'react';
import List from 'rc-virtual-list';
import PropTypes from 'prop-types';

const parseChildrenToArray = children => {
    if (children && !Array.isArray(children)) {
        return [children];
    }
    return children;
};

// 定义虚拟滚动组件FefferyVirtualList
const FefferyVirtualList = (props) => {
    // 取得必要属性或参数
    let {
        id,
        children,
        style,
        className,
        key,
        height,
        itemHeight,
        setProps,
        loading_state
    } = props;

    children = parseChildrenToArray(children);

    children = children || [];

    return (<List
        id={id}
        style={style}
        className={className}
        key={key}
        itemKey="virtual-list-id"
        height={height}
        itemHeight={itemHeight}
        data={children.map((_, index) => index)}
        children={(index) => children[index]}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />);
}

// 定义参数或属性
FefferyVirtualList.propTypes = {
    /**
     * 组件id
     */
    id: PropTypes.string,

    /**
     * 组件子元素
     */
    children: PropTypes.node,

    /**
     * 设置css样式
     */
    style: PropTypes.object,

    /**
     * 设置css类名
     */
    className: PropTypes.string,

    /**
     * 辅助刷新用唯一标识key值
     */
    key: PropTypes.string,

    /**
     * 虚拟化区域像素高度
     */
    height: PropTypes.number.isRequired,

    /**
     * 每个子元素区域的像素高度
     */
    itemHeight: PropTypes.number.isRequired,

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
FefferyVirtualList.defaultProps = {
}

export default FefferyVirtualList;