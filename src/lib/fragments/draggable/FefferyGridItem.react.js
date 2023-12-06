import React from 'react';
import { propTypes, defaultProps } from '../../components/draggable/FefferyGridItem.react';

// 定义可拖拽网格项组件FefferyGridItem
const FefferyGridItem = (props) => {
    // 取得必要属性或参数
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