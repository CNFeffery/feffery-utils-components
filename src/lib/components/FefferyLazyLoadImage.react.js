import React from 'react';
import { LazyLoadImage } from 'react-lazy-load-image-component';
import PropTypes from 'prop-types';
import 'react-lazy-load-image-component/src/effects/opacity.css';

// 定义图片懒加载组件FefferyLazyLoadImage
const FefferyLazyLoadImage = (props) => {
    // 取得必要属性或参数
    const {
        id,
        alt,
        height,
        width,
        src,
        placeholderSrc,
        threshold,
        setProps,
        loading_state
    } = props;

    return <LazyLoadImage
        id={id}
        alt={alt}
        height={height}
        width={width}
        src={src}
        placeholderSrc={placeholderSrc}
        threshold={threshold}
        effect={'opacity'}
        data-dash-is-loading={
            (loading_state && loading_state.is_loading) || undefined
        } />;
}

// 定义参数或属性
FefferyLazyLoadImage.propTypes = {
    // 部件id
    id: PropTypes.string,

    // 设置图片alt信息
    alt: PropTypes.string,

    // 设置图片高度
    height: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.number
    ]),

    // 设置图片宽度
    width: PropTypes.oneOfType([
        PropTypes.string,
        PropTypes.number
    ]),

    // 设置图片url地址
    src: PropTypes.string,

    // 图片未显示或加载失败时的占位图地址
    placeholderSrc: PropTypes.string,

    // 设置触发加载像素距离阈值，当图片未划入视口但距离视口低于此阈值时
    // 开始触发加载延时倒计时，默认为100
    threshold: PropTypes.number,

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
    }),

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func,
};

// 设置默认参数
FefferyLazyLoadImage.defaultProps = {
    threshold: 100
}

export default FefferyLazyLoadImage;