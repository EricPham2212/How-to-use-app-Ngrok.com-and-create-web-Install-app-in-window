# How to Use Ngrok and Create a Web App on Windows

## Introduction
This guide provides step-by-step instructions on how to install and use Ngrok to expose your local web server to the internet.

## Prerequisites
Before getting started, ensure you have the following:
- A computer running Windows
- An internet connection

## Installation Steps

1. **Download Ngrok**  
   Visit the official website: [Ngrok Download](https://ngrok.com/) and download the version suitable for Windows.

2. **Extract and Install**  
   - Unzip the downloaded file to a directory of your choice.
   - Open a terminal (Command Prompt or PowerShell) and navigate to the extracted folder.

3. **Authenticate Your Ngrok Account**  
   - Sign up at [Ngrok](https://dashboard.ngrok.com/signup).
   - Retrieve your authentication token from the dashboard.
   - Run the following command in the terminal(ngrok):
     ```sh
     ngrok authtoken [YOUR_AUTH_TOKEN]
     ```
     ![image](https://github.com/user-attachments/assets/a382806f-0220-4ef4-b726-0f72df296d69)

   
4. **Start Ngrok**  
   To expose a local web server, use the following command:
   ```sh
   ngrok http 8000
