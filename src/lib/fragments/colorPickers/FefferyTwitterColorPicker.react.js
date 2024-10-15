// react核心
import React, { useEffect } from 'react';
// 组件核心
import TwitterPicker from 'react-color/es/Twitter';
// 参数类型
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyTwitterColorPicker.react';

/**
 * Twitter风格色彩选择器FefferyGithubColorPicker
 */
const FefferyTwitterColorPicker = (props) => {
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
        <TwitterPicker id={id}
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

export default FefferyTwitterColorPicker;

FefferyTwitterColorPicker.defaultProps = defaultProps;
FefferyTwitterColorPicker.propTypes = propTypes;