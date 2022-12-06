# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferywebsocket

"""
    ''_fefferywebsocket(;kwargs...)

A FefferyWebSocket component.

Keyword arguments:
- `id` (String; optional)
- `latestMessage` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `message` (String; optional)
- `operation` (a value equal to: 'connect', 'disconnect', 'send'; optional)
- `reconnectInterval` (Real; optional)
- `reconnectLimit` (Real; optional)
- `socketUrl` (String; required)
- `state` (a value equal to: 'connecting', 'open', 'closing', 'closed'; optional)
"""
function ''_fefferywebsocket(; kwargs...)
        available_props = Symbol[:id, :latestMessage, :loading_state, :message, :operation, :reconnectInterval, :reconnectLimit, :socketUrl, :state]
        wild_props = Symbol[]
        return Component("''_fefferywebsocket", "FefferyWebSocket", "feffery_utils_components", available_props, wild_props; kwargs...)
end

