import * as React from 'react';
export interface GluejarState {
    images: string[];
}
export interface GluejarProps {
    children?: (state: GluejarState) => React.ReactNode;
    container: HTMLElement;
    onPaste: (state: GluejarState) => void;
    onError: (error: string) => void;
    acceptedFiles: string[];
}
export declare class Gluejar extends React.Component<GluejarProps, GluejarState> {
    static displayName: string;
    static defaultProps: {
        onPaste: () => null;
        errorHandler: () => null;
        acceptedFiles: string[];
    };
    state: {
        images: never[];
    };
    getContainer: () => HTMLElement;
    isValidFormat: (fileType: string) => boolean;
    pasteHandler: (e: ClipboardEvent) => void;
    transformImages: (data: DataTransfer, cb: Function) => void;
    checkPasted: (e: ClipboardEvent, cb: Function) => void;
    pushImage: (source: string) => void;
    componentDidMount(): void;
    componentDidUpdate(): void;
    componentWillUnmount(): void;
    render(): {} | null | undefined;
}
