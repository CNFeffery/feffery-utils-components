# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyexternaljs

"""
    ''_fefferyexternaljs(;kwargs...)

A FefferyExternalJs component.

Keyword arguments:
- `id` (String; optional)
- `jsUrl` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `recentlyStatus` (a value equal to: 'unset', 'loading', 'ready', 'error'; optional)
"""
function ''_fefferyexternaljs(; kwargs...)
        available_props = Symbol[:id, :jsUrl, :loading_state, :recentlyStatus]
        wild_props = Symbol[]
        return Component("''_fefferyexternaljs", "FefferyExternalJs", "feffery_utils_components", available_props, wild_props; kwargs...)
end

