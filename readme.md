# 🔌 Household Power Consumption Forecasting

This project focuses on forecasting household electricity usage using historical time series data. It leverages a modular, production-ready Python framework for building, training, and deploying a machine learning model to predict **Global Active Power** consumption.

---

## 📈 Project Description

The goal of this project is to build a time series regression model that can forecast the **Global Active Power** usage of a household based on historical readings. The pipeline handles data ingestion, preprocessing, model training, evaluation, and prediction in a clean, maintainable structure. The final model can be deployed via a web interface for real-time prediction.

---

## 🗂️ Dataset

- **Source**: [UCI Machine Learning Repository – Individual household electric power consumption](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption)
- **Time Span**: December 2006 – November 2010
- **Frequency**: 1-minute intervals
- **Records**: Over 2 million
- **Target Variable**: `Global_active_power` (kilowatts)

### 🔢 Features Used

| Column                | Description                                      |
|-----------------------|--------------------------------------------------|
| Date & Time           | Timestamp of measurement                         |
| Global_active_power   | Household power consumption (kW) — **Target**    |
| Global_reactive_power | Reactive power                                   |
| Voltage               | Voltage (V)                                      |
| Global_intensity      | Intensity (A)                                    |
| Sub_metering_1        | Kitchen appliance energy                         |
| Sub_metering_2        | Laundry appliance energy                         |
| Sub_metering_3        | Climate control energy                           |


