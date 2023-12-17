import React, { useRef, useEffect } from "react";
import Cropper from "react-cropper";
import "cropperjs/dist/cropper.css";
import { isString } from 'lodash';
import useCss from '../../hooks/useCss';
import { propTypes, defaultProps } from '../../components/images/FefferyImageCropper.react';

// 定义图片裁剪组件FefferyImageCropper，api参数参考https://github.com/fengyuanchen/cropperjs?tab=readme-ov-file#options
const FefferyImageCropper = (props) => {
    // 取得必要属性或参数
    const {
        id,
        className,
        style,
        key,
        croppedImageData,
        src,
        alt,
        crossOrigin,
        viewMode,
        dragMode,
        initialAspectRatio,
        aspectRatio,
        data,
        preview,
        responsive,
        restore,
        checkCrossOrigin,
        checkOrientation,
        modal,
        guides,
        center,
        highlight,
        background,
        autoCrop,
        autoCropArea,
        movable,
        rotatable,
        scalable,
        zoomable,
        zoomOnTouch,
        zoomOnWheel,
        wheelZoomRatio,
        cropBoxMovable,
        cropBoxResizable,
        toggleDragModeOnDblclick,
        minContainerWidth,
        minContainerHeight,
        minCanvasWidth,
        minCanvasHeight,
        minCropBoxWidth,
        minCropBoxHeight,
        reset,
        clear,
        replace,
        enable,
        disable,
        destroy,
        move,
        moveTo,
        zoom,
        zoomTo,
        rotate,
        rotateTo,
        scale,
        scaleX,
        scaleY,
        outputData,
        containerData,
        imageData,
        canvasData,
        cropBoxData,
        setProps,
        loading_state
    } = props;

    const cropperRef = useRef(null);

    const onCrop = () => {
        const cropper = cropperRef.current?.cropper;
        setProps({ croppedImageData: cropper.getCroppedCanvas().toDataURL() });
        setProps({ outputData: cropper.getData() });
        setProps({ containerData: cropper.getContainerData() });
        setProps({ imageData: cropper.getImageData() });
        setProps({ canvasData: cropper.getCanvasData() });
        setProps({ cropBoxData: cropper.getCropBoxData() });
    };

    useEffect(() => {
        if (reset) {
            cropperRef.current?.cropper.reset();
            setProps({ reset: false });
        }
    }, [reset])

    useEffect(() => {
        if (clear) {
            cropperRef.current?.cropper.clear();
            setProps({ clear: false });
        }
    }, [clear])

    useEffect(() => {
        if (replace.isReplace && replace.url) {
            cropperRef.current?.cropper.replace(replace.url, replace.hasSameSize);
            setProps({ replace: { isReplace: false, url: undefined, hasSameSize: false } });
        }
    }, [replace])

    useEffect(() => {
        if (enable) {
            cropperRef.current?.cropper.enable();
            setProps({ enable: false });
        }
    }, [enable])

    useEffect(() => {
        if (disable) {
            cropperRef.current?.cropper.disable();
            setProps({ disable: false });
        }
    }, [disable])

    useEffect(() => {
        if (destroy) {
            cropperRef.current?.cropper.destroy();
            setProps({ destroy: false });
        }
    }, [destroy])

    useEffect(() => {
        if (move.isMove && move.offsetX) {
            cropperRef.current?.cropper.move(move.offsetX, move.offsetY);
            setProps({ move: { isMove: false, offsetX: undefined, offsetY: undefined } });
        }
    }, [move])

    useEffect(() => {
        if (moveTo.isMoveTo && moveTo.x) {
            cropperRef.current?.cropper.moveTo(moveTo.x, moveTo.y);
            setProps({ moveTo: { isMoveTo: false, x: undefined, y: undefined } });
        }
    }, [moveTo])

    useEffect(() => {
        if (zoom.isZoom && zoom.ratio) {
            cropperRef.current?.cropper.zoom(zoom.ratio);
            setProps({ zoom: { isZoom: false, ratio: undefined } });
        }
    }, [zoom])

    useEffect(() => {
        if (zoomTo.isZoomTo && zoomTo.ratio) {
            cropperRef.current?.cropper.zoomTo(zoomTo.ratio, zoomTo.pivot);
            setProps({ zoomTo: { isZoomTo: false, ratio: undefined, pivot: undefined } });
        }
    }, [zoomTo])

    useEffect(() => {
        if (rotate.isRotate && rotate.degree) {
            cropperRef.current?.cropper.rotate(rotate.degree);
            setProps({ rotate: { isRotate: false, degree: undefined } });
        }
    }, [rotate])

    useEffect(() => {
        if (rotateTo.isRotateTo && rotateTo.degree) {
            cropperRef.current?.cropper.rotateTo(rotateTo.degree);
            setProps({ rotateTo: { isRotateTo: false, degree: undefined } });
        }
    }, [rotateTo])

    useEffect(() => {
        if (scale.isScale && scale.scaleX) {
            cropperRef.current?.cropper.scale(scale.scaleX, scale.scaleY);
            setProps({ scale: { isScale: false, scaleX: undefined, scaleY: undefined } });
        }
    }, [scale])

    useEffect(() => {
        if (scaleX.isScaleX && scaleX.scaleX) {
            cropperRef.current?.cropper.scaleX(scaleX.scaleX);
            setProps({ scaleX: { isScaleX: false, scaleX: undefined } });
        }
    }, [scaleX])

    useEffect(() => {
        if (scaleY.isScaleY && scaleY.scaleY) {
            cropperRef.current?.cropper.scaleY(scaleY.scaleY);
            setProps({ scaleY: { isScaleY: false, scaleY: undefined } });
        }
    }, [scaleY])

    return (
        <Cropper
            ref={cropperRef}
            id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            key={key}
            src={src}
            alt={alt}
            crossOrigin={crossOrigin}
            viewMode={viewMode}
            dragMode={dragMode}
            initialAspectRatio={initialAspectRatio}
            aspectRatio={aspectRatio}
            data={data}
            preview={preview}
            responsive={responsive}
            restore={restore}
            checkCrossOrigin={checkCrossOrigin}
            checkOrientation={checkOrientation}
            modal={modal}
            guides={guides}
            center={center}
            highlight={highlight}
            background={background}
            autoCrop={autoCrop}
            autoCropArea={autoCropArea}
            movable={movable}
            rotatable={rotatable}
            scalable={scalable}
            zoomable={zoomable}
            zoomOnTouch={zoomOnTouch}
            zoomOnWheel={zoomOnWheel}
            wheelZoomRatio={wheelZoomRatio}
            cropBoxMovable={cropBoxMovable}
            cropBoxResizable={cropBoxResizable}
            toggleDragModeOnDblclick={toggleDragModeOnDblclick}
            minContainerWidth={minContainerWidth}
            minContainerHeight={minContainerHeight}
            minCanvasWidth={minCanvasWidth}
            minCanvasHeight={minCanvasHeight}
            minCropBoxWidth={minCropBoxWidth}
            minCropBoxHeight={minCropBoxHeight}
            crop={onCrop}
            loading_state={loading_state}
        />
    );
}

export default FefferyImageCropper;

FefferyImageCropper.defaultProps = defaultProps;
FefferyImageCropper.propTypes = propTypes;