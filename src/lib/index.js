/* eslint-disable import/prefer-default-export */
import FefferyCaptcha from "./components/FefferyCaptcha.react";
import FefferyTopProgress from "./components/FefferyTopProgress.react"
import FefferyShortcutPanel from "./components/FefferyShortcutPanel.react"
import FefferyGuide from "./components/FefferyGuide.react"
import FefferySplit from "./components/split/FefferySplit.react";
import FefferySplitPane from "./components/split/FefferySplitPane.react"
import FefferyExecuteJs from "./components/FefferyExecuteJs.react";
import FefferyScroll from "./components/FefferyScroll.react";
import FefferyScrollbars from "./components/FefferyScrollbars.react";
import FefferyExtraSpinner from "./components/FefferyExtraSpinner.react";
import FefferyLazyLoad from "./components/FefferyLazyLoad.react";
import FefferyVirtualList from "./components/FefferyVirtualList.react";
import FefferyInViewport from "./components/listeners/FefferyInViewport.react";
import FefferyHexColorPicker from "./components/colorPickers/FefferyHexColorPicker.react";
import FefferyRgbColorPicker from "./components/colorPickers/FefferyRgbColorPicker.react";
import FefferyGithubColorPicker from "./components/colorPickers/FefferyGithubColorPicker.react";
import FefferyTwitterColorPicker from "./components/colorPickers/FefferyTwitterColorPicker.react";
import FefferyBlockColorPicker from "./components/colorPickers/FefferyBlockColorPicker.react";
import FefferyCircleColorPicker from "./components/colorPickers/FefferyCircleColorPicker.react";
import FefferyWheelColorPicker from "./components/colorPickers/FefferyWheelColorPicker.react";
import FefferyHighlightWords from "./components/FefferyHighlightWords.react";
import FefferyDocumentVisibility from "./components/listeners/FefferyDocumentVisibility.react";
import FefferyExternalCss from "./components/FefferyExternalCss.react";
import FefferyExternalJs from "./components/FefferyExternalJs.react";
import FefferySetTitle from "./components/FefferySetTitle.react";
import FefferyResponsive from "./components/listeners/FefferyResponsive.react";
import FefferyGeolocation from "./components/listeners/FefferyGeolocation.react";
import FefferyIdle from "./components/listeners/FefferyIdle.react";
import FefferyWindowSize from "./components/listeners/FefferyWindowSize.react";
import FefferyKeyPress from "./components/listeners/FefferyKeyPress.react";
import FefferyTimeout from "./components/FefferyTimeout.react";
import FefferyCountDown from "./components/FefferyCountDown.react";
import FefferySortableItem from "./components/sortable/FefferySortableItem.react";
import FefferySortableContainer from "./components/sortable/FefferySortableContainer.react";
import FefferyRawHTML from "./components/FefferyRawHTML.react";
import FefferyFancyNotification from "./components/FefferyFancyNotification";
import FefferyQRCode from "./components/FefferyQrcode.react";
import FefferyFancyMessage from "./components/FefferyFancyMessage";
import FefferyStyle from "./components/FefferyStyle.react";
import FefferyDiv from "./components/FefferyDiv.react";
import FefferyReload from "./components/FefferyReload.react";
import FefferyCssVar from "./components/FefferyCssVar.react";
import FefferyEyeDropper from "./components/colorPickers/FefferyEyeDropper.react";
import FefferySticky from "./components/FefferySticky.react";
import FefferySessionStorage from "./components/store/FefferySessionStorage";
import FefferyWebSocket from "./components/FefferyWebSocket.react";
import FefferyShadowDom from "./components/FefferyShadowDom.react";
import FefferyGrid from "./components/draggable/FefferyGrid.react";
import FefferyGridItem from "./components/draggable/FefferyGridItem.react";
import FefferyFancyButton from "./components/FefferyFancyButton.react";
import FefferyJsonViewer from "./components/FefferyJsonViewer.react";
import FefferyImagePaste from "./components/FefferyImagePaste.react";
import FefferyFullscreen from "./components/FefferyFullscreen.react";
import FefferyDeviceDetect from "./components/listeners/FefferyDeviceDetect.react";
import FefferyMotion from "./components/animations/FefferyMotion.react";
import FefferyAutoAnimate from "./components/animations/FefferyAutoAnimate.react";
import FefferyCountUp from "./components/FefferyCountUp.react";
import FefferyListenUnload from "./components/listeners/FefferyListenUnload.react";
import FefferyListenScroll from "./components/listeners/FefferyListenScroll.react";
import FefferyMousePosition from "./components/listeners/FefferyMousePosition.react";
import FefferyListenPaste from "./components/listeners/FefferyListenPaste.react";
import FefferyLocation from "./components/listeners/FefferyLocation.react";
import FefferyCookie from "./components/store/FefferyCookie.react";
import FefferyResizable from "./components/resizable/FefferyResizable.react";

/* 
忽略部分设计React中规范的console警告信息
目前已知无关警告信息：
1. 数组推导形成的组件，每个子组件需要唯一的key
2. 在原生html元素中携带小驼峰命名法的props
*/
// try {
//     consoleErrorBackup
// } catch (e) {
//     const consoleErrorBackup = console.error;
//     console.error = (msg) => {
//         const supressedWarnings = [
//             'Each child in a list should have a unique',
//             'React does not recognize the'
//         ];

//         if (!supressedWarnings.some(entry => msg.includes && msg.includes(entry))) {
//             consoleErrorBackup(msg);
//         }
//     };
// }

// 自定义sessionStorage事件监听
const originalSetItem = sessionStorage.setItem;
sessionStorage.setItem = function (key, newValue) {
    originalSetItem.apply(this, [key, newValue]);
    const setItemEvent = new Event("sessionStorageSetItem");
    setItemEvent['triggerKey'] = key
    setItemEvent[key] = newValue;
    window.dispatchEvent(setItemEvent);
};

export {
    FefferyCaptcha,
    FefferyTopProgress,
    FefferyShortcutPanel,
    FefferyGuide,
    FefferySplit,
    FefferySplitPane,
    FefferyExecuteJs,
    FefferyScroll,
    FefferyScrollbars,
    FefferyExtraSpinner,
    FefferyLazyLoad,
    FefferyVirtualList,
    FefferyInViewport,
    FefferyHexColorPicker,
    FefferyRgbColorPicker,
    FefferyGithubColorPicker,
    FefferyTwitterColorPicker,
    FefferyBlockColorPicker,
    FefferyCircleColorPicker,
    FefferyWheelColorPicker,
    FefferyHighlightWords,
    FefferyDocumentVisibility,
    FefferyExternalCss,
    FefferyExternalJs,
    FefferySetTitle,
    FefferyResponsive,
    FefferyGeolocation,
    FefferyIdle,
    FefferyWindowSize,
    FefferyKeyPress,
    FefferyTimeout,
    FefferyCountDown,
    FefferySortableItem,
    FefferySortableContainer,
    FefferyRawHTML,
    FefferyFancyNotification,
    FefferyQRCode,
    FefferyFancyMessage,
    FefferyStyle,
    FefferyDiv,
    FefferyReload,
    FefferyCssVar,
    FefferyEyeDropper,
    FefferySticky,
    FefferySessionStorage,
    FefferyWebSocket,
    FefferyShadowDom,
    FefferyGrid,
    FefferyGridItem,
    FefferyFancyButton,
    FefferyJsonViewer,
    FefferyImagePaste,
    FefferyFullscreen,
    FefferyDeviceDetect,
    FefferyMotion,
    FefferyAutoAnimate,
    FefferyCountUp,
    FefferyListenUnload,
    FefferyListenScroll,
    FefferyMousePosition,
    FefferyListenPaste,
    FefferyLocation,
    FefferyCookie,
    FefferyResizable
};