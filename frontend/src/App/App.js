import React from 'react';

import ImageList from '../ImageList';
import getImageData from '../helpers/imageData';

import './App.css';


class App extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = { images: getImageData() }
  }
  
  render() {
    return <ImageList images={this.state.images} />
  }
}


export default App;