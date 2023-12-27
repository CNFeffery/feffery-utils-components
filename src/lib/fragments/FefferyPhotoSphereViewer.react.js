import { ReactPhotoSphereViewer } from 'react-photo-sphere-viewer';
import { propTypes, defaultProps } from '../components/FefferyPhotoSphereViewer.react';

// 定义全景图片查看器组件FefferyPhotoSphereViewer
const FefferyPhotoSphereViewer = (props) => {
    const {
        id,
        key,
        src,
        width,
        height,
        littlePlanet,
        containerClass,
        navbar,
        caption,
        loadingImg,
        loadingTxt,
        mousewheel,
        mousemove,
        moveSpeed,
        zoomSpeed,
        setProps,
        loading_state
    } = props;

    return (
        <ReactPhotoSphereViewer
            id={id}
            key={key}
            src={src}
            width={width}
            height={height}
            littlePlanet={littlePlanet}
            containerClass={containerClass}
            navbar={navbar}
            caption={caption}
            loadingImg={loadingImg}
            loadingTxt={loadingTxt}
            mousewheel={mousewheel}
            mousemove={mousemove}
            moveSpeed={moveSpeed}
            zoomSpeed={zoomSpeed}
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyPhotoSphereViewer;

FefferyPhotoSphereViewer.defaultProps = defaultProps;
FefferyPhotoSphereViewer.propTypes = propTypes;