---
layout: page
title: Contact Me
permalink: /contact/
author_profile: true
---

## Reach Out

Feel free to send me a message, and I'll get back to you as soon as possible.


<!-- <form action="https://formspree.io/f/xeoebqlb" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="email">Your email:</label>
    <input type="email" id="email" name="email" required>
    
    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>
    
    <button type="submit">Send</button>
</form> -->

<style>
    /* Keep the form aligned while allowing the profile to show */
    .contact-container {
        width: 100%;
        max-width: 600px;
        padding: 20px 0;
    }

    .contact-form {
        width: 100%;
        max-width: 500px;
        padding: 20px;
        background: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }

    .contact-form input, 
    .contact-form textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        transition: all 0.3s ease-in-out;
    }

    .contact-form input:focus, 
    .contact-form textarea:focus {
        border-color: #007bff;
        outline: none;
        box-shadow: 0px 0px 8px rgba(0, 123, 255, 0.2);
    }

    .contact-form textarea {
        height: 150px;
        resize: vertical;
    }

    .contact-form button {
        display: block;
        width: 100%;
        padding: 12px;
        background: #007bff;
        color: white;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background 0.3s ease-in-out;
        margin-top: 10px;
    }

    .contact-form button:hover {
        background: #0056b3;
    }
</style>

<div class="contact-container">
    <form class="contact-form" action="https://formspree.io/f/xeoebqlb" method="POST">
        <input type="text" id="name" name="name" placeholder="First Name & Last" required>
        <input type="email" id="email" name="email" placeholder="Email" required>
        <textarea id="message" name="message" placeholder="Write your message here..." required></textarea>
        <button type="submit">Send Message</button>
    </form>
</div>

<br />

<br />