

function Profile(props) {
    // console.log(props);
    return (
        <h1>
            Name : {props.name} Lastname : {props.lastname}
            {/* {props.children} */}
        </h1>
    )
}

export default Profile;