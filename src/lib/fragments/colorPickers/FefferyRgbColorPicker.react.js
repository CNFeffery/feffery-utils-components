import { RgbStringColorPicker, RgbaStringColorPicker } from 'react-colorful';
import { useEffect } from 'react';
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyRgbColorPicker.react';

// 定义rgb色彩选择器FefferyRgbColorPicker，文档参考：https://github.com/omgovich/react-colorful
const FefferyRgbColorPicker = (props) => {
    // 取得必要属性或参数
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