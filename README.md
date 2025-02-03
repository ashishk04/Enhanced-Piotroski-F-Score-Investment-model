# Enhanced-Piotroski-F-Score-Investment-model

## Project Overview
This project builds upon the classic Piotroski F-Score model, enhancing it with additional parameters to better evaluate both long-term and short-term investment opportunities. By leveraging financial ratios and scores, the model ranks stocks based on their potential for high returns, providing insights for both beginner and advanced investors.


## Key Features:
1. Piotroski F-Score Calculation:

- Segmented into three categories:
  - Profitability Ratios (4 scores)
  - Efficiency Measures (2 scores)
  - Capital Structure Metrics (3 scores)
  - High growth score (4)
    
- Each category is analyzed in its own file, allowing independent examination of specific metrics.
  
2. Enhanced Features:

- Integrated additional metrics such as Quick Ratio and Sales Growth to optimize short-term investment identification.
- Developed a separate High Growth Stock Strategy, incorporating factors like:
  - Earnings Per Share (EPS)
  - PEG Ratio
  - Return on Equity (ROE)
  - Sales Growth Ratio
    
3. Data Extraction:

- Utilized the yFinance library to fetch real-time and historical financial data.
  
4. Scoring System:

- The model calculates cumulative F-Scores, typically ranging between 0 and 9.
- Companies with scores of 8 or 9 are considered strong candidates for long-term investment.
- For short-term growth, additional financial ratios and trends are evaluated.
  
## File Structure

1. Profitability Ratios: Contains calculations for four profitability metrics contributing to the Piotroski F-Score.
2. Efficiency Ratios: Focuses on the analysis of two efficiency measures, providing insights into operational effectiveness.
3 Capital Structure Metrics: Evaluates three metrics related to financial stability and leverage.
4.High Growth Stock Strategy: A separate file dedicated to analyzing high-growth companies using expanded metrics.

## Usage

1 Input Data:
- Stock data is fetched directly using the yFinance library.
- Balance sheet and income statement data are processed to compute relevant financial ratios.
  
2. Analysis:
- Use the individual files to analyze specific categories of the Piotroski F-Score.
- Refer to the High Growth Stock Strategy file for short-term investment evaluations.
  
3. Investment Decision:
- Combine scores to assess the overall strength of a stock.
- Long-term investments are recommended for companies scoring 8–9 on the Piotroski F-Score.
- Short-term opportunities are highlighted based on additional growth metrics.
  
## Benefits
- For Beginners: A simple and effective strategy to identify strong investment opportunities.
- For Advanced Users: Customizable scoring to adapt to different financial scenarios.
  
### This project aims to empower investors by providing a robust tool to evaluate stocks based on financial health and growth potential. Feel free to experiment with the provided code and adapt it to your investment strategy.
