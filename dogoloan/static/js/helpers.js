// This code is executed when the document (HTML) is fully loaded and ready
$(document).ready(function () {
    // Select the input fields for password and confirm password
    const passwordField = $("#password");
    const confirmPasswordField = $("#password2");
    const messageElement = $("#registrationMessage");
  
    // Function to update the password matching status message
    function updatePasswordMatchingStatus() {
      // Get the values of the password and confirm password fields
      const password = passwordField.val();
      const confirmPassword = confirmPasswordField.val();
  
      // If either password field is empty, do not display any message
      if (password === "" || confirmPassword === "") {
        messageElement.text("");
      } else if (password === confirmPassword) {
        // If passwords match, show success message with call-out effect
        messageElement
          .text("Passwords match")
          .removeClass("alert-danger") // Remove any error class if present
          .addClass("alert alert-success alert-dismissible") // Apply success class with call-out styles
          .fadeIn(400) // Fade in the message with a duration of 400 milliseconds
          .animate({ top: "0", scale: "1" }, 200); // Animate the message position and scale
      } else {
        // If passwords do not match, show error message with fade-in animation
        messageElement
          .text("Passwords do not match")
          .removeClass("alert-success") // Remove any success class if present
          .addClass("alert alert-danger alert-dismissible") // Apply error class with fade-in styles
          .hide() // Hide the message initially
          .fadeIn(1000, "linear"); // Fade in the message with a duration of 1000 milliseconds using linear easing
      }
    }
  
    // Listen for input changes in password and confirm password fields
    // When the user types in the fields, call the updatePasswordMatchingStatus() function to check if passwords match
    passwordField.on("input", updatePasswordMatchingStatus);
    confirmPasswordField.on("input", updatePasswordMatchingStatus);
  
    // Handle form submission using AJAX
    $("#msform").on("submit", function (event) {
      event.preventDefault(); // Prevent the default form submission behavior
  
      // Perform an AJAX POST request to the server with the form data
      $.ajax({
        type: "POST", // HTTP method of the request
        url: "{% url 'users:register' %}", // URL to send the request to (provided by Django template)
        data: $(this).serialize(), // Serialize the form data and send it in the request
        success: function (response) {
          // If the request is successful, handle the response from the server
          if (response.error) {
            // If there's an error message in the response, display it in red
            $("#registrationMessage").text(response.error).css("color", "red");
          } else if (response.success) {
            // If there's a success message in the response, display it in green
            $("#registrationMessage").text(response.success).css("color", "green");
          }
        },
        error: function (xhr, data) {
          // If there's an error with the AJAX request, log it in the console and display a general error message in red
          console.log(data);
          $("#registrationMessage")
            .text("An error occurred. Please try again." + ": " + xhr)
            .css("color", "red");
        },
      });
    });
  });
  