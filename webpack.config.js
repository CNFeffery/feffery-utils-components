const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');
const webpack = require('webpack');
const WebpackDashDynamicImport = require('@plotly/webpack-dash-dynamic-import');
const packagejson = require('./package.json');
// const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

const dashLibraryName = packagejson.name.replace(/-/g, '_');

module.exports = (env, argv) => {

    let mode;

    const overrides = module.exports || {};

    // if user specified mode flag take that value
    if (argv && argv.mode) {
        mode = argv.mode;
    }

    // else if configuration object is already set (module.exports) use that value
    else if (overrides.mode) {
        mode = overrides.mode;
    }

    // else take webpack default (production)
    else {
        mode = 'production';
    }

    let filename = (overrides.output || {}).filename;
    if (!filename) {
        const modeSuffix = mode === 'development' ? 'dev' : 'min';
        filename = `${dashLibraryName}.${modeSuffix}.js`;
    }

    const entry = overrides.entry || { main: './src/lib/index.js' };

    const devtool = overrides.devtool || 'source-map';

    const externals = ('externals' in overrides) ? overrides.externals : ({
        react: 'React',
        'react-dom': 'ReactDOM',
        'plotly.js': 'Plotly',
        'prop-types': 'PropTypes',
    });

    return {
        mode,
        entry,
        output: {
            path: path.resolve(__dirname, dashLibraryName),
            chunkFilename: '[name].js',
            filename,
            library: dashLibraryName,
            libraryTarget: 'window',
        },
        // devtool: false, // 开发阶段使用，生成全量source-map
        devtool, // 发布阶段使用，生成最小化source-map
        externals,
        module: {
            rules: [
                {
                    test: /\.(woff2|woff|ttf|svg|eot)$/, //fonts目录下四个文件后缀名
                    use: ["url-loader"],
                },
                {
                    test: /\.(woff|ttf)$/,
                    exclude: /node_modules\/katex\/dist\/fonts/,
                    use: {
                        loader: 'ignore-loader'
                    }
                },
                {
                    test: /\.jsx?$/,
                    exclude: /node_modules/,
                    use: {
                        loader: 'babel-loader'
                    }
                },
                {
                    test: /\.js$/,
                    include: [
                        path.resolve('node_modules', '@lit'),
                        path.resolve('node_modules', 'lit-element'),
                        path.resolve('node_modules', 'lit-html'),
                        path.resolve('node_modules', '@shoelace-style'),
                        path.resolve('node_modules', 'emoji-mart'),
                        path.resolve('node_modules', '@photo-sphere-viewer'),
                        path.resolve('node_modules', 'wouter'),
                        path.resolve('node_modules', 'autofit.js'),
                    ],
                    use: {
                        loader: 'babel-loader',
                        options: {
                            presets: ['@babel/preset-env'],
                            plugins: [
                                '@babel/plugin-proposal-optional-chaining',
                                '@babel/plugin-proposal-nullish-coalescing-operator'
                            ]
                        }
                    }
                },
                {
                    test: /\.mjs$/,
                    include: /node_modules/,
                    type: "javascript/auto"
                },
                {
                    test: /\.(css|less)$/,
                    use: [
                        {
                            loader: 'style-loader',
                            options: {
                                insertAt: 'top'
                            }
                        },
                        {
                            loader: 'css-loader',
                        },
                        {
                            loader: 'less-loader',
                            options: {
                                javascriptEnabled: true
                            }
                        },
                    ],
                },
                {
                    test: /\.s[ac]ss$/i,
                    use: [
                        // 将 JS 字符串生成为 style 节点
                        'style-loader',
                        // 将 CSS 转化成 CommonJS 模块
                        'css-loader',
                        // 将 Sass 编译成 CSS
                        'sass-loader',
                    ]
                }
            ]
        },
        optimization: {
            minimizer: [
                new TerserPlugin({
                    sourceMap: true,
                    parallel: true,
                    cache: './.build_cache/terser',
                    terserOptions: {
                        warnings: false,
                        ie8: false
                    }
                })
            ],
            splitChunks: {
                name: '[name].js',
                cacheGroups: {
                    async: {
                        chunks: 'async',
                        minSize: 0,
                        name(module, chunks, cacheGroupKey) {
                            return `${cacheGroupKey}-${chunks[0].name}`;
                        }
                    },
                    shared: {
                        chunks: 'all',
                        minSize: 0,
                        minChunks: 2,
                        name: 'async-fuc-shared'
                    }
                }
            }
        },
        plugins: [
            // new BundleAnalyzerPlugin(),
            new WebpackDashDynamicImport(),
            new webpack.SourceMapDevToolPlugin({
                filename: '[file].map',
                exclude: ['async-plotlyjs']
            }),
        ]
    }
};
