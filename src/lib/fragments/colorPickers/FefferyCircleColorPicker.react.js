import React, { useEffect } from 'react';
import CirclePicker from 'react-color/es/Circle';
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyCircleColorPicker.react';

// 定义Circle风格色彩选择器FefferyBlockColorPicker，文档参考：https://casesandberg.github.io/react-color/
const FefferyCircleColorPicker = (props) => {
    // 取得必要属性或参数
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