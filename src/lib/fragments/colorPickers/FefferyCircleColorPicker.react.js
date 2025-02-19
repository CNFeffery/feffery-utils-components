// react核心
import React, { useEffect } from 'react';
// 组件核心
import CirclePicker from 'react-color/es/Circle';
// 辅助库
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyCircleColorPicker.react';

/**
 * Circle风格色彩选择器
 */
const FefferyCircleColorPicker = ({
    id,
    className,
    style,
    width,
    circleSize,
    circleSpacing,
    color,
    colors,
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
        <CirclePicker id={id}
            className={className}
            style={style}
            width={width}
            circleSize={circleSize}
            circleSpacing={circleSpacing}
            color={color}
            colors={colors}
            onChangeComplete={(c, e) => setProps({ color: c.hex })}
            data-dash-is-loading={useLoading()} />
    );
}

export default FefferyCircleColorPicker;

FefferyCircleColorPicker.defaultProps = defaultProps;
FefferyCircleColorPicker.propTypes = propTypes;