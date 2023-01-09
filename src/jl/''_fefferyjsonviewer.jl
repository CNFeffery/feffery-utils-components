# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferyjsonviewer

"""
    ''_fefferyjsonviewer(;kwargs...)

A FefferyJsonViewer component.

Keyword arguments:
- `id` (String; optional)
- `addible` (Bool; optional)
- `className` (String | Dict; optional)
- `collapseStringsAfterLength` (Bool | Real; optional)
- `collapsed` (Bool | Real; optional)
- `data` (Dict; optional)
- `deletable` (Bool; optional)
- `displayArrayKey` (Bool; optional)
- `displayDataTypes` (Bool; optional)
- `displayObjectSize` (Bool; optional)
- `editable` (Bool; optional)
- `enableClipboard` (Bool; optional)
- `groupArraysAfterLength` (Real; optional)
- `iconStyle` (a value equal to: 'circle', 'triangle', 'square'; optional)
- `indent` (Real; optional)
- `key` (String; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `quotesOnKeys` (Bool; optional)
- `sortKeys` (Bool; optional)
- `style` (Dict; optional)
- `theme` (a value equal to: 'apathy', 'apathy:inverted', 'ashes', 'bespin', 'brewer', 'bright:inverted', 'bright', 'chalk', 'codeschool', 'colors', 'eighties', 'embers', 'flat', 'google', 'grayscale', 'grayscale:inverted', 'greenscreen', 'harmonic', 'hopscotch', 'isotope', 'marrakesh', 'mocha', 'monokai', 'ocean', 'paraiso', 'pop', 'railscasts', 'rjv-default', 'shapeshifter', 'shapeshifter:inverted', 'solarized', 'summerfruit', 'summerfruit:inverted', 'threezerotwofour', 'tomorrow', 'tube', 'twilight'; optional)
"""
function ''_fefferyjsonviewer(; kwargs...)
        available_props = Symbol[:id, :addible, :className, :collapseStringsAfterLength, :collapsed, :data, :deletable, :displayArrayKey, :displayDataTypes, :displayObjectSize, :editable, :enableClipboard, :groupArraysAfterLength, :iconStyle, :indent, :key, :loading_state, :quotesOnKeys, :sortKeys, :style, :theme]
        wild_props = Symbol[]
        return Component("''_fefferyjsonviewer", "FefferyJsonViewer", "feffery_utils_components", available_props, wild_props; kwargs...)
end

