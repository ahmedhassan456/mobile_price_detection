# Mobile Price Detection Project

## Overview
This project is a machine learning model that predicts the price range of mobile phones based on various features. The model was built using the XGBoost classifier (`XGBClassifier`) and deployed using Streamlit for interactive user input and predictions.

## Table of Contents
1. [Dataset](#dataset)
2. [Model](#model)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Results](#results)
6. [Streamlit Deployment](#streamlit-deployment)
7. [Contributing](#contributing)
8. [License](#license)

## Dataset
The dataset used for this project includes the following features:
- **battery_power**: Battery capacity in mAh
- **blue**: Whether the phone has Bluetooth or not
- **clock_speed**: Speed at which microprocessor executes instructions
- **dual_sim**: Whether the phone has dual SIM support or not
- **fc**: Front Camera megapixels
- **four_g**: Whether the phone has 4G or not
- **int_memory**: Internal memory in GB
- **m_dep**: Mobile depth in cm
- **mobile_wt**: Weight of the mobile phone
- **n_cores**: Number of cores in processor
- **pc**: Primary Camera megapixels
- **px_height**: Pixel Resolution Height
- **px_width**: Pixel Resolution Width
- **ram**: Random Access Memory in MB
- **sc_h**: Screen Height in cm
- **sc_w**: Screen Width in cm
- **talk_time**: Maximum talk time in hours
- **three_g**: Whether the phone has 3G or not
- **touch_screen**: Whether the phone has a touch screen or not
- **wifi**: Whether the phone has WiFi or not

The target variable is `price_range`, which categorizes the price into one of four ranges:
1. Low
2. Medium
3. High
4. Very High

## Model
The model was developed using the XGBoost classifier (`XGBClassifier`), which is known for its efficiency and performance in classification tasks. Key steps in the model development process include:
- Data preprocessing and feature engineering
- Splitting the dataset into training and testing sets
- Training the XGBoost model
- Evaluating the model's performance using accuracy, precision, recall, and F1-score

## Installation
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/mobile-price-detection.git
   cd mobile-price-detection
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```


## Usage
1. **Running the notebook:**
   - Open the `mobile_price_prediction.ipynb` notebook in Jupyter or any compatible environment to see the step-by-step model building process.

2. **Running the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   This will start the web application, where you can input various features of a mobile phone and get the predicted price range.

## Results
The model achieved the following performance metrics on the test set:
- **Accuracy**: 94%
- **Precision**: 95%
- **Recall**: 95%
- **F1-Score**: 94%

## Streamlit Deployment
The model was deployed using Streamlit, a powerful tool for building web applications. The app allows users to interact with the model by providing input features and receiving a predicted price range.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
