import { Component } from "react";

const name = "George";
const displayMessage = () => {
  return <h1> Messages</h1>
};

class Message extends Component {
  render() {
    return (
      <div>
        <h1> Message : {this.props.messagecode}</h1>
        {/* <h1>Message Code</h1> */}
      </div>
    )
  }
}

export default Message;
