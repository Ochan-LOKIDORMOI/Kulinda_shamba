# **🌱Kulinda Shamba: Wildlife Detection System for Farm Protection**

![Image](https://github.com/user-attachments/assets/e6e0e585-4185-49f3-82c6-297103f0729c) 

## **Project Overview:**

The Kulinda Shamba system, which translates from Swahili as **"Protect the Farm,"** is a smart Wildlife intrusion detection system developed to mitigate human Wildlife conflict affecting smallholder farmers in Kenya. 
This initiative uses transfer learning and image classification to detect specific animals elephants, monkeys, and buffaloes that are responsible for frequent crop damage in regions bordering protected wildlife reserves such as the Maasai Mara.

- The goal is to equip small farms with affordable, intelligent monitoring systems that can:

- Detect wildlife intrusions in real-time using Convolutional Neural Networks (CNN),

- Notify farmers via SMS or mobile alerts,

- Trigger non-lethal deterrents like LED flashers or buzzing sounds.

This system is built for low-bandwidth and off-grid rural environments, enabling communities to improve food security while promoting peaceful human-wildlife coexistence.

[VIDEO DEMO:]() 

[FIGMA DESIGN](https://www.figma.com/design/K6ZSBAHsGH6skLbp1GaNKn/Kulinda-Shamba?node-id=0-1&p=f&t=baEVnncDcfRDpecO-0)



### 📁 Project Structure

```
kulinda-web/
├── app.py
├── static/
│   ├── style.css
│   ├── script.js
│   └── assets/
│       ├── graphs/
│       └── images/
├── templates/
│   ├── about.html
│   ├── base.html
│   ├── graphs.html
│   ├── index.html
│   ├── testimonies.html
├── notebook/
│   └── Kulinda_Shamba_Model_Notebook.ipynb
├── model/
│   └── Kulinda2_model.h5
├── logs.csv
├── README.md
└── requirements.txt
```
### 📷 Screenshots of the   Web interfaces

![Image](https://github.com/user-attachments/assets/f7cf7a9a-4e57-402c-bfab-1c14ac2c89bb) 
![Image](https://github.com/user-attachments/assets/a24ec07d-76ce-43b8-9b5f-93d8b0de137a)

## 🧰 Setup Instructions

### ⚙️ Environment Setup

[Download kulinda2_model.h5 here](https://drive.google.com/drive/folders/13p9u6Y_oKs8jNbowexg8RLTbVE11zqCz)

**1. Clone the Repository:**

`git clone https://github.com/Ochan-LOKIDORMOI/Kulinda_shamba.git
cd kulinda-shamba`

**2. Create a virtual environment:**

`python -m venv shamba`

`shamba\Scripts\activate `

**3. Install requirements:**

`pip install -r requirements.txt`

**4. Start the Flask Server:**

`python app.py`

**Note:** Ensure your Python version is 3.10 or lower. TensorFlow does not support 3.11+ as of now.




### 🧱 Deployment Plan

| Module            | Tech Stack            | Status    |
| ----------------- | --------------------- | --------- |
| ✅ Model           | TensorFlow (.h5)      | ✔️ Done   |
| ✅ UI              | HTML/CSS/JS (Flask)   | ✔️ Done   |
| 🔄 MongoDB        | pymongo, cloud-hosted | 🔧 inprogress  |
| 🔄 SMS Alert      | Twilio / API          | 🔧 Inprogress   |
| 🔄 Hosting        | Render / Railway      | 🔧 DIn progress |
| 🔄 Logging System | MongoDB + CSV         | 🔧 Inprogress |

## **Contributor:**

*Ochan Denmark LOKIDORMOI*
## **Email:** o.lokidormo@alustudent.com
