"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __spreadArrays = (this && this.__spreadArrays) || function () {
    for (var s = 0, i = 0, il = arguments.length; i < il; i++) s += arguments[i].length;
    for (var r = Array(s), k = 0, i = 0; i < il; i++)
        for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++)
            r[k] = a[j];
    return r;
};
Object.defineProperty(exports, "__esModule", { value: true });
var React = require("react");
var Gluejar = /** @class */ (function (_super) {
    __extends(Gluejar, _super);
    function Gluejar() {
        var _this = _super !== null && _super.apply(this, arguments) || this;
        _this.state = {
            images: []
        };
        _this.getContainer = function () { return _this.props.container || window; };
        _this.isValidFormat = function (fileType) { return _this.props.acceptedFiles.includes(fileType); };
        _this.pasteHandler = function (e) { return _this.checkPasted(e, _this.pushImage); };
        _this.transformImages = function (data, cb) {
            // NOTE: This needs to be a for loop, it's a list like object
            for (var i = 0; i < data.items.length; i++) {
                if (_this.isValidFormat(data.items[i].type) !== false) {
                    var blob = data.items[i].getAsFile();
                    var URL_1 = window.URL;
                    if (blob) {
                        // We shouldn't fire the callback if we can't create `new Blob()`
                        var src = URL_1.createObjectURL(blob);
                        cb(src);
                    }
                }
                else {
                    _this.props.onError("Sorry, that's not a format we support");
                }
            }
        };
        _this.checkPasted = function (e, cb) {
            e.clipboardData && e.clipboardData.items.length > 0
                ? _this.transformImages(e.clipboardData, cb)
                : _this.props.onError("Sorry, to bother you but there was no image pasted.");
        };
        _this.pushImage = function (source) {
            return _this.setState(function (_a) {
                // var images = _a.images;
                // return ({ images: __spreadArrays(images, [source]) });
                return ({ images: [source] });
            });
        };
        return _this;
    }
    Gluejar.prototype.componentDidMount = function () {
        var elm = this.getContainer();
        elm.addEventListener('paste', this.pasteHandler);
    };
    Gluejar.prototype.componentDidUpdate = function (prevProps, prevState) {
        if (prevState.images !== this.state.images) {
            this.props.onPaste(this.state);
        }
    };
    Gluejar.prototype.componentWillUnmount = function () {
        var elm = this.getContainer();
        elm.removeEventListener('paste', this.pasteHandler);
    };
    Gluejar.prototype.render = function () {
        var images = this.state.images;
        var children = this.props.children;
        return children ? children({ images: images }) : null;
    };
    Gluejar.displayName = 'Gluejar';
    Gluejar.defaultProps = {
        onPaste: function () { return null; },
        errorHandler: function () { return null; },
        acceptedFiles: ['image/gif', 'image/png', 'image/jpeg', 'image/bmp']
    };
    return Gluejar;
}(React.Component));
exports.Gluejar = Gluejar;
//# sourceMappingURL=index.js.map