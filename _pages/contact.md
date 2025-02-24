---
layout: page
title: Contact Me
permalink: /contact/
---

## Reach Out

Feel free to send me a message, and I'll get back to you as soon as possible.

<br />

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
    /* Align form to the left */
    form {
        width: 100%;
        max-width: 500px;
        padding: 20px;
        background: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }

    label {
        font-weight: bold;
        display: block;
        margin: 10px 0 5px;
    }

    input, textarea {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        transition: all 0.3s ease-in-out;
    }

    input:focus, textarea:focus {
        border-color: #007bff;
        outline: none;
        box-shadow: 0px 0px 8px rgba(0, 123, 255, 0.2);
    }

    textarea {
        height: 150px;
        resize: vertical;
    }

    button {
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

    button:hover {
        background: #0056b3;
    }
</style>

<form action="https://formspree.io/f/XYZ_123" method="POST">
    <!-- <label for="name">Name</label> -->
    <input type="text" id="name" name="name" placeholder="First Name and Last" required>
    
    <!-- <label for="email">Email</label> -->
    <input type="email" id="email" name="email" placeholder="you@example.com" required>
    
    <!-- <label for="message">Message</label> -->
    <textarea id="message" name="message" placeholder="Write your message here..." required></textarea>
    
    <button type="submit">Send Message</button>
</form>

<br />