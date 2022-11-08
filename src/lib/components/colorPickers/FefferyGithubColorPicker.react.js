import React, { useEffect } from 'react';
import { GithubPicker } from 'react-color';
import PropTypes from 'prop-types';
import '../styles.css';

// 定义Github风格色彩选择器FefferyGithubColorPicker，文档参考：https://casesandberg.github.io/react-color/
const FefferyGithubColorPicker = (props) => {
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
        <GithubPicker id={id}
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

// 定义参数或属性
FefferyGithubColorPicker.propTypes = {
    // 部件id
    id: PropTypes.string,

    // css类名
    className: PropTypes.string,

    // 自定义css字典
    style: PropTypes.object,

    // 设置组件整体宽度，默认为'200px'
    width: PropTypes.string,

    // 对应当前选中的16进制色彩字符串
    color: PropTypes.string,

    // 设置可选的16进制色彩值数组，默认为['#B80000', '#DB3E00', '#FCCB00', '#008B02', '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3', '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3', '#D4C4FB']
    colors: PropTypes.arrayOf(PropTypes.string),

    // 设置顶部箭头的方位，可选的有'hide'、'top-left'、'top-right'，默认为'top-left'
    triangle: PropTypes.oneOf(['hide', 'top-left', 'top-right']),

    loading_state: PropTypes.shape({
        /**
         * Determines if the component is loading or not
         */
        is_loading: PropTypes.bool,
        /**
         * Holds which property is loading
         */
        prop_name: PropTypes.string,
        /**
         * Holds the name of the component that is loading
         */
        component_name: PropTypes.string
    })
};

// 设置默认参数
FefferyGithubColorPicker.defaultProps = {
    triangle: 'top-left',
    width: '200px',
    colors: ['#B80000', '#DB3E00', '#FCCB00', '#008B02', '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3', '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3', '#D4C4FB']
}

export default React.memo(FefferyGithubColorPicker);