// react核心
import React from 'react';
// 辅助库
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/draggable/FefferyGridItem.react';

/**
 * 可拖拽网格项组件FefferyGridItem
 */
const FefferyGridItem = ({
    id,
    children,
    style,
    className,
    key,
    setProps
}) => {

    return (
        <div
            id={id}
            key={key}
            style={style}
            className={className}
            data-dash-is-loading={useLoading()} >{children}</div>
    );
}

export default FefferyGridItem;

FefferyGridItem.defaultProps = defaultProps;
FefferyGridItem.propTypes = propTypes;