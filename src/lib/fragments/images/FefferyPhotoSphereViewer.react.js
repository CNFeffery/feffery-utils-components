import { ReactPhotoSphereViewer } from 'react-photo-sphere-viewer';
// 额外插件
import { AutorotatePlugin } from '@photo-sphere-viewer/autorotate-plugin';
import { omit } from 'ramda';
import { propTypes, defaultProps } from '../../components/images/FefferyPhotoSphereViewer.react';

// 插件名 -> 插件
const type2plugins = {
    Autorotate: AutorotatePlugin
}

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
        downloadUrl,
        loadingImg,
        loadingTxt,
        mousewheel,
        mousemove,
        moveSpeed,
        zoomSpeed,
        fisheye,
        lang,
        hideNavbarButton,
        plugins,
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
            downloadUrl={downloadUrl}
            loadingImg={loadingImg}
            loadingTxt={loadingTxt}
            mousewheel={mousewheel}
            mousemove={mousemove}
            moveSpeed={moveSpeed}
            zoomSpeed={zoomSpeed}
            fisheye={fisheye}
            lang={lang}
            hideNavbarButton={hideNavbarButton}
            plugins={
                plugins && plugins.map(
                    (plugin) => ([
                        type2plugins[plugin.type],
                        omit(['type'], plugin)
                    ])
                )
            }
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyPhotoSphereViewer;

FefferyPhotoSphereViewer.defaultProps = defaultProps;
FefferyPhotoSphereViewer.propTypes = propTypes;