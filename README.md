# ASX Real-Time Analytics Dashboard

A comprehensive Australian Stock Exchange (ASX) analytics platform featuring real-time stock data, economic indicators, and interactive visualizations.

## 🚀 Features

- **Real-time ASX Stock Data**: Live price feeds for ASX 200 companies
- **Economic Indicators**: RBA cash rate, inflation, unemployment, GDP data
- **Interactive Charts**: Real-time price charts with technical indicators
- **WebSocket Streaming**: Live data updates without page refresh
- **Security**: API key authentication for premium features

## 🏗️ Architecture

### Backend (Python/FastAPI)
- **FastAPI** for high-performance async API
- **WebSocket** connections for real-time data
- **Redis** for caching and pub/sub messaging

### Frontend (React)
- **React 18** with modern hooks
- **Recharts** for interactive data visualization
- **Tailwind CSS** for responsive design

## 🛠️ Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Redis (optional, will use mock data if unavailable)

### 1. Backend Setup
```bash
cd backend
pip install -r ../requirements.txt
python main.py
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm start
```

### 3. Access
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📄 License

This project is licensed under the MIT License.

---

**Built for the Australian financial sector** 🇦🇺