import React, { Component } from "react";
import Table from "./Table";

class App extends Component {
  state = {
    advert: [],
    data: "http://127.0.0.1:8000/muzi-muzi/get_adverts?limit=10"
  };

  componentDidMount() {
    const url = this.state.data;
    fetch(url)
      .then(result => result.json())
      .then(result => {
        this.setState({
          advert: result.fields
        });
        console.log(this.state);
      });
  }

  render() {
    const { advert } = this.state;
    return (
      <div>
        <Table adverts={advert} />
      </div>
    );
  }
}

export default App;