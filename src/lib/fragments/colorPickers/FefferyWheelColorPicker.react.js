// react核心
import React, { useEffect } from 'react';
// 组件核心
import Wheel from '@uiw/react-color-wheel';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyWheelColorPicker.react';

/**
 * Wheel风格色彩选择器FefferyWheelColorPicker
 */
const FefferyWheelColorPicker = (props) => {
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