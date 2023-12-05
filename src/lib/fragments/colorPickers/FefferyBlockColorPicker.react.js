import React, { useEffect } from 'react';
import BlockPicker from 'react-color/es/Block';
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyBlockColorPicker.react';

// 定义Block风格色彩选择器FefferyBlockColorPicker，文档参考：https://casesandberg.github.io/react-color/
const FefferyBlockColorPicker = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        width,
        color,
        colors,
        triangle,
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
        <BlockPicker id={id}
            className={className}
            style={style}
            color={color}
            colors={colors}
            width={width}
            triangle={triangle}
            onChangeComplete={(c, e) => setProps({ color: c.hex })}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyBlockColorPicker;

FefferyBlockColorPicker.defaultProps = defaultProps;
FefferyBlockColorPicker.propTypes = propTypes;