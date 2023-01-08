import * as React from 'react'

/* <PasteContainer
  onPaste={files => files.length > 0 && this.props.onFileAccepted(files[0], files[0])}
/> */

// NOTE: `onPaste` should return an array of files that were acceptedFiles
//
// const Image = ({ src }) => <img src={image} alt={`Pasted: ${image}`} />
//
// <PasteContainer
//    onPaste={files => this.method(files)}
//    onError={err => console.error(err)}
// >
//   {({images}) => images.map((image, i) => <Image src={image} key={i} />)}
// </PasteContainer>

export interface GluejarState {
  images: string[]
}

export interface GluejarProps {
  children?: (state: GluejarState) => React.ReactNode
  container: HTMLElement
  onPaste: (state: GluejarState) => void
  onError: (error: string) => void
  acceptedFiles: string[]
}

type BlobLikeFile = File | null

export class Gluejar extends React.Component<GluejarProps, GluejarState> {
  static displayName = 'Gluejar'

  static defaultProps = {
    onPaste: () => null,
    errorHandler: () => null,
    acceptedFiles: ['image/gif', 'image/png', 'image/jpeg', 'image/bmp']
  }

  state = {
    images: []
  }

  getContainer = (): HTMLElement => this.props.container || window

  isValidFormat = (fileType: string): boolean => this.props.acceptedFiles.includes(fileType)

  pasteHandler = (e: ClipboardEvent) => this.checkPasted(e, this.pushImage)

  transformImages = (data: DataTransfer, cb: Function) => {
    // NOTE: This needs to be a for loop, it's a list like object
    for (let i = 0; i < data.items.length; i++) {
      if (this.isValidFormat(data.items[i].type) !== false) {
        let blob: BlobLikeFile = data.items[i].getAsFile()
        let URL = window.URL

        if (blob) {
          // We shouldn't fire the callback if we can't create `new Blob()`
          let src = URL.createObjectURL(blob)

          cb(src)
        }
      } else {
        this.props.onError(`Sorry, that's not a format we support`)
      }
    }
  }

  checkPasted = (e: ClipboardEvent, cb: Function) => {
    e.clipboardData && e.clipboardData.items.length > 0
      ? this.transformImages(e.clipboardData, cb)
      : this.props.onError(`Sorry, to bother you but there was no image pasted.`)
  }

  pushImage = (source: string) =>
    this.setState(({ images }: GluejarState) => ({ images: [...images, source] }))

  componentDidMount() {
    const elm: Element = this.getContainer()
    elm.addEventListener('paste', this.pasteHandler)
  }

  componentDidUpdate() {
    this.props.onPaste(this.state)
  }

  componentWillUnmount() {
    const elm: HTMLElement = this.getContainer()
    elm.removeEventListener('paste', this.pasteHandler)
  }

  render() {
    const { images } = this.state
    const { children } = this.props
    return children ? children({ images }) : null
  }
}
