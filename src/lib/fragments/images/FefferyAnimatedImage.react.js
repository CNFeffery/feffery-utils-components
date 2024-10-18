import React from 'react';
import SlAnimatedImage from '@shoelace-style/shoelace/dist/react/animated-image';
import { propTypes, defaultProps } from '../../components/images/FefferyAnimatedImage.react';

/**
 * 动图组件FefferyAnimatedImage
 */
const FefferyAnimatedImage = (props) => {
    let {
        id,
        className,
        style,
        src,
        alt,
        play,
        setProps,
        loading_state
    } = props;

    return (
        <SlAnimatedImage id={id}
            className={className}
            style={style}
            src={src}
            alt={alt}
            play={play}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyAnimatedImage;

FefferyAnimatedImage.defaultProps = defaultProps;
FefferyAnimatedImage.propTypes = propTypes;