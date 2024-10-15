// react核心
import { useEffect } from 'react';
// 组件核心
import { HexColorPicker, HexAlphaColorPicker } from 'react-colorful';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyHexColorPicker.react';

/**
 * 16进制色彩选择器FefferyHexColorPicker
 */
const FefferyHexColorPicker = (props) => {
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
            <HexAlphaColorPicker id={id}
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
        <HexColorPicker id={id}
            className={className}
            style={style}
            color={color}
            onChange={(c) => setProps({ color: c })}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyHexColorPicker;

FefferyHexColorPicker.defaultProps = defaultProps;
FefferyHexColorPicker.propTypes = propTypes;