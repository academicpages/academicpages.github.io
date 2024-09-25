<?php
 /**
  * Requires the "PHP Email Form" library
  * The "PHP Email Form" library is available only in the pro version of the template
  * The library should be uploaded to: vendor/php-email-form/php-email-form.php
  * For more info and help: https://bootstrapmade.com/php-email-form/
  */

// Replace contact@example.com with your real receiving email address
$receiving_email_address = 'sierrapomar1001@gmail.com';

// Check if the PHP Email Form library exists
if( file_exists($php_email_form = '../assets/vendor/php-email-form/php-email-form.php' )) {
    include( $php_email_form );
} else {
    die( 'Unable to load the "PHP Email Form" Library!');
}

// Initialize the email form
$contact = new PHP_Email_Form;
$contact->ajax = true;  // Enable AJAX form submission

// Set up the email details
$contact->to = $receiving_email_address;  // Set the receiving email
$contact->from_name = $_POST['name'];  // Sender's name from form
$contact->from_email = $_POST['email'];  // Sender's email from form
$contact->subject = $_POST['subject'];  // Email subject from form

// Uncomment and configure below code if you want to use SMTP to send emails
/*
$contact->smtp = array(
  'host' => 'smtp.yourhost.com',  // Replace with your SMTP host
  'username' => 'yourusername',   // Replace with your SMTP username
  'password' => 'yourpassword',   // Replace with your SMTP password
  'port' => '587'                 // SMTP port (587 is typical for TLS, 465 for SSL)
);
*/

// Add messages to the email
$contact->add_message( $_POST['name'], 'From');
$contact->add_message( $_POST['email'], 'Email');
$contact->add_message( $_POST['message'], 'Message', 10);

// Send the email and output the result
echo $contact->send();
?>
