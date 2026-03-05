# RaknaTech Certificate Generator 🏆

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-pandas%20%7C%20pillow-orange.svg)

A lightweight, automated desktop application built to streamline the creation of bulk certificates. Designed for event organizers and institutions, this tool reads participant data from a CSV file, automatically maps corresponding profile photos, and renders crisp, high-fidelity text onto a custom certificate template.

---

## 🚀 Features

* **Automated Batch Processing:** Generate hundreds of certificates in seconds.
* **Dynamic Image Mapping:** Automatically detects and resizes athlete/participant photos (`.jpg`, `.jpeg`, `.png`) based on serial numbers.
* **Precision Typography:** Utilizes direct TrueType font (`.ttf`) rendering for professional-grade text overlays.
* **User-Friendly Interface:** A clean, intuitive graphical user interface (GUI) built with Tkinter—no coding required for the end-user.
* **Failsafe Logic:** Includes error handling for missing photos, missing fonts, and missing data files.

---

## 📋 Prerequisites

To run this application from the source code, you will need **Python 3.x** installed on your machine.

Install the required dependencies using pip:

```bash
pip install pandas Pillow
```
## 📂 Project Structure

For the application to run successfully, your project directory must follow this exact structure:

```text
rakna-certificate-generator/
│
├── Completed_Certificates/    # Generated certificates are saved here
├── Photos/                    # Place participant photos here (e.g., photo1.jpg)
├── main.py                    # The core application script
├── athletes.csv               # The data source file
├── template.jpg               # Your blank high-res certificate template
├── ARIAL.TTF                  # Required font file
├── requirements.txt           # Dependency list
└── README.md                  # Project documentation

```

### Data Formatting (`athletes.csv`)
Ensure your CSV contains the following exact column headers to prevent key errors during generation: 
`slno`, `name`, `represented`, `snatch`, `clean_jerk`, `total`, `dob`, `category`, `position`

---

## 💻 Usage Instructions

1. **Prepare your template:** Ensure `template.jpg` is placed in the root folder.
2. **Add the font:** Place your `ARIAL.TTF` font file in the root folder.
3. **Load the data:** Fill out `athletes.csv` with the participant information.
4. **Load the photos:** Drop participant photos into the `Photos/` directory. Name them according to their Serial Number (e.g., `photo1.jpg` for `slno` 1).
5. **Run the app:**
   ```bash
   python main.py
6.**Generate: Click the "Generate Certificates" button in the pop-up window.**
7.**Retrieve: Find your perfectly formatted certificates in the Completed_Certificates/ folder!**

---
**👨‍💻 Author**
RAKNA | RaknaTech

Automating recognition, pixel by pixel.
