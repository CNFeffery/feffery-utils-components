import React, { useEffect } from 'react';
import { sortableContainer, sortableElement } from 'react-sortable-hoc';
import PropTypes from 'prop-types';
import { arrayMoveImmutable } from 'array-move';
import { useCss } from 'react-use';
import { isString } from 'lodash';

const SortableContainer = sortableContainer((props) => {
    return <div {...props} />;
});

const SortableItem = sortableElement((props) => <div {...props} />);

// 定义排序容器组件FefferySortableContainer
const FefferySortableContainer = (props) => {
    let {
        id,
        children,
        style,
        className,
        helperClassName,
        orders,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        if (children) {
            setProps({
                orders: children.map((_, index) => index)
            })
        }
    }, [])

    const onSortEnd = ({ oldIndex, newIndex }) => {
        setProps({
            orders: arrayMoveImmutable(orders, oldIndex, newIndex)
        })
    };

    return (<SortableContainer
        id={id}
        style={style}
        className={className}
        helperClass={isString(helperClassName) ? helperClassName : useCss(helperClassName)}
        onSortEnd={onSortEnd}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } >
        {orders.map((order, index) => <SortableItem index={index} children={children[order]} />)}
    </SortableContainer>);
};

// 定义参数或属性
FefferySortableContainer.propTypes = {

    children: PropTypes.node,

    id: PropTypes.string,

    style: PropTypes.object,

    className: PropTypes.string,

    helperClassName: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.object
    ]),

    orders: PropTypes.arrayOf(PropTypes.number),

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
FefferySortableContainer.defaultProps = {
    orders: [],
    helperClassName: 'sortable-helper'
}

export default FefferySortableContainer;