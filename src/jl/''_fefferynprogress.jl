# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferynprogress

"""
    ''_fefferynprogress(;kwargs...)
    ''_fefferynprogress(children::Any;kwargs...)
    ''_fefferynprogress(children_maker::Function;kwargs...)


A FefferyNprogress component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `excludeProps` (Array of Strings; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
"""
function ''_fefferynprogress(; kwargs...)
        available_props = Symbol[:children, :id, :className, :excludeProps, :loading_state, :style]
        wild_props = Symbol[]
        return Component("''_fefferynprogress", "FefferyNprogress", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferynprogress(children::Any; kwargs...) = ''_fefferynprogress(;kwargs..., children = children)
''_fefferynprogress(children_maker::Function; kwargs...) = ''_fefferynprogress(children_maker(); kwargs...)

