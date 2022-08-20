# AUTO GENERATED FILE - DO NOT EDIT

export ''_fefferysyntaxhighlighter

"""
    ''_fefferysyntaxhighlighter(;kwargs...)

A FefferySyntaxHighlighter component.

Keyword arguments:
- `id` (String; optional)
- `codeBlockStyle` (Dict; optional)
- `codeStyle` (Dict; optional)
- `codeTheme` (a value equal to: 'a11y-dark', 'atom-dark', 'coldark-cold', 'coldark-dark', 'coy', 'coy-without-shadows', 'darcula', 'dracula', 'nord', 'okaidia', 'prism', 'solarizedlight', 'twilight', 'duotone-sea', 'duotone-dark', 'duotone-light', 'duotone-space', 'gh-colors', 'gruvbox-dark', 'material-dark', 'night-owl', 'one-light', 'pojoaque', 'solarized-dark-atom', 'synthwave84', 'z-touch'; optional)
- `loading_state` (optional): . loading_state has the following type: lists containing elements 'is_loading', 'prop_name', 'component_name'.
Those elements have the following types:
  - `is_loading` (Bool; optional): Determines if the component is loading or not
  - `prop_name` (String; optional): Holds which property is loading
  - `component_name` (String; optional): Holds the name of the component that is loading
- `showLineNumbers` (Bool; optional)
"""
function ''_fefferysyntaxhighlighter(; kwargs...)
        available_props = Symbol[:id, :codeBlockStyle, :codeStyle, :codeTheme, :loading_state, :showLineNumbers]
        wild_props = Symbol[]
        return Component("''_fefferysyntaxhighlighter", "FefferySyntaxHighlighter", "feffery_utils_components", available_props, wild_props; kwargs...)
end

