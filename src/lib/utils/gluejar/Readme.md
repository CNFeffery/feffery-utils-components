# React Gluejar

> Collects the images you paste from your clipboard.

![Demo using `react-gluejar`](/.github/gluejar.gif)

## Installation

```sh
yarn add @charliewilco/gluejar
```

## Example

```js
import React, { Component } from 'react'
import { Gluejar } from '@charliewilco/gluejar'

class App extends Component {
  render() {
    return (
      <Gluejar onPaste={files => console.log(files)} onError={err => console.error(err)}>
        {({ images }) =>
          images.length > 0 &&
          images.map(image => <img src={image} key={image} alt={`Pasted: ${image}`} />)
        }
      </Gluejar>
    )
  }
}
```

Run this example locally by [cloning the repo](https://help.github.com/articles/cloning-a-repository/) and running `yarn example` in the root directory. You can visit the example [here](https://react-gluejar.now.sh/).

## Usage

### Available Props

| Prop            | Type            | Description                                      | Default                                                 |
| --------------- | --------------- | ------------------------------------------------ | ------------------------------------------------------- |
| `onPaste`       | `Function`      | returns Array of image Blobs, responds to events | `() => null`                                            |
| `onError`       | `Function`      | returns error messages                           | `() => null`                                            |
| `children`      | `Function`      | returns Array of history of pasted images        | N/A                                                     |
| `acceptedFiles` | `Array<String>` | Array of accepted files to check for             | `['image/gif', 'image/png', 'image/jpeg', 'image/bmp']` |
| `container`     | `Element`       | Element object to listen on                      | `window`                                                |

### Browser Support

| Browser | Support |
| ------- | ------- |
| Chrome  | 👍      |
| IE      | 👎      |
| Firefox | 🙄      |
| Edge    | 👍      |
| Safari  | 👍      |
| Opera   | 👍      |

🙄 = Look there's something going on in Firefox for a while. You can read the tracking issue [here](https://bugzilla.mozilla.org/show_bug.cgi?id=906420), but I don't insight into their timeline or priority.
