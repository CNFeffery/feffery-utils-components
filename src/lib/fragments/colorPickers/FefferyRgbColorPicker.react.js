// react核心
import { useEffect } from 'react';
// 组件核心
import { RgbStringColorPicker, RgbaStringColorPicker } from 'react-colorful';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyRgbColorPicker.react';

/**
 * rgb色彩选择器FefferyRgbColorPicker
 */
const FefferyRgbColorPicker = (props) => {
    const {
        id,
        className,
        style,
        color,
        showAlpha,
        setProps,
        loading_state
    } = props;

    useEffect(() => {
        setProps({ color: color })
    }, [])

    if (showAlpha) {
        return (
            <RgbaStringColorPicker id={id}
                className={className}
                style={style}
                color={color}
                onChange={(c) => setProps({ color: c })}
                data-dash-is-loading={
                    (loading_state && loading_state.is_loading) || undefined
                } />
        );
    }

    return (
        <RgbStringColorPicker id={id}
            className={className}
            style={style}
            color={color}
            onChange={(c) => setProps({ color: c })}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyRgbColorPicker;

FefferyRgbColorPicker.defaultProps = defaultProps;
FefferyRgbColorPicker.propTypes = propTypes;