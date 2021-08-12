
module FefferyUtilsComponents
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/''_fefferycaptcha.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "feffery_utils_components",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "feffery_utils_components.min.js",
    external_url = "https://unpkg.com/feffery_utils_components@0.0.1/feffery_utils_components/feffery_utils_components.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "feffery_utils_components.min.js.map",
    external_url = "https://unpkg.com/feffery_utils_components@0.0.1/feffery_utils_components/feffery_utils_components.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
