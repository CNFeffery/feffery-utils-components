import React, { useEffect } from 'react';
import GithubPicker from 'react-color/es/Github';
import { propTypes, defaultProps } from '../../components/colorPickers/FefferyGithubColorPicker.react';

// 定义Github风格色彩选择器FefferyGithubColorPicker，文档参考：https://casesandberg.github.io/react-color/
const FefferyGithubColorPicker = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
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
        <GithubPicker id={id}
            className={className}
            style={style}
            color={color}
            colors={colors}
            triangle={triangle}
            onChangeComplete={(c, e) => setProps({ color: c.hex })}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyGithubColorPicker;

FefferyGithubColorPicker.defaultProps = defaultProps;
FefferyGithubColorPicker.propTypes = propTypes;