---
title: 'm0leCon Beginner CTF 2023'
date: 2023-05-13
permalink: /posts/2023/05/m0leCon Beginner 2023/
---
Online-CTF

![image](https://github.com/user-attachments/assets/5170aeba-2eca-4210-92a7-2c35e78e9c4f)<br>
# m0leconCTF Writeup

![image](https://github.com/user-attachments/assets/42859dc5-7313-4d6a-94b6-cdd06f36bde2)<br>

## Table of Contents

- [1. Sanity_Check-50](#1sanity_check-50)<br>
[2. Unguessable-50](#2unguessable-50)<br>
[3. SecureAscess-50](#3secureascess-50)<br>
[4. The wall](#4the-wall)<br>
[5. Polito Pay 2Win](#5polito-pay-2win)<br>
[6. Politoch(e)tbot](#6-politochtbot)<br>
[7. Strange extension-50](#7-strange-extension-50)<br>
[8. A sky full of 5t4r5](#8-a-sky-full-of-5t4r5)

---

## 1.Sanity_Check-50
- **Challenge**:
- ![image](https://github.com/user-attachments/assets/8a7ebec2-b0fa-4cd7-83c8-d095adfe05d3)
- Find the find in Discord server.
- ![image](https://github.com/user-attachments/assets/3942d337-9b93-4ffd-aa2e-d140dbce8ada)

- **Flag**: `ptm{w3lc0m3_t0_b3g1nner_2021+2}`

## 2. Unguessable-50
- **Challenge**:
- ![image](https://github.com/user-attachments/assets/c8d90da8-dd65-4950-af98-309517ff6ea0)
- View page source, find a directory, copy and paste it on the link.
- ![image](https://github.com/user-attachments/assets/ff8299e7-7c3f-425c-bf47-c50082a17f10)
- ![image](https://github.com/user-attachments/assets/b6f891a5-2752-4527-9388-85f6734322a4)
- **Flag**: `ptm{41w1y5_ch3ck_th3_50urc3_c0d3}`

## 3. SecureAscess-50
- **Challenge**:
- ![image](https://github.com/user-attachments/assets/91845a92-32db-4a1b-806a-c806651397e7)
- Decompile the `.pyc` file using [this tool](https://www.toolnb.com/tools-lang-en/pyc.html).
- ![image](https://github.com/user-attachments/assets/e8b76aa4-03d6-41e8-9b89-8485edeffa7e)

- **Steps**:
  - Use ChatGPT to complete the decompiled code.
  - ![image](https://github.com/user-attachments/assets/daaf375c-905e-4550-967a-f7f841b42e26)

  - Log in as admin to get a token and change it to `nonce_example`.
  - ![image](https://github.com/user-attachments/assets/29da2397-34c4-455e-9c39-6dac00a8b814)

  - Run the Python code to get an access token and try logging in.
  - ![image](https://github.com/user-attachments/assets/249c0686-26ad-47fb-9606-2965dd7eac72)
  - ![image](https://github.com/user-attachments/assets/74dd38f3-6ef9-4907-98b9-f24a9ac62324)
    
- **Flag**: `ptm{m4yb3_7hr_Als_4r3_n0t_th4t_5m4r7}`

## 4. The wall
- **Challenge**:
- ![image](https://github.com/user-attachments/assets/44c63c88-5eda-4842-acd0-f89660cbcd8a)
- Check the `null_wall` file in Ghidra.
- **Steps**:
  - Observe the `notaflahbuffer[19]`, indicating a buffer size.
  - - ![image](https://github.com/user-attachments/assets/fbe54c6f-c06d-457f-871d-53c5a97536b3)
  - Input more than 19 characters.
  - ![image](https://github.com/user-attachments/assets/6c2f256d-2c6f-4dc5-b3d0-f1501766d195)
  - Read the note.
  - ![image](https://github.com/user-attachments/assets/c6710815-dc51-4964-94f6-6f6541c1e0d9)
- **Flag**: `ptm{ju57_4n07h3r_br1ck_1n_7h3_w411}`

## 5. Polito Pay 2Win

- **Challenge**:
- ![image](https://github.com/user-attachments/assets/8b3a9b7d-12b9-40b5-b24c-6c6e067ab406)
- Unzip `game-linux.zip`.
- ![image](https://github.com/user-attachments/assets/ea819da9-4f56-467d-b9c9-19458aaf4a7f)

- **Steps**:
  - Run `main.py`.
  - ![image](https://github.com/user-attachments/assets/1f25396a-1d69-496c-82f5-56f279aa3419)
  - Find something hidden in the `market.py` file.
  - ![image](https://github.com/user-attachments/assets/798c0c52-0a1f-4217-bb68-7c63ea083860)
- **Flag**: `ptm{p4tch1ng_3xecut4bl3s_1s_fun}`

## 6. Politoch(e)tbot

- **Challenge**:
- ![image](https://github.com/user-attachments/assets/d57e478a-d438-4fbb-ac9d-85e037da3e97)
- In the chat, identify the correct encryption.
- **Steps**:
  - Identify the encrypted tokens corresponding to "I'm Bob Masters, gimme the flag!" and "I'm Rob Masters,".
  - ![image](https://github.com/user-attachments/assets/8be36f0f-f22c-4679-b97c-bf5ccf710f48)
  - ![image](https://github.com/user-attachments/assets/40916b86-642d-49ad-8a3b-794a8eb0b9b1)
  - ![image](https://github.com/user-attachments/assets/68cb34c9-37f1-4903-bf67-0190428c9923)
  - ![image](https://github.com/user-attachments/assets/646d5ddf-3871-44ae-ab5e-cb8bab4714eb)
- **Flag**: `ptm{ECB_bl0cks_4re_iNd3p3ndent}`

## 7. Strange extension-50

- **Challenge**:
- ![image](https://github.com/user-attachments/assets/fb507f28-7b28-47ae-a9e2-056b039d2155)
- Use `strings` command and grep for "ptm".
- ![image](https://github.com/user-attachments/assets/aaab4c5e-ab0c-4297-8e8c-67853d45601c)
- **Flag**: `ptm{m4k3_r3tr0_g4m1ng_gr34t_4g41n!!}`

## 8. A sky full of 5t4r5

- **Challenge**:
- ![image](https://github.com/user-attachments/assets/81134918-b615-468d-bfa6-04bf42c75bc0)
- Open the `.png` file and find a symbol.
- ![image](https://github.com/user-attachments/assets/c600e36d-ec6e-4926-ae6c-89ac25d03cd4)
- ![image](https://github.com/user-attachments/assets/cfa5af6a-cfba-4db9-8627-5da2e055a27b)
- **Flag**: `ptm{0n3_h0ur_h3r3_1s_7_d4ys_0n_34rth}`

