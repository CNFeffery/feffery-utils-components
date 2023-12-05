import React, { useEffect } from 'react';
import Wheel from '@uiw/react-color-wheel';
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyWheelColorPicker.react';

// 定义Wheel风格色彩选择器FefferyWheelColorPicker，文档参考：https://uiwjs.github.io/react-color/#/wheel
const FefferyWheelColorPicker = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        color,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        if (!color) {
            setProps({
                color: '#fffc51'
            })
        }
    }, [])

    return (
        <Wheel id={id}
            className={className}
            style={style}
            color={color}
            onChange={(c) => {
                setProps({ color: c.hex })
            }}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyWheelColorPicker;

FefferyWheelColorPicker.defaultProps = defaultProps;
FefferyWheelColorPicker.propTypes = propTypes;