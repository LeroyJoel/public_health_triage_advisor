# 🏥 Nigerian Health Triage Advisor

**🚀 HACKATHON PROJECT** - AI-Powered Healthcare Guidance System for Nigeria

A comprehensive CrewAI project that uses 5 specialized AI agents to provide real-time health assessment, triage, and guidance tailored to the Nigerian healthcare system.

## 🎯 **Hackathon Highlights**

- **🤖 Multi-Agent AI System** - 5 specialized agents working collaboratively
- **🏥 Real-time Health Assessment** - Instant symptom analysis and triage
- **📍 Location-Specific Guidance** - Tailored to Nigerian healthcare infrastructure
- **🚨 Emergency Response** - Critical situation detection and immediate action
- **💊 Medicine Availability** - Real-time pricing and availability data
- **💰 Financial Guidance** - Insurance and cost-saving recommendations
- **📱 Interactive Web Interface** - User-friendly Streamlit application
- **🎬 Live Demo Capability** - Perfect for hackathon presentations

## 🏆 **Why This Stands Out**

1. **Real-World Impact** - Addresses actual healthcare challenges in Nigeria
2. **Technical Innovation** - Advanced multi-agent AI architecture
3. **Comprehensive Solution** - Covers triage, maternal health, medicine, and finance
4. **Emergency Ready** - Critical situation detection and response
5. **Scalable Architecture** - Easy to deploy and extend
6. **Interactive Demo** - Judges can actually use the system

## Description

You're a healthcare professional who helps identify symptoms and recommend next steps. You provide initial health assessments and guide people to the appropriate level of medical care they need.

## 🚀 **Quick Start (Hackathon Demo)**

### **Option 1: Interactive Web App**
```bash
# Install dependencies
pip install -e .

# Set your Gemini API key in .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Launch interactive web interface
streamlit run app.py
```

### **Option 2: Command Line Demo**
```bash
# Run the hackathon demo with 3 scenarios
python demo.py
```

### **Option 3: Basic Usage**
```bash
# Run the crew directly
python -m public_health_triage_crew.main
```

## 📋 **Installation Details**

1. Install dependencies:
```bash
pip install -e .
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your GEMINI_API_KEY
```

## Usage

### Run the crew:
```bash
python -m public_health_triage_crew.main
```

### Train the crew:
```bash
python -m public_health_triage_crew.main train <iterations> <filename>
```

### Test the crew:
```bash
python -m public_health_triage_crew.main test <iterations> <eval_llm>
```

## Project Structure

```
public_health_triage_crew/
├── src/
│   └── public_health_triage_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       ├── tools/
│       │   └── custom_tool.py
│       ├── crew.py
│       └── main.py
├── knowledge/
├── tests/
└── pyproject.toml
```

## Agent Details

- **Role**: Public Health Triage Advisor
- **Goal**: Guide people to appropriate medical care
- **Task**: Assess reported symptoms and provide guidance on appropriate next steps for medical care, including urgency levels and recommended healthcare providers.
