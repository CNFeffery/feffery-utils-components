import { HexColorPicker, HexAlphaColorPicker } from 'react-colorful';
import { useEffect } from 'react';
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyHexColorPicker.react';

// 定义16进制色彩选择器FefferyHexColorPicker，文档参考：https://github.com/omgovich/react-colorful
const FefferyHexColorPicker = (props) => {
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