$(document).ready(function() {

  jQuery.validator.addMethod("lettersonly", function (value, element) {
    return this.optional(element) || /^[a-z]+$/i.test(value);
  }, "Please enter only letters."); 

  jQuery.validator.addMethod("noSpace", function (value, element) {
    return value == '' || value.trim().length != 0;
  }, "No space please and don't leave it empty.");

  $.validator.addMethod("custom_email", function (value, element) {
    return this.optional(element) || /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/i.test(value);
  }, "Please enter a valid email address.");


  jQuery.validator.addMethod("letterswithspace", function (value, element) {
    return this.optional(element) || /^[a-z][a-z\s]*$/i.test(value);
  }, "Please enter only letters.");

   $("#register_form, #login_form").validate({
        rules: {
            name:{
              required:true,
              letterswithspace:true
            },
            first_name:{
              required:true,
              letterswithspace:true
              
            },
            
            last_name:{
              required:true,
              lettersonly:true,
              noSpace: true
            },
            email: {
                required: true,
                custom_email: true
            },
            confirm_password: {
                required:true,
                equalTo:"#passw"
            },
            avatar:{
              required:true
            },
            password: {
                required:true,
                rangelength:[4,20]
            }
	         
        },
        messages: {
            name: {
               required: "Please enter your name."
               
            },
            first_name: {
               required: "Please enter your first name."
               
            },
            last_name: {
               required: "Please enter your last name."
               
            },
            email: {
              required: "Please enter an email address.",
              email : "Please enter a valid email address."
            },
            
            confirm_password: {
                required: "Please confirm your password."
                
            },
            avatar:{
              required:"Please select your profile image."
            },

            password: {
                required: "Please enter your password.",
                rangelength: "Please enter alteast 4 charactors."
                
            },
            
        },
    });
});
