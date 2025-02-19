// react核心
import React, { useEffect } from 'react';
// 组件核心
import BlockPicker from 'react-color/es/Block';
// 辅助库
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyBlockColorPicker.react';

/**
 * Block风格色彩选择器
 */
const FefferyBlockColorPicker = ({
    id,
    className,
    style,
    width,
    color,
    colors,
    triangle,
    setProps
}) => {

    useEffect(() => {
        if (colors && !color) {
            // 默认缺省选中色为colors中第0个色彩
            setProps({
                color: colors[0]
            })
        }
    }, [])

    return (
        <BlockPicker id={id}
            className={className}
            style={style}
            color={color}
            colors={colors}
            width={width}
            triangle={triangle}
            onChangeComplete={(c, e) => setProps({ color: c.hex })}
            data-dash-is-loading={useLoading()} />
    );
}

export default FefferyBlockColorPicker;

FefferyBlockColorPicker.defaultProps = defaultProps;
FefferyBlockColorPicker.propTypes = propTypes;