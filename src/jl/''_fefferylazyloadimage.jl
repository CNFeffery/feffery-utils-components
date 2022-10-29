# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferylazyloadimage

"""
    ''_fefferylazyloadimage(;kwargs...)

A FefferyLazyLoadImage component.

Keyword arguments:
- `id` (String; optional)
- `alt` (String; optional)
- `height` (String | Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `placeholderSrc` (String; optional)
- `src` (String; optional)
- `threshold` (Real; optional)
- `width` (String | Real; optional)
"""
function ''_fefferylazyloadimage(; kwargs...)
        available_props = Symbol[:id, :alt, :height, :loading_state, :placeholderSrc, :src, :threshold, :width]
        wild_props = Symbol[]
        return Component("''_fefferylazyloadimage", "FefferyLazyLoadImage", "feffery_utils_components", available_props, wild_props; kwargs...)
end

