// 组件核心
import ReactJson from '../../utils/react-json-view/dist/main'
// 辅助库
import { isString } from 'lodash';
// 自定义hooks
import useCss from '../../hooks/useCss';
// 参数类型
import { propTypes, defaultProps } from '../../components/dataDisplay/FefferyJsonViewer.react';

/**
 * json数据展示组件FefferyJsonViewer
 */
const FefferyJsonViewer = (props) => {
    const {
        id,
        key,
        style,
        className,
        data,
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
        setProps,
        loading_state
    } = props;

    return (
        <ReactJson
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
            data-dash-is-loading={
                (loading_state && loading_state.is_loading) || undefined
            } />
    );
}

export default FefferyJsonViewer;

FefferyJsonViewer.defaultProps = defaultProps;
FefferyJsonViewer.propTypes = propTypes;