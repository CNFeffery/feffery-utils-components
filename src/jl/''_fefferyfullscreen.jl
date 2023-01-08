# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyfullscreen

"""
    ''_fefferyfullscreen(;kwargs...)

A FefferyFullscreen component.

Keyword arguments:
- `id` (String; optional)
- `isFullscreen` (Bool; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `targetId` (String; required)
"""
function ''_fefferyfullscreen(; kwargs...)
        available_props = Symbol[:id, :isFullscreen, :loading_state, :targetId]
        wild_props = Symbol[]
        return Component("''_fefferyfullscreen", "FefferyFullscreen", "feffery_utils_components", available_props, wild_props; kwargs...)
end

