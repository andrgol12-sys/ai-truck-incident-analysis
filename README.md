# AI Incident Analysis for Truck Damage

## Description

This project demonstrates a multimodal AI workflow for analyzing truck damage from incident photos using the OpenAI API.

The application sends an image of a damaged truck to a multimodal model (`gpt-4o`) and receives a structured JSON response describing:
- damaged vehicle parts;
- visible damage;
- severity level;
- operational risks;
- inspection recommendations.

The project was created as part of a Prompt Engineering and Multimodal AI practice assignment.

---

# Features

- Multimodal image analysis
- OpenAI Vision API integration
- Structured JSON output
- Russian-language response support
- Real logistics business use case
- Python + VS Code workflow

---

# Example Output

```json
{
  "тип_тс": "грузовой автомобиль",
  "зона_повреждения": "передняя часть",
  "поврежденные_элементы": [
    "бампер",
    "решетка радиатора",
    "фара"
  ],
  "видимые_повреждения": [
    "вмятины",
    "царапины",
    "трещины"
  ],
  "степень_повреждения": "средняя",
  "можно_продолжать_движение": "требуется осмотр",
  "риски": [
    "снижение эффективности освещения",
    "возможное повреждение креплений"
  ],
  "описание": "Повреждения передней части грузового автомобиля."
}
```

---

# Project Structure

```text
incident_analysis_project
├── images/
│   └── incident.jpg
├── output/
├── .env
├── .gitignore
├── analyze_incident.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone repository

```bash
git clone <your_repo_url>
```

## 2. Create virtual environment

```bash
python -m venv .venv
```

## 3. Activate environment

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

## 4. Install dependencies

```bash
pip install openai python-dotenv
```

---

# Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

---

# Run Project

```bash
python analyze_incident.py
```

---

# Technologies Used

- Python
- OpenAI API
- GPT-4o Vision
- JSON
- VS Code
- Prompt Engineering

---

# Possible Future Improvements

- Telegram bot integration
- Automatic insurance report generation
- Google Sheets export
- Multiple image analysis
- Confidence score support
- n8n workflow integration

---

# Author

Andrei Golubev (AIGolubev)
