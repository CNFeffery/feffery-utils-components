// react核心
import { useRef, useEffect } from 'react';
// 组件核心
import jsPreviewExcel from '@js-preview/excel';
// 样式
import '@js-preview/excel/lib/index.css';
// 辅助库
import useCss from '../../hooks/useCss';
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 参数类型
import { propTypes, defaultProps } from '../../components/filePreview/FefferyExcelPreview.react';

/**
 * excel文件预览组件FefferyExcelPreview
 */
const FefferyExcelPreview = ({
    id,
    style,
    className,
    src,
    minColLength,
    minRowLength,
    widthOffset,
    heightOffset,
    setProps
}) => {

    const containerRef = useRef(null);

    useEffect(
        () => {
            if (!containerRef.current) return;

            // 挂载到指定目标容器
            const excelPreviewer = jsPreviewExcel.init(
                containerRef.current,
                {
                    minColLength,
                    minRowLength,
                    widthOffset,
                    heightOffset
                }
            );

            // 传递要预览的文件地址即可
            excelPreviewer.preview(src).then(res => {
                // console.log('预览完成');
            }).catch(e => {
                // console.log('预览失败', e);
            });

            // 清除资源（在组件卸载时）
            return () => {
                excelPreviewer.destroy();
            };
        }, [src]
    )

    return (
        <div
            id={id}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            style={style}
            ref={containerRef}
            data-dash-is-loading={useLoading()} />
    );
}

export default FefferyExcelPreview;

FefferyExcelPreview.defaultProps = defaultProps;
FefferyExcelPreview.propTypes = propTypes;