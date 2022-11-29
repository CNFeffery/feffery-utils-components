# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferytopprogress

"""
    ''_fefferytopprogress(;kwargs...)
    ''_fefferytopprogress(children::Any;kwargs...)
    ''_fefferytopprogress(children_maker::Function;kwargs...)


A FefferyTopProgress component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `color` (String; optional)
- `debug` (Bool; optional)
- `easing` (String; optional)
- `excludeProps` (Array of Strings; optional)
- `includeProps` (Array of Strings; optional)
- `listenPropsMode` (a value equal to: 'default', 'exclude', 'include'; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `minimum` (Real; optional)
- `showSpinner` (Bool; optional)
- `speed` (Real; optional)
- `spinning` (Bool; optional)
- `style` (Dict; optional)
- `zIndex` (Real; optional)
"""
function ''_fefferytopprogress(; kwargs...)
        available_props = Symbol[:children, :id, :className, :color, :debug, :easing, :excludeProps, :includeProps, :listenPropsMode, :loading_state, :minimum, :showSpinner, :speed, :spinning, :style, :zIndex]
        wild_props = Symbol[]
        return Component("''_fefferytopprogress", "FefferyTopProgress", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferytopprogress(children::Any; kwargs...) = ''_fefferytopprogress(;kwargs..., children = children)
''_fefferytopprogress(children_maker::Function; kwargs...) = ''_fefferytopprogress(children_maker(); kwargs...)

