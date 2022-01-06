# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferypasteimage

"""
    ''_fefferypasteimage(;kwargs...)
    ''_fefferypasteimage(children::Any;kwargs...)
    ''_fefferypasteimage(children_maker::Function;kwargs...)


A FefferyPasteImage component.

Keyword arguments:
- `children` (a list of or a singular dash component, string or number; optional): The content of the tab - will only be displayed if this tab is selected
- `id` (String; required)
- `className` (String; optional)
- `currentPastedImages` (Array of Bool | Real | String | Dict | Arrays; optional)
- `deletedIdx` (Array of Reals; optional)
- `imageHeight` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `style` (Dict; optional)
"""
function ''_fefferypasteimage(; kwargs...)
        available_props = Symbol[:children, :id, :className, :currentPastedImages, :deletedIdx, :imageHeight, :loading_state, :style]
        wild_props = Symbol[]
        return Component("''_fefferypasteimage", "FefferyPasteImage", "feffery_utils_components", available_props, wild_props; kwargs...)
end

''_fefferypasteimage(children::Any; kwargs...) = ''_fefferypasteimage(;kwargs..., children = children)
''_fefferypasteimage(children_maker::Function; kwargs...) = ''_fefferypasteimage(children_maker(); kwargs...)

