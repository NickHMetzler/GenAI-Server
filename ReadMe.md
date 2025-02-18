# GenAI Server

GenAI Server is a lightweight server designed to work alongside your existing web-based AI UI, allowing for remote access and sharing. Run it on your home PC and extend access to your AI tools seamlessly.

---

## 🚀 Prerequisites

### **1. Python 3.11**  
- If you do not have it installed, [download it here](https://www.python.org/downloads/).  
- During installation, make sure to check **"Add Python to PATH"**.

### **2. ngrok**  
- Create an account at [ngrok](https://ngrok.com/).  
- Download `ngrok.exe` from [here](https://ngrok.com/downloads/windows?tab=download).  
- Place `ngrok.exe` in a folder of your choosing.

---

## 📥 Installation

### **1. Clone or Download the Repository**
```sh
git clone https://github.com/your-repo/GenAI-Server.git
cd GenAI-Server
```

### **2. Add ngrok.exe to PATH**
- Follow [this guide](https://www.youtube.com/watch?v=ow2jROvxyH4) to add ngrok to your system PATH.

### **3. Set Up ngrok Authentication**
- Visit the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) and copy your **Authtoken**.
- Open Command Prompt as **Administrator** and run:
  ```sh
  ngrok config add-authtoken YOUR_AUTHTOKEN
  ```
  *(Replace `YOUR_AUTHTOKEN` with your actual token.)*

### **4. Install Dependencies**
- Navigate to the **GenAI Server** folder:
  ```sh
  cd path/to/GenAI-Server
  ```
- Install required packages:
  ```sh
  python -m pip install -r global_requirements.txt
  ```

### **5. Configure Environment Variables**
- Rename `dotenv` to `.env`.
- Edit `.env` to add the correct names and local URLs.
- You can add or remove entries as needed.

---

## 🎯 Usage

### **1. Start Your Web-Based AI UI**
Ensure your AI interface is running before launching GenAI Server.

### **2. Run the Server**
Run the following command:
```sh
python app.py
```

### **3. Share Your Server Address**
Once running, the server will display an address you can share for remote access.

---

## 🛠️ Troubleshooting
- If `ngrok` doesn’t work, ensure it is correctly added to your system PATH.
- Double-check that your `.env` file has the correct local URLs.
- Run `python -m pip install --upgrade pip setuptools wheel` if dependency issues arise.

---

## 📜 License
This project is open-source. Feel free to modify and contribute!

---

### 🔗 Useful Links
- [Python 3.11 Download](https://www.python.org/downloads/)
- [ngrok Download](https://ngrok.com/downloads/windows?tab=download)
- [How to Add to PATH (YouTube)](https://www.youtube.com/watch?v=ow2jROvxyH4)
- [ngrok Authtoken Setup](https://dashboard.ngrok.com/get-started/your-authtoken)

---

Enjoy using **GenAI Server**! 🚀

