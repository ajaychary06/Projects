# Applied Statistics Analysis Project

> Statistical analysis project implementing logistic regression, LASSO regression, and polynomial modeling using R.

## Overview

This project implements various statistical modeling techniques to analyze different datasets including medical data (Downer dataset) and the Boston Housing dataset. The analysis includes logistic regression for medical outcome prediction, LASSO regression for feature selection, and polynomial regression for eruption prediction.

### Key Features
- Logistic regression model for medical outcome prediction
- LASSO regression implementation for Boston Housing dataset
- Polynomial regression analysis for Old Faithful eruption data
- Cross-validation techniques for model evaluation
- Feature importance analysis

## Installation

### Prerequisites
- R (version 4.0 or higher)
- RStudio (recommended)

### Required R Packages
```R
install.packages(c(
    "alr4",
    "dplyr",
    "glmnet",
    "MASS",
    "car",
    "effects"
))
```

## Usage Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/applied-statistics-project.git
```

2. Open the R project in RStudio

3. Install required dependencies:
```R
source("install_dependencies.R")  # If provided
```

4. Run the analysis scripts in the following order:
   - `logistic_regression.R`
   - `lasso_regression.R`
   - `polynomial_regression.R`

## Developer Guide

### Project Structure
```
applied-statistics-project/
├── R/
│   ├── logistic_regression.R
│   ├── lasso_regression.R
│   └── polynomial_regression.R
├── data/
│   ├── Downer.csv
│   └── faithful.csv
└── docs/
    └── analysis_report.pdf
```

### Building the Project
1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

### Development Requirements
- R development tools
- Knowledge of statistical modeling
- Familiarity with R packages: glmnet, MASS, dplyr
- Understanding of cross-validation techniques

## Expectations

### Model Performance
- Logistic Regression: Expected accuracy > 75%
- LASSO Regression: MSE < 22 for Boston Housing predictions
- Polynomial Regression: R-squared > 0.85 for best fit model

### Limitations
- Models are trained on specific datasets and may require retraining for different data
- Cross-validation results may vary with different random seeds
- Computational resources may affect performance with large datasets

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ajaychary06/Projects/blob/main/LICENSE) file for details.


## Contact

Your Name - [Ajaychary Kandukuri](https://www.linkedin.com/in/ajaychary-kandukuri-053a5a25a) - ajaycharykandukuri0629@gmail.com

