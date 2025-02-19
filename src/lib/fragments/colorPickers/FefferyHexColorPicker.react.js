// react核心
import { useEffect } from 'react';
// 组件核心
import { HexColorPicker, HexAlphaColorPicker } from 'react-colorful';
// 辅助库
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyHexColorPicker.react';

/**
 * 16进制色彩选择器FefferyHexColorPicker
 */
const FefferyHexColorPicker = ({
    id,
    className,
    style,
    color,
    showAlpha,
    setProps
}) => {

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
                data-dash-is-loading={useLoading()} />
        );
    }

    return (
        <HexColorPicker id={id}
            className={className}
            style={style}
            color={color}
            onChange={(c) => setProps({ color: c })}
            data-dash-is-loading={useLoading()} />
    );
}

export default FefferyHexColorPicker;

FefferyHexColorPicker.defaultProps = defaultProps;
FefferyHexColorPicker.propTypes = propTypes;