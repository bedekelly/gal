import React from 'react';
import Image from '../Image';

import './ImageList.css';

const ImageList = ({ images }) =>
  <div id="gallery">
    { images.map(image => {
      const [src, preview] = image;
      return <Image key={src} src={src} preview={preview} />
    }) }
  </div>


export default ImageList;
