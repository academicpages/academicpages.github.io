---
layout: archive
title: Contact Me
permalink: /contact/
author_profile: true
---
{% include base_path %}

## Reach Out

Feel free to send me a message, and I'll get back to you as soon as possible.


<style>
    .contact-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        padding: 10px 0;
    }

    .contact-form {
        width: 100%;
        max-width: 500px;
        padding: 20px;
        background: transparent; /* Remove the white background */
        border-radius: 10px;
        box-shadow: none; /* Optionally remove the shadow */
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
        width: 50%;
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