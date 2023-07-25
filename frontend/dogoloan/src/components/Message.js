import { Component } from "react";

const name = "George";
const displayMessage = () => {
  return <h1> Messages</h1>
};

class Message extends Component {
  render() {
    return (
      <div>
        <h1>Displayed Message</h1>
        {displayMessage()}
      </div>
    )
  }
}

export default Message;
