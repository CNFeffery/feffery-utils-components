import { toPairs, flatten } from 'ramda';

const parseChildrenToArray = children => {
    if (children && !Array.isArray(children)) {
        return [children];
    }
    return children;
};

const resolveChildProps = child => window.dash_component_api.getLayout(child.props.componentPath)?.props;

const useLoading = () => window.dash_component_api.useDashContext().useLoading() || undefined;

const loadingSelector = (componentPath) => state => {
    let stringPath = JSON.stringify(componentPath);
    stringPath = stringPath.substring(0, stringPath.length - 1);
    const loadingChildren = toPairs(state.loading).reduce(
        (acc, [path, load]) => {
            if (path.startsWith(stringPath) && load.length) {
                return [...acc, load];
            }
            return acc;
        },
        []
    )
    if (loadingChildren?.length) {
        return flatten(loadingChildren);
    }
    return [];
};

export { parseChildrenToArray, resolveChildProps, useLoading, loadingSelector };