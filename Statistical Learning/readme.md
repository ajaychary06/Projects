
# Car Seat Sales Predictive Analysis

A statistical learning project analyzing car seat sales data using multiple regression models to predict sales performance and identify key market factors.

## Overview

This project implements predictive analysis on car seat sales data using various statistical learning methods including Linear Regression, Random Forest, and Decision Trees. The analysis focuses on understanding sales patterns and predicting unit sales based on various market factors.

**Keywords**: Statistical Learning, R Programming, Predictive Analytics, Sales Analysis, Machine Learning, Data Science

## Key Features

- Comprehensive exploratory data analysis
- Multiple regression models implementation
- Feature engineering and transformation
- Cross-validation and model comparison
- Visualization of results
- Performance metrics evaluation

## Installation

### Prerequisites
- R (version 4.0 or higher)
- RStudio (recommended)

### Required R Packages
```R
install.packages(c(
    "ISLR",
    "ggplot2",
    "caret",
    "randomForest",
    "rpart",
    "rpart.plot",
    "gridExtra"
))
```

## Usage

1. Clone the repository:
```bash
git clone https://github.com/ajaychary06/Projects.git
cd Projects/Statistical-Learning/Ajaychary-final-project.Rmd

```

2. Open the R project in RStudio

3. Run the analysis:
   - Open `final_project.Rmd`
   - Click "Knit" to generate the complete analysis report
   - Or run individual chunks to explore specific sections

## Developer Instructions

### Project Structure
```
├── README.md
├── final_project.Rmd
├── data/
│   └── Carseats.csv
├── outputs/
│   └── figures/
└── .gitignore
```

### Building the Project

1. Fork the repository
2. Create a new branch for your features
3. Make your changes
4. Run all code chunks to ensure reproducibility
5. Submit a pull request

### Code Style
- Follow tidyverse style guide
- Document all functions
- Include comments for complex operations
- Use meaningful variable names

## Expectations

The analysis should:
- Load and preprocess the Carseats dataset
- Perform exploratory data analysis
- Implement multiple regression models
- Compare model performances
- Generate visualizations
- Produce interpretable results

## Results

The analysis revealed that:
- Random Forest model performed best with highest accuracy
- Price and advertising budget significantly impact sales
- Shelf location quality influences purchase decisions
- Cross-validation improved model reliability


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ajaychary06/Projects/blob/main/LICENSE) file for details.


## Contact

Your Name - [Ajaychary Kandukuri](https://www.linkedin.com/in/ajaychary-kandukuri-053a5a25a) - ajaycharykandukuri0629@gmail.com
