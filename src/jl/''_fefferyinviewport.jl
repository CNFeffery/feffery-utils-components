# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyinviewport

"""
    ''_fefferyinviewport(;kwargs...)
    ''_fefferyinviewport(children::Any;kwargs...)
    ''_fefferyinviewport(children_maker::Function;kwargs...)


A FefferyInViewport component.

Keyword arguments:
- `children` (optional)
- `id` (optional)
- `inViewport` (optional)
- `loading_state` (optional)
- `setProps` (optional): Dash-assigned callback that should be called to report property changes
to Dash, to make them available for callbacks.
- `threshold` (optional)
"""
function ''_fefferyinviewport(; kwargs...)
        available_props = Symbol[:children, :id, :inViewport, :loading_state, :threshold]
        wild_props = Symbol[]
        return Component("''_fefferyinviewport", "FefferyInViewport", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferyinviewport(children::Any; kwargs...) = ''_fefferyinviewport(;kwargs..., children = children)
''_fefferyinviewport(children_maker::Function; kwargs...) = ''_fefferyinviewport(children_maker(); kwargs...)

