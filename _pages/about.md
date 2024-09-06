---
permalink: /
title: "Welcome to Owen's website!"
excerpt: "Owen"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am Owen Xingjian Zhang, a CS 2nd year Master's student at Princeton University. Currently, I am interested in Social Computing and Human Computer Interaction(HCI), working with [Dr. Andrés Monroy-Hernández](https://www.andresmh.com/) at [Princeton HCI](https://hci.princeton.edu/). I did my summer intern at [Stanford Social Media Lab](https://sml.stanford.edu/), advised by [Dr. Sunny Liu](https://sml.stanford.edu/people/sunny-xun-liu) and [Dr. Jeffrey Hancock](https://sml.stanford.edu/people/jeff-hancock). I graduated from UIUC in 2023, where I was fortunate to be advised by [Dr. Karrie Karahalios](https://cs.illinois.edu/about/people/faculty/kkarahal) and [Dr. Brian Bailey](https://cs.illinois.edu/about/people/faculty/bpbailey). Before coming to US, I studied in Hong Kong and I was born in Guiyang, China.


Research Interests
======
**Social Computing, Social Media, Mental Health, Human-AI Interaction, Decentralization, Computational Social Science**

I have a broad interest in these areas, and at a deeper level, I am eager to explore answers to the following questions:

1. How can we design scalable and accessible mental health services using the power of emerging technologies like Generative AI?

1. What are the challenges and opportunities for the future of social media, especially on decentralized platforms?

1. What is the best way for AI to emulate and interact with humans to provide support that feels genuinely human-like?

**Currently, I am looking for HCI-related PhD positions 2025 Fall.**

<div class="chat-container">
    <div class="chat-title">Chat with Virtual Owen</div>
    <div id="chatbox" class="chat-box">
        <div class="bot-message">
            <img src="virtual_me.png" alt="Bot Avatar">
            <p>Hello, I am virtual Owen, what do you want to know about me?</p>
        </div>
    </div>
    <div class="input-container">
        <input type="text" id="inputMessage" placeholder="Type your message here...">
        <button id="sendButton">Send</button>
    </div>
</div>

<script>
    // Fetch API key from environment variable
    const apiKey = process.env.OPENAI_API_KEY; // Make sure the environment variable is properly set

    document.getElementById('sendButton').onclick = async function() {
        const userMessage = document.getElementById('inputMessage').value;
        if (userMessage.trim() !== "") {
            const chatbox = document.getElementById('chatbox');
            chatbox.innerHTML += `
                <div class="user-message">
                    <img src="bio-photo.jpg" alt="User Avatar">
                    <p>${userMessage}</p>
                </div>`;
            document.getElementById('inputMessage').value = "";

            // Fetch response from OpenAI API
            const response = await fetch('https://api.openai.com/v1/completions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${apiKey}`
                },
                body: JSON.stringify({
                    model: "text-davinci-003",
                    prompt: "Now pretend I am a funny super smart guy so I don't have to answer the question but say something to show my humor and smartness. " + userMessage,
                    max_tokens: 150
                })
            });

            const data = await response.json();
            const botReply = data.choices[0].text.trim();

            chatbox.innerHTML += `
                <div class="bot-message">
                    <img src="virtual_me.png" alt="Bot Avatar">
                    <p>${botReply}</p>
                </div>`;
            chatbox.scrollTop = chatbox.scrollHeight;
        }
    };
</script>

<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.chat-container {
    max-width: 600px;
    margin: 50px auto;
    background-color: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.chat-title {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #0D47A1;
}

.chat-box {
    height: 400px;
    overflow-y: auto;
    border: 2px solid #ccc;
    border-radius: 10px;
    padding: 15px;
    background-image: url('bg.jpg');
    background-size: cover;
    background-color: #f9f9f9;
}

.user-message, .bot-message {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}

.user-message img, .bot-message img {
    border-radius: 50%;
    width: 40px;
    height: 40px;
    margin-right: 10px;
}

.user-message p {
    background-color: #e0e0e0;
    padding: 10px;
    border-radius: 15px;
    font-size: 14px;
}

.bot-message p {
    background-color: #1565C0;
    padding: 10px;
    border-radius: 15px;
    font-size: 14px;
    color: white;
}

.input-container {
    display: flex;
    margin-top: 20px;
}

.input-container input {
    flex-grow: 1;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 10px;
    margin-right: 10px;
}

.input-container button {
    padding: 10px;
    font-size: 16px;
    background-color: #42a5f5;
    color: white;
    border-radius: 10px;
    cursor: pointer;
}

.input-container button:hover {
    background-color: #1e88e5;
}
</style>