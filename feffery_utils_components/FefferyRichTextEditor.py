# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FefferyRichTextEditor(Component):
    """A FefferyRichTextEditor component.
富文本编辑器组件FefferyRichTextEditor

Keyword arguments:

- id (string; optional):
    组件唯一id.

- key (string; optional):
    对当前组件的`key`值进行更新，可实现强制重绘当前组件的效果.

- style (dict; optional):
    当前组件css样式.

- className (string | dict; optional):
    当前组件css类名，支持[动态css](/advanced-classname).

- toolbarClassName (string; optional):
    工具栏类名.

- toolbarStyle (dict; optional):
    设置工具栏的样式.

- editorClassName (string; optional):
    编辑器类名.

- editorStyle (dict; optional):
    设置编辑器的样式.

- locale (a value equal to: 'zh-CN', 'en'; default 'zh-CN'):
    组件语言，可选的有`'zh-CN'`、`'en'`  默认值：`'zh-CN'`.

- mode (a value equal to: 'default', 'simple'; default 'default'):
    编辑器模式，可选的有`'default'`、`'simple'`，`'default'`模式 - 集成了 wangEditor
    所有功能，`'simple'`模式 - 仅有部分常见功能，但更加简洁易用  默认值：`'default'`.

- htmlValue (string; optional):
    编辑器`html`格式内容.

- textValue (string; optional):
    编辑器纯文本内容.

- toolbarConfig (dict; default {    modalAppendToBody: False}):
    工具栏配置.

    `toolbarConfig` is a dict with keys:

    - toolbarKeys (list; optional):
        配置工具栏显示的菜单key，默认工具栏从左至右菜单对应的key为<br/>  [<br/>
        &emsp;\"headerSelect\",<br/>
        &emsp;\"blockquote\",<br/>                  &emsp;\"|\",<br/>
        &emsp;\"bold\",<br/>
        &emsp;\"underline\",<br/>
        &emsp;\"italic\",<br/>                  &emsp;{<br/>
        &emsp;&emsp;\"key\": \"group-more-style\",<br/>
        &emsp;&emsp;\"title\": \"更多\",<br/>
        &emsp;&emsp;\"iconSvg\": \"<svg viewBox=\\"0 0 1024
        1024\\"><path d=\\"M204.8 505.6m-76.8 0a76.8 76.8 0 1 0 153.6
        0 76.8 76.8 0 1 0-153.6 0Z\\"></path><path d=\\"M505.6
        505.6m-76.8 0a76.8 76.8 0 1 0 153.6 0 76.8 76.8 0 1 0-153.6
        0Z\\"></path><path d=\\"M806.4 505.6m-76.8 0a76.8 76.8 0 1 0
        153.6 0 76.8 76.8 0 1 0-153.6 0Z\\"></path></svg>\",<br/>
        &emsp;&emsp;\"menuKeys\": [<br/>
        &emsp;&emsp;&emsp;\"through\",<br/>
        &emsp;&emsp;&emsp;\"code\",<br/>
        &emsp;&emsp;&emsp;\"sup\",<br/>
        &emsp;&emsp;&emsp;\"sub\",<br/>
        &emsp;&emsp;&emsp;\"clearStyle\"</br>
        &emsp;&emsp;]<br/>                  &emsp;},<br/>
        &emsp;\"color\",<br/>                  &emsp;\"bgColor\",<br/>
        &emsp;\"|\",<br/>                  &emsp;\"fontSize\",<br/>
        &emsp;\"fontFamily\",<br/>
        &emsp;\"lineHeight\",<br/>                  &emsp;\"|\",<br/>
        &emsp;\"bulletedList\",<br/>
        &emsp;\"numberedList\",<br/>
        &emsp;\"todo\",<br/>                  &emsp;{<br/>
        &emsp;&emsp;\"key\": \"group-justify\",<br/>
        &emsp;&emsp;\"title\": \"对齐\",<br/>
        &emsp;&emsp;\"iconSvg\": \"<svg viewBox=\\"0 0 1024
        1024\\"><path d=\\"M768 793.6v102.4H51.2v-102.4h716.8z
        m204.8-230.4v102.4H51.2v-102.4h921.6z
        m-204.8-230.4v102.4H51.2v-102.4h716.8zM972.8
        102.4v102.4H51.2V102.4h921.6z\\"></path></svg>\",<br/>
        &emsp;&emsp;\"menuKeys\": [<br/>
        &emsp;&emsp;&emsp;\"justifyLeft\",<br/>
        &emsp;&emsp;&emsp;\"justifyRight\",<br/>
        &emsp;&emsp;&emsp;\"justifyCenter\",<br/>
        &emsp;&emsp;&emsp;\"justifyJustify\"</br>
        &emsp;&emsp;]<br/>                  &emsp;},<br/>
        &emsp;{<br/>                      &emsp;&emsp;\"key\":
        \"group-indent\",<br/>
        &emsp;&emsp;\"title\": \"缩进\",<br/>
        &emsp;&emsp;\"iconSvg\": \"<svg viewBox=\\"0 0 1024
        1024\\"><path d=\\"M0 64h1024v128H0z m384 192h640v128H384z m0
        192h640v128H384z m0 192h640v128H384zM0 832h1024v128H0z
        m0-128V320l256 192z\\"></path></svg>\",<br/>
        &emsp;&emsp;\"menuKeys\": [<br/>
        &emsp;&emsp;&emsp;\"indent\",<br/>
        &emsp;&emsp;&emsp;\"delIndent\"</br>
        &emsp;&emsp;]<br/>                  &emsp;},<br/>
        &emsp;\"|\",<br/>                  &emsp;\"emotion\",</br>
        &emsp;\"insertLink\",<br/>                  &emsp;{<br/>
        &emsp;&emsp;\"key\": \"group-image\",<br/>
        &emsp;&emsp;\"title\": \"图片\",<br/>
        &emsp;&emsp;\"iconSvg\": \"<svg viewBox=\\"0 0 1024
        1024\\"><path d=\\"M959.877 128l0.123 0.123v767.775l-0.123
        0.122H64.102l-0.122-0.122V128.123l0.122-0.123h895.775zM960
        64H64C28.795 64 0 92.795 0 128v768c0 35.205 28.795 64 64
        64h896c35.205 0 64-28.795
        64-64V128c0-35.205-28.795-64-64-64zM832 288.01c0 53.023-42.988
        96.01-96.01 96.01s-96.01-42.987-96.01-96.01S682.967 192 735.99
        192 832 234.988 832 288.01zM896 832H128V704l224.01-384 256
        320h64l224.01-192z\\"></path></svg>\",<br/>
        &emsp;&emsp;\"menuKeys\": [<br/>
        &emsp;&emsp;&emsp;\"insertImage\",<br/>
        &emsp;&emsp;&emsp;\"uploadImage\"<br/>
        &emsp;&emsp;]<br/>                  &emsp;},<br/>
        &emsp;{<br/>                      &emsp;&emsp;\"key\":
        \"group-video\",<br/>
        &emsp;&emsp;\"title\": \"视频\",<br/>
        &emsp;&emsp;\"iconSvg\": \"<svg viewBox=\\"0 0 1024
        1024\\"><path d=\\"M981.184 160.096C837.568 139.456 678.848
        128 512 128S186.432 139.456 42.816 160.096C15.296 267.808 0
        386.848 0 512s15.264 244.16 42.816 351.904C186.464 884.544
        345.152 896 512 896s325.568-11.456 469.184-32.096C1008.704
        756.192 1024 637.152 1024
        512s-15.264-244.16-42.816-351.904zM384 704V320l320 192-320
        192z\\"></path></svg>\",<br/
        &emsp;&emsp;\"menuKeys\": [<br/>
        &emsp;&emsp;&emsp;\"insertVideo\",<br/>
        &emsp;&emsp;&emsp;\"uploadVideo\"<br/>
        &emsp;&emsp;]<br/>                  &emsp;},<br/>
        &emsp;\"insertTable\",<br/>
        &emsp;\"codeBlock\",<br/>
        &emsp;\"divider\",<br/>                  &emsp;\"|\",<br/>
        &emsp;\"undo\",<br/>                  &emsp;\"redo\",<br/>
        &emsp;\"|\",<br/>                  &emsp;\"fullScreen\"<br/>
        ].

    - modalAppendToBody (boolean; optional):
        是否将菜单弹出的`modal`添加到`body`下  默认值：`False`.

- editorConfig (dict; default {    readOnly: False,    autoFocus: True,    scroll: True}):
    编辑器配置.

    `editorConfig` is a dict with keys:

    - placeholder (string; optional):
        配置编辑器`placeholder`.

    - readOnly (boolean; optional):
        配置编辑器是否只读  默认值：`False`.

    - autoFocus (boolean; optional):
        配置编辑器默认是否`focus`  默认值：`True`.

    - scroll (boolean; optional):
        配置编辑器是否支持滚动，注意，此时不要固定`editor-container`的高度，设置一个`min-height`即可，TIP：可将`scroll`设置为`False`的情况：编辑器高度自增、在线文档，如腾讯文档、语雀那样的
        默认值：`True`.

    - maxLength (number; optional):
        配置编辑器的`maxlength`，TIP：无特殊需求，请慎用`maxLength`，这可能会导致编辑器内容过多时，编辑卡顿.

    - MENU_CONF (dict; optional):
        配置菜单.

        `MENU_CONF` is a dict with keys:

        - color (list; optional):
            配置菜单文字颜色选项.

        - bgColor (list; optional):
            配置菜单背景颜色选项.

        - fontSize (dict; optional):
            配置菜单字号选项.

            `fontSize` is a dict with keys:

            - fontSizeList (list of dicts; optional)

                `fontSizeList` is a list of string

              Or dict with keys:

    - name (string; optional)

    - value (string; optional)s

        - fontFamily (dict; optional):
            配置菜单字体选项.

            `fontFamily` is a dict with keys:

            - fontFamilyList (list of dicts; optional)

                `fontFamilyList` is a list of string

              Or dict with keys:

    - name (string; optional)

    - value (string; optional)s

        - lineHeight (dict; optional):
            配置菜单行高选项.

            `lineHeight` is a dict with keys:

            - lineHeightList (list of strings; optional)

        - emotions (dict; optional):
            配置菜单表情选项.

            `emotions` is a dict with keys:

            - emotions (list of strings; optional)

        - codeSelectLang (dict; optional):
            配置代码高亮.

            `codeSelectLang` is a dict with keys:

            - codeLangs (list of dicts; optional):
                配置代码语言，可用的有：<br/>  [<br/>
                &emsp;{<br/>
                &emsp;&emsp;\"text\": \"CSS\",<br/>
                &emsp;&emsp;\"value\": \"css\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"HTML\",<br/>
                &emsp;&emsp;\"value\": \"html\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"XML\",<br/>
                &emsp;&emsp;\"value\": \"xml\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Javascript\",<br/>
                &emsp;&emsp;\"value\": \"javascript\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Typescript\",<br/>
                &emsp;&emsp;\"value\": \"typescript\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"JSX\",<br/>
                &emsp;&emsp;\"value\": \"jsx\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Go\",<br/>
                &emsp;&emsp;\"value\": \"go\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"PHP\",<br/>
                &emsp;&emsp;\"value\": \"php\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"C\",<br/>
                &emsp;&emsp;\"value\": \"c\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Python\",<br/>
                &emsp;&emsp;\"value\": \"python\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Java\",<br/>
                &emsp;&emsp;\"value\": \"java\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"C++\",<br/>
                &emsp;&emsp;\"value\": \"cpp\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"C#\",<br/>
                &emsp;&emsp;\"value\": \"csharp\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Visual Basic\",<br/>
                &emsp;&emsp;\"value\": \"visual-basic\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"SQL\",<br/>
                &emsp;&emsp;\"value\": \"sql\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Ruby\",<br/>
                &emsp;&emsp;\"value\": \"ruby\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Swift\",<br/>
                &emsp;&emsp;\"value\": \"swift\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Bash\",<br/>
                &emsp;&emsp;\"value\": \"bash\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Lua\",<br/>
                &emsp;&emsp;\"value\": \"lua\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Groovy\",<br/>
                &emsp;&emsp;\"value\": \"groovy\"<br/>
                &emsp;},<br/>                          &emsp;{<br/>
                &emsp;&emsp;\"text\": \"Markdown\",<br/>
                &emsp;&emsp;\"value\": \"markdown\"<br/>
                &emsp;}<br/>                      ].

                `codeLangs` is a list of dicts with keys:

    - text (string; optional)

    - value (string; optional)

- uploadImage (dict; default {    fieldName: 'wangeditor-uploaded-image',    maxFileSize: 2 * 1024 * 1024,    maxNumberOfFiles: 100,    allowedFileTypes: ['image/*'],    metaWithUrl: False,    withCredentials: False,    timeout: 10,    base64LimitSize: 0}):
    配置菜单图片上传.

    `uploadImage` is a dict with keys:

    - server (string; optional):
        配置上传的服务端地址，服务端`response body`格式要求如下：<br/>  上传成功的返回格式：<br/>
        {<br/>                  &emsp;\"errno\": 0, //
        注意：值是数字，不能是字符串<br/>                  &emsp;\"data\": {<br/>
        &emsp;&emsp;\"url\": \"xxx\", // 图片 src ，必须<br/>
        &emsp;&emsp;\"alt\": \"yyy\", // 图片描述文字，非必须<br/>
        &emsp;&emsp;\"href\": \"zzz\" // 图片的链接，非必须<br/>
        &emsp;}<br/>              }<br/>  上传失败的返回格式：<br/>{<br/>
        &emsp;\"errno\": 1, // 只要不等于 0 就行<br/>
        &emsp;\"message\": \"失败信息\"<br/>              }.

    - fieldName (string; optional):
        配置上传的`form-data fieldName`  默认值：`'wangeditor-uploaded-image'`.

    - maxFileSize (number; optional):
        配置单个文件的最大体积限制，单位为`B`  默认值：`2 * 1024 * 1024`.

    - maxNumberOfFiles (number; optional):
        配置最多可上传几个文件  默认值：`100`.

    - allowedFileTypes (list; optional):
        配置选择文件时的类型限制，默认为`['image/*']`，如不想限制，则设置为`[]`.

    - meta (dict; optional):
        配置自定义上传参数，例如传递验证的`token`等，参数会被添加到`formData`中，一起上传到服务端.

    - metaWithUrl (boolean; optional):
        配置是否将`meta`拼接到`url`参数中  默认`False`.

    - headers (dict; optional):
        配置自定义增加`http  header`.

    - withCredentials (boolean; optional):
        配置跨域是否传递`cookie`  默认值：`False`.

    - timeout (number; optional):
        配置超时时间，单位：秒  默认值：`10`.

    - base64LimitSize (number; optional):
        配置小于该值就插入`base64`格式（而不上传）  默认值：`0`.

- uploadVideo (dict; default {    fieldName: 'wangeditor-uploaded-video',    maxFileSize: 10 * 1024 * 1024,    maxNumberOfFiles: 5,    allowedFileTypes: ['video/*'],    metaWithUrl: False,    withCredentials: False,    timeout: 10}):
    配置菜单视频上传.

    `uploadVideo` is a dict with keys:

    - server (string; optional):
        配置上传的服务端地址，服务端`response body`格式要求如下：<br/>  上传成功的返回格式：<br/>
        {<br/>                  &emsp;\"errno\": 0, //
        注意：值是数字，不能是字符串<br/>                  &emsp;\"data\": {<br>
        &emsp;&emsp;\"url\": \"xxx\", // 视频 src ，必须<br/>
        &emsp;&emsp;\"poster\": \"xxx.png\" // 视频封面图片 url ，可选<br>
        &emsp;}<br/>              }<br/>  上传失败的返回格式：<br/>
        {<br/>                  &emsp;\"errno\": 1, // 只要不等于 0 就行<br/>
        &emsp;\"message\": \"失败信息\"<br/>              }<br/>.

    - fieldName (string; optional):
        配置上传的`form-data fieldName`  默认值：`'wangeditor-uploaded-video'`.

    - maxFileSize (number; optional):
        配置单个文件的最大体积限制，单位为`B`  默认值：`10 * 1024 * 1024`.

    - maxNumberOfFiles (number; optional):
        配置最多可上传几个文件  默认值：`5`.

    - allowedFileTypes (list; optional):
        选择文件时的类型限制，默认为`['video/*']`，如不想限制，则设置为`[]`.

    - meta (dict; optional):
        配置自定义上传参数，例如传递验证的`token`等，参数会被添加到`formData`中，一起上传到服务端.

    - metaWithUrl (boolean; optional):
        配置是否将`meta`拼接到`url`参数中  默认`False`.

    - headers (dict; optional):
        配置自定义增加`http  header`.

    - withCredentials (boolean; optional):
        配置跨域是否传递`cookie`  默认值：`False`.

    - timeout (number; optional):
        配置超时时间，单位：秒  默认值：`10`.

- successMessage (dict; optional):
    成功的消息提示配置.

    `successMessage` is a dict with keys:

    - className (string; optional):
        设置消息的`css`类名.

    - style (dict; optional):
        设置消息的`css`样式.

    - duration (number; optional):
        设置消息提示显示时长（单位：毫秒）  默认值：`4000`.

    - icon (a list of or a singular dash component, string or number; optional):
        自定义消息提示图标.

    - position (a value equal to: 'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'; optional):
        设置消息提示的弹出方位，可选的有`'top-left'`、`'top-center'`、`'top-right'`、`'bottom-left'`、`'bottom-center'`、`'bottom-right'`
        默认值：`'top-center'`.

- errorMessage (dict; optional):
    错误的消息提示配置.

    `errorMessage` is a dict with keys:

    - className (string; optional):
        设置消息的`css`类名.

    - style (dict; optional):
        设置消息的`css`样式.

    - duration (number; optional):
        设置消息提示显示时长（单位：毫秒）  默认值：`4000`.

    - icon (a list of or a singular dash component, string or number; optional):
        自定义消息提示图标.

    - position (a value equal to: 'top-left', 'top-center', 'top-right', 'bottom-left', 'bottom-center', 'bottom-right'; optional):
        设置消息提示的弹出方位，可选的有`'top-left'`、`'top-center'`、`'top-right'`、`'bottom-left'`、`'bottom-center'`、`'bottom-right'`
        默认值：`'top-center'`.

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

    - component_name (string; optional):
        Holds the name of the component that is loading."""
    _children_props = ['successMessage.icon', 'errorMessage.icon']
    _base_nodes = ['children']
    _namespace = 'feffery_utils_components'
    _type = 'FefferyRichTextEditor'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, toolbarClassName=Component.UNDEFINED, toolbarStyle=Component.UNDEFINED, editorClassName=Component.UNDEFINED, editorStyle=Component.UNDEFINED, locale=Component.UNDEFINED, mode=Component.UNDEFINED, htmlValue=Component.UNDEFINED, textValue=Component.UNDEFINED, toolbarConfig=Component.UNDEFINED, editorConfig=Component.UNDEFINED, uploadImage=Component.UNDEFINED, uploadVideo=Component.UNDEFINED, successMessage=Component.UNDEFINED, errorMessage=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'style', 'className', 'toolbarClassName', 'toolbarStyle', 'editorClassName', 'editorStyle', 'locale', 'mode', 'htmlValue', 'textValue', 'toolbarConfig', 'editorConfig', 'uploadImage', 'uploadVideo', 'successMessage', 'errorMessage', 'loading_state']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'style', 'className', 'toolbarClassName', 'toolbarStyle', 'editorClassName', 'editorStyle', 'locale', 'mode', 'htmlValue', 'textValue', 'toolbarConfig', 'editorConfig', 'uploadImage', 'uploadVideo', 'successMessage', 'errorMessage', 'loading_state']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(FefferyRichTextEditor, self).__init__(**args)
