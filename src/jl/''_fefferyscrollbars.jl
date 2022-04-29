# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyscrollbars

"""
    ''_fefferyscrollbars(;kwargs...)
    ''_fefferyscrollbars(children::Any;kwargs...)
    ''_fefferyscrollbars(children_maker::Function;kwargs...)


A FefferyScrollbars component.

Keyword arguments:
- `children` (optional)
- `id` (optional)
- `autoHide` (optional)
- `className` (optional)
- `classNames` (optional)
- `forceVisible` (optional)
- `loading_state` (optional)
- `scrollbarMaxSize` (optional)
- `scrollbarMinSize` (optional)
- `style` (optional)
- `timeout` (optional)
"""
function ''_fefferyscrollbars(; kwargs...)
        available_props = Symbol[:children, :id, :autoHide, :className, :classNames, :forceVisible, :loading_state, :scrollbarMaxSize, :scrollbarMinSize, :style, :timeout]
        wild_props = Symbol[]
        return Component("''_fefferyscrollbars", "FefferyScrollbars", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyscrollbars(children::Any; kwargs...) = ''_fefferyscrollbars(;kwargs..., children = children)
''_fefferyscrollbars(children_maker::Function; kwargs...) = ''_fefferyscrollbars(children_maker(); kwargs...)

