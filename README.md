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

简体中文 | [English](./README-en_US.md)

`feffery-components`计划子项目，`Plotly Dash`第三方组件库，将超多实用辅助功能组件引入`Dash`的世界 🥳，最新版本：`0.3.5`（2026-01-16）

## Dash版本兼容性说明

| fuc版本 | 适用Dash版本 |
| :-----: | :----------: |
| >=0.3.0 |   >=3.0.0    |
| <0.3.0  |    <3.0.0    |

## 1 最新版本安装方式

```bash
pip install feffery-utils-components -U
```

## 2 最新预发布版本安装方式

> [!NOTE]  
> 最新预发布版本（2025-06-27）：`0.3.0rc4`

```bash
pip install feffery-utils-components --pre -U
```

## 3 静态资源 CDN 加速方法

```Python
# 非debug模式下对Dash()传入参数serve_locally=False会强制浏览器端从unpkg cdn加载各个依赖的
# xxx.min.js等静态资源，从而避免占用服务器带宽，适合中小型站点加速访问
app = dash.Dash(serve_locally=False)
```

## 4 在线文档

<a href='http://fuc.feffery.tech/' target='_blank'>文档地址</a>

## 5 贡献者

<a href = "https://github.com/CNFeffery/feffery-utils-components/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=CNFeffery/feffery-utils-components"/>
</a>
