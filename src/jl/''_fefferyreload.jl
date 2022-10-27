# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyreload

"""
    ''_fefferyreload(;kwargs...)

A FefferyReload component.

Keyword arguments:
- `id` (String; optional)
- `delay` (Real; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `reload` (Bool; optional)
"""
function ''_fefferyreload(; kwargs...)
        available_props = Symbol[:id, :delay, :loading_state, :reload]
        wild_props = Symbol[]
        return Component("''_fefferyreload", "FefferyReload", "feffery_utils_components", available_props, wild_props; kwargs...)
end

