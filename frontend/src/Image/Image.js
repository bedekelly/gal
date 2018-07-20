import React from 'react';

import './Image.css';


class Image extends React.Component {
  constructor(props) {
    super(props);
    this.srcUrl = `image/${this.props.src}`;
    this.state = { loaded: false };
    this.loaded = this.loaded.bind(this);
  }
  
  loaded() {
    this.setState({ loaded: true });
  }
  
  render() {
    const imgHidden = this.state.loaded ? "shown" : "hidden";
    return <div className="image-wrapper">
      <img src={this.props.preview} alt=""/>
      <img src={this.srcUrl} className={imgHidden} onLoad={this.loaded}/>
    </div>
  }
}


export default Image;