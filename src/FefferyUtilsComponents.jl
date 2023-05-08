
module FefferyUtilsComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.1.28"

include("jl/''_fefferyautoanimate.jl")
include("jl/''_fefferymotion.jl")
include("jl/''_fefferyblockcolorpicker.jl")
include("jl/''_fefferycirclecolorpicker.jl")
include("jl/''_fefferyeyedropper.jl")
include("jl/''_fefferygithubcolorpicker.jl")
include("jl/''_fefferyhexcolorpicker.jl")
include("jl/''_fefferyrgbcolorpicker.jl")
include("jl/''_fefferytwittercolorpicker.jl")
include("jl/''_fefferywheelcolorpicker.jl")
include("jl/''_fefferygrid.jl")
include("jl/''_fefferygriditem.jl")
include("jl/''_fefferycaptcha.jl")
include("jl/''_fefferycountdown.jl")
include("jl/''_fefferycountup.jl")
include("jl/''_fefferycssvar.jl")
include("jl/''_fefferydiv.jl")
include("jl/''_fefferyexecutejs.jl")
include("jl/''_fefferyexternalcss.jl")
include("jl/''_fefferyexternaljs.jl")
include("jl/''_fefferyextraspinner.jl")
include("jl/''_fefferyfancybutton.jl")
include("jl/''_fefferyfancymessage.jl")
include("jl/''_fefferyfancynotification.jl")
include("jl/''_fefferyfullscreen.jl")
include("jl/''_fefferyguide.jl")
include("jl/''_fefferyhighlightwords.jl")
include("jl/''_fefferyimagepaste.jl")
include("jl/''_fefferyjsonviewer.jl")
include("jl/''_fefferylazyload.jl")
include("jl/''_fefferyqrcode.jl")
include("jl/''_fefferyrawhtml.jl")
include("jl/''_fefferyreload.jl")
include("jl/''_fefferyscroll.jl")
include("jl/''_fefferyscrollbars.jl")
include("jl/''_fefferysettitle.jl")
include("jl/''_fefferyshadowdom.jl")
include("jl/''_fefferyshortcutpanel.jl")
include("jl/''_fefferysticky.jl")
include("jl/''_fefferystyle.jl")
include("jl/''_fefferytimeout.jl")
include("jl/''_fefferytopprogress.jl")
include("jl/''_fefferyvirtuallist.jl")
include("jl/''_fefferywebsocket.jl")
include("jl/''_fefferydevicedetect.jl")
include("jl/''_fefferydocumentvisibility.jl")
include("jl/''_fefferygeolocation.jl")
include("jl/''_fefferyidle.jl")
include("jl/''_fefferyinviewport.jl")
include("jl/''_fefferykeypress.jl")
include("jl/''_fefferylistenpaste.jl")
include("jl/''_fefferylistenscroll.jl")
include("jl/''_fefferylistenunload.jl")
include("jl/''_fefferylocation.jl")
include("jl/''_fefferymouseposition.jl")
include("jl/''_fefferyresponsive.jl")
include("jl/''_fefferywindowsize.jl")
include("jl/''_fefferysortablecontainer.jl")
include("jl/''_fefferysortableitem.jl")
include("jl/''_fefferysplit.jl")
include("jl/''_fefferysplitpane.jl")
include("jl/''_fefferysessionstorage.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "feffery_utils_components",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "feffery_utils_components.min.js",
    external_url = "https://unpkg.com/feffery_utils_components@0.1.28/feffery_utils_components/feffery_utils_components.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "feffery_utils_components.min.js.map",
    external_url = "https://unpkg.com/feffery_utils_components@0.1.28/feffery_utils_components/feffery_utils_components.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
