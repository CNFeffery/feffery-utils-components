# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferylocation

"""
    ''_fefferylocation(;kwargs...)

A FefferyLocation component.

Keyword arguments:
- `id` (String; optional)
- `hash` (String; optional)
- `host` (String; optional)
- `hostname` (String; optional)
- `href` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `pathname` (String; optional)
- `port` (String; optional)
- `protocol` (String; optional)
- `search` (String; optional)
- `trigger` (a value equal to: 'load', 'pushstate', 'popstate'; optional)
"""
function ''_fefferylocation(; kwargs...)
        available_props = Symbol[:id, :hash, :host, :hostname, :href, :loading_state, :pathname, :port, :protocol, :search, :trigger]
        wild_props = Symbol[]
        return Component("''_fefferylocation", "FefferyLocation", "feffery_utils_components", available_props, wild_props; kwargs...)
end

