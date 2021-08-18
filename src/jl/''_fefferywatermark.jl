# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferywatermark

"""
    ''_fefferywatermark(;kwargs...)
    ''_fefferywatermark(children::Any;kwargs...)
    ''_fefferywatermark(children_maker::Function;kwargs...)


A FefferyWaterMark component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; optional)
- `className` (String; optional)
- `content` (String; optional)
- `fontColor` (String; optional)
- `fontSize` (Real; optional)
- `gapX` (Real; optional)
- `gapY` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `rotate` (Real; optional)
- `style` (Dict; optional)
- `zIndex` (Real; optional)
"""
function ''_fefferywatermark(; kwargs...)
        available_props = Symbol[:children, :id, :className, :content, :fontColor, :fontSize, :gapX, :gapY, :loading_state, :rotate, :style, :zIndex]
        wild_props = Symbol[]
        return Component("''_fefferywatermark", "FefferyWaterMark", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferywatermark(children::Any; kwargs...) = ''_fefferywatermark(;kwargs..., children = children)
''_fefferywatermark(children_maker::Function; kwargs...) = ''_fefferywatermark(children_maker(); kwargs...)

