import React from 'react';
import List from 'rc-virtual-list';

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
        height,
        itemHeight,
        setProps,
        loading_state
    } = props;

    children = parseChildrenToArray(children);

    return (<List
        id={id}
        style={style}
        className={className}
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
    // 部件id
    id: PropTypes.string,

    children: PropTypes.node,

    style: PropTypes.object,

    className: PropTypes.string,

    height: PropTypes.number,

    itemHeight: PropTypes.number,

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

export default React.memo(FefferyVirtualList);