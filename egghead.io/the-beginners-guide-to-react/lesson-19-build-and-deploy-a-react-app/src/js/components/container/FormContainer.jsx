import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import Input from '../presentational/Input.jsx';


class FormContainer extends Component {
  constructor(props) {
    super(props);

    this.state = { title: '' };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    const { id, value } = event.target;
    this.setState({ [id]: value });
  }

  render() {
    const { title } = this.state;
    return (
      <form id="article-form">
        <Input 
          text="Title"
          label="title"
          type="text"
          id="title"
          value={title}
          handleChange={this.handleChange}
        />
      </form>
    );
  }
}

export default FormContainer;

const wrapper = document.getElementById('create-article-form');
wrapper ? ReactDOM.render(<FormContainer />, wrapper) : false;
