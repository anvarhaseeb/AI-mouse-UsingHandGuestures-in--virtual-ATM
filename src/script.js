 // Get references to the input field and keypad
 const inputField = document.getElementById("input-field");
 const keypad = document.getElementById("keypad");

 // Add click event listeners to all buttons in the keypad
 keypad.querySelectorAll("button").forEach(button => {
   button.addEventListener("click", () => {
     // Get the button's text content
     const buttonText = button.textContent;

     // Handle the button click based on its text content
     switch (buttonText) 
     {
       case "Clear":
         // Clear the input field
         inputField.value = "";
         break;
       case "Enter":
         // Do something with the entered value (e.g. submit a form)
         console.log("Entered value:", inputField.valueAsNumber);
         break;
       default:
         // Add the button's text content to the input field
         inputField.value += buttonText;
         break;
     }
   });
 });
 