// react核心
import { useEffect } from 'react';
// 组件核心
import { RgbStringColorPicker, RgbaStringColorPicker } from 'react-colorful';
// 辅助库
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyRgbColorPicker.react';

/**
 * rgb色彩选择器FefferyRgbColorPicker
 */
const FefferyRgbColorPicker = ({
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
            <RgbaStringColorPicker id={id}
                className={className}
                style={style}
                color={color}
                onChange={(c) => setProps({ color: c })}
                data-dash-is-loading={useLoading()} />
        );
    }

    return (
        <RgbStringColorPicker id={id}
            className={className}
            style={style}
            color={color}
            onChange={(c) => setProps({ color: c })}
            data-dash-is-loading={useLoading()} />
    );
}

export default FefferyRgbColorPicker;

FefferyRgbColorPicker.defaultProps = defaultProps;
FefferyRgbColorPicker.propTypes = propTypes;