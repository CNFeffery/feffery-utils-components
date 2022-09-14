
module FefferyUtilsComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.20"

include("jl/''_fefferyblockcolorpicker.jl")
include("jl/''_fefferycirclecolorpicker.jl")
include("jl/''_fefferygithubcolorpicker.jl")
include("jl/''_fefferyhexcolorpicker.jl")
include("jl/''_fefferyrgbcolorpicker.jl")
include("jl/''_fefferytwittercolorpicker.jl")
include("jl/''_fefferywheelcolorpicker.jl")
include("jl/''_fefferycaptcha.jl")
include("jl/''_fefferyexecutejs.jl")
include("jl/''_fefferyextraspinner.jl")
include("jl/''_fefferyguide.jl")
include("jl/''_fefferyhighlightwords.jl")
include("jl/''_fefferylazyload.jl")
include("jl/''_fefferylocation.jl")
include("jl/''_fefferyscroll.jl")
include("jl/''_fefferyscrollbars.jl")
include("jl/''_fefferyshortcutpanel.jl")
include("jl/''_fefferysyntaxhighlighter.jl")
include("jl/''_fefferytopprogress.jl")
include("jl/''_fefferyvirtuallist.jl")
include("jl/''_fefferydiv.jl")
include("jl/''_fefferydocumentvisibility.jl")
include("jl/''_fefferyinviewport.jl")
include("jl/''_fefferysplit.jl")
include("jl/''_fefferysplitpane.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "feffery_utils_components",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "feffery_utils_components.min.js",
    external_url = "https://unpkg.com/feffery_utils_components@0.0.20/feffery_utils_components/feffery_utils_components.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "feffery_utils_components.min.js.map",
    external_url = "https://unpkg.com/feffery_utils_components@0.0.20/feffery_utils_components/feffery_utils_components.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
