# AUTO GENERATED FILE - DO NOT EDIT

''FefferyCaptcha <- function(id=NULL, bgColor=NULL, captcha=NULL, charNum=NULL, className=NULL, fontSize=NULL, height=NULL, loading_state=NULL, style=NULL, width=NULL) {
    
    props <- list(id=id, bgColor=bgColor, captcha=captcha, charNum=charNum, className=className, fontSize=fontSize, height=height, loading_state=loading_state, style=style, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FefferyCaptcha',
        namespace = 'feffery_utils_components',
        propNames = c('id', 'bgColor', 'captcha', 'charNum', 'className', 'fontSize', 'height', 'loading_state', 'style', 'width'),
        package = 'fefferyUtilsComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
