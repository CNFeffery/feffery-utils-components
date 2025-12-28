<p align="center">
	<img src="./fuc-logo.svg" height=200></img>
</p>
<h1 align="center">feffery-utils-components</h1>
<div align="center">

[![GitHub](https://img.shields.io/github/license/plotly/dash.svg?color=dark-green)](https://github.com/plotly/dash/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/feffery-utils-components.svg?color=dark-green)](https://pypi.org/project/feffery-utils-components/)
[![Downloads](https://pepy.tech/badge/feffery-utils-components)](https://pepy.tech/project/feffery-utils-components)
[![Downloads](https://pepy.tech/badge/feffery-utils-components/month)](https://pepy.tech/project/feffery-utils-components)

</div>

[简体中文](./README.md) | English

A sub-project of the `feffery-components` plan, this `Plotly Dash` third-party component library brings numerous practical utility components to the world of `Dash` 🥳, latest version: `0.3.4`(2025-12-28)

## Dash Version Compatibility

| fuc version | Compatible Dash version |
| :-----: | :----------: |
| >=0.3.0 |   >=3.0.0    |
| <0.3.0  |    <3.0.0    |

## 1 Installation Method for Latest Version

```bash
pip install feffery-utils-components -U
```

## 2 Installation Method for Latest Pre-release Version

> [!NOTE]  
> Latest pre-release version (2025-06-27): `0.3.0rc4`

```bash
pip install feffery-utils-components --pre -U
```

## 3 Static Resource CDN Acceleration Method

```Python
# In non-debug mode, passing serve_locally=False to Dash() forces the browser to load
# dependent xxx.min.js and other static resources from unpkg cdn, avoiding server bandwidth usage
# and suitable for small to medium-sized sites to accelerate access
app = dash.Dash(serve_locally=False)
```

## 4 Online Documentation

<a href='http://fuc.feffery.tech/' target='_blank'>Documentation Link</a>

## 5 Contributors

<a href = "https://github.com/CNFeffery/feffery-utils-components/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=CNFeffery/feffery-utils-components"/>
</a>