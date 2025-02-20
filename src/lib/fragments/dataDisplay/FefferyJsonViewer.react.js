// 组件核心
import ReactJsonView from '@microlink/react-json-view'
// 辅助库
import { isString } from 'lodash';
import { useLoading } from '../../components/utils';
// 自定义hooks
import useCss from '../../hooks/useCss';
// 参数类型
import { propTypes, defaultProps } from '../../components/dataDisplay/FefferyJsonViewer.react';

/**
 * json数据展示组件FefferyJsonViewer
 */
const FefferyJsonViewer = ({
    id,
    key,
    style,
    className,
    data,
    rootName,
    theme,
    indent,
    iconStyle,
    collapsed,
    collapseStringsAfterLength,
    groupArraysAfterLength,
    enableClipboard,
    displayObjectSize,
    displayDataTypes,
    editable,
    addible,
    deletable,
    sortKeys,
    quotesOnKeys,
    displayArrayKey,
    setProps
}) => {

    return (
        <ReactJsonView
            id={id}
            key={key}
            style={style}
            className={
                isString(className) ?
                    className :
                    (className ? useCss(className) : undefined)
            }
            theme={theme}
            src={data}
            name={rootName}
            indentWidth={indent}
            iconStyle={iconStyle}
            collapsed={collapsed}
            collapseStringsAfterLength={collapseStringsAfterLength}
            groupArraysAfterLength={groupArraysAfterLength}
            enableClipboard={enableClipboard}
            displayObjectSize={displayObjectSize}
            displayDataTypes={displayDataTypes}
            onEdit={
                editable ? (e) => setProps({ data: e.updated_src }) : false
            }
            onAdd={
                addible ? (e) => setProps({ data: e.updated_src }) : false
            }
            onDelete={
                deletable ? (e) => setProps({ data: e.updated_src }) : false
            }
            sortKeys={sortKeys}
            quotesOnKeys={quotesOnKeys}
            displayArrayKey={displayArrayKey}
            data-dash-is-loading={useLoading()} />
    );
}

export default FefferyJsonViewer;

FefferyJsonViewer.defaultProps = defaultProps;
FefferyJsonViewer.propTypes = propTypes;