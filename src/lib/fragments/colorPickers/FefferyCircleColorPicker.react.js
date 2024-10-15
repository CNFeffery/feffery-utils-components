// react核心
import React, { useEffect } from 'react';
// 组件核心
import CirclePicker from 'react-color/es/Circle';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyCircleColorPicker.react';

/**
 * Circle风格色彩选择器
 */
const FefferyCircleColorPicker = (props) => {
    const {
        id,
        className,
        style,
        width,
        circleSize,
        circleSpacing,
        color,
        colors,
        setProps,
        loading_state
    } = props;

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
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyCircleColorPicker;

FefferyCircleColorPicker.defaultProps = defaultProps;
FefferyCircleColorPicker.propTypes = propTypes;