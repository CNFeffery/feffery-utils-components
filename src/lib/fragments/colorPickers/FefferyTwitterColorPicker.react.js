import React, { useEffect } from 'react';
import TwitterPicker from 'react-color/es/Twitter';
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyTwitterColorPicker.react';

// 定义Twitter风格色彩选择器FefferyGithubColorPicker，文档参考：https://casesandberg.github.io/react-color/
const FefferyTwitterColorPicker = (props) => {
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