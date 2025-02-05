
# Spatio-Temporal Patterns of New York City Taxi Usage


Analyze and visualize spatio-temporal patterns of New York City taxi usage using Python and data science techniques.

## Introduction
This project explores the spatial and temporal behavior of New York City residents through their taxi usage patterns. By examining cab usage data, we uncover how patterns change throughout the year, week, and day, with a focus on differences between weekdays and weekends.

**Keywords**: data analysis, visualization, spatio-temporal patterns, New York City, taxi data, Python, pandas, matplotlib, scikit-learn

## Key Technical Details
- Data Preprocessing Techniques:
  - Outlier removal using percentile-based filtering
  - Coordinate transformation
  - Trip duration normalization
- Analysis Methods:
  - Geospatial coordinate conversion
  - Temporal pattern extraction
  - Statistical analysis of taxi trips
 
### Additional Dependencies
- numpy
- pandas
- matplotlib
- scikit-learn
- scipy

## User Instructions

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/ajaychary06/Projects.git
   cd Projects/Big-Data-Analysis/final-project.ipnyb
   ```
2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

### Usage
1. Ensure you have the necessary data files in the `data` directory.
2. Open and run the Jupyter notebook `final-project.ipynb`:
   ```
   jupyter notebook final-project.ipynb
   ```
3. Follow the notebook cells to explore the analysis and visualizations.

## Developer Instructions

### Building and Modifying the Project
1. Fork the repository on GitHub.
2. Clone your forked repository:
   ```
   git clone https://github.com/yourusername/nyc-taxi-patterns.git
   ```
3. Create a new branch for your changes:
   ```
   git checkout -b feature/your-new-feature
   ```
4. Make your changes and commit them:
   ```
   git add .
   git commit -m "Add your descriptive commit message"
   ```
5. Push your changes to your fork:
   ```
   git push origin feature/your-new-feature
   ```
6. Create a pull request on the original repository.

## Methodology Highlights
- Coordinate conversion using median latitude/longitude
- Distance calculations in kilometers
- Filtering extreme data points
- Visualization of trip distributions


## Expectations
- The project requires Python 3.7+ and Jupyter Notebook.
- Large datasets may require significant computational resources.
- Visualizations and analyses may vary based on the specific dataset used.

## Research Insights
- Explored spatial distribution of taxi pickups/dropoffs
- Analyzed trip duration patterns
- Investigated temporal variations in taxi usage

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ajaychary06/Projects/blob/main/LICENSE) file for details.


## Contact

Your Name - [Ajaychary Kandukuri](https://www.linkedin.com/in/ajaychary-kandukuri-053a5a25a) - ajaycharykandukuri0629@gmail.com
