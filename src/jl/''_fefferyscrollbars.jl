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
- `autoHideDuration` (optional)
- `autoHideTimeout` (optional)
- `className` (optional)
- `loading_state` (optional)
- `style` (optional)
- `thumbSize` (optional)
"""
function ''_fefferyscrollbars(; kwargs...)
        available_props = Symbol[:children, :id, :autoHide, :autoHideDuration, :autoHideTimeout, :className, :loading_state, :style, :thumbSize]
        wild_props = Symbol[]
        return Component("''_fefferyscrollbars", "FefferyScrollbars", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyscrollbars(children::Any; kwargs...) = ''_fefferyscrollbars(;kwargs..., children = children)
''_fefferyscrollbars(children_maker::Function; kwargs...) = ''_fefferyscrollbars(children_maker(); kwargs...)

