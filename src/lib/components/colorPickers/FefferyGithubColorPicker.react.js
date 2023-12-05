import React, { Suspense } from 'react';
import PropTypes from 'prop-types';

const LazyFefferyGithubColorPicker = React.lazy(() => import(/* webpackChunkName: "feffery_color_pickers" */ '../../fragments/colorPickers/FefferyGithubColorPicker.react'));

const FefferyGithubColorPicker = (props) => {
    return (
        <Suspense fallback={null}>
            <LazyFefferyGithubColorPicker {...props} />
        </Suspense>
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
    colors: ['#B80000', '#DB3E00', '#FCCB00', '#008B02', '#006B76', '#1273DE', '#004DCF', '#5300EB', '#EB9694', '#FAD0C3', '#FEF3BD', '#C1E1C5', '#BEDADC', '#C4DEF6', '#BED3F3', '#D4C4FB']
}

export default FefferyGithubColorPicker;

export const propTypes = FefferyGithubColorPicker.propTypes;
export const defaultProps = FefferyGithubColorPicker.defaultProps;