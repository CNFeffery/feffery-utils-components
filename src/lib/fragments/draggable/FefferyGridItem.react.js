import React from 'react';
import { propTypes, defaultProps } from '../../components/draggable/FefferyGridItem.react';

/**
 * 可拖拽网格项组件FefferyGridItem
 */
const FefferyGridItem = (props) => {
    const {
        id,
        children,
        style,
        className,
        key,
        setProps,
        loading_state
    } = props;

    return (
        <div
            id={id}
            key={key}
            style={style}
            className={className}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } >{children}</div>
    );
}

export default FefferyGridItem;

FefferyGridItem.defaultProps = defaultProps;
FefferyGridItem.propTypes = propTypes;