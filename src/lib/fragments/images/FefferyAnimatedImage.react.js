// react核心
import React from 'react';
// 组件核心
import SlAnimatedImage from '@shoelace-style/shoelace/dist/react/animated-image';
// 辅助库
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/images/FefferyAnimatedImage.react';

/**
 * 动图组件FefferyAnimatedImage
 */
const FefferyAnimatedImage = ({
    id,
    className,
    style,
    src,
    alt,
    play,
    setProps
}) => {

    return (
        <SlAnimatedImage id={id}
            className={className}
            style={style}
            src={src}
            alt={alt}
            play={play}
            data-dash-is-loading={useLoading()} />
    );
}

export default FefferyAnimatedImage;

FefferyAnimatedImage.defaultProps = defaultProps;
FefferyAnimatedImage.propTypes = propTypes;