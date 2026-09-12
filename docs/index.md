# Project Documentation

This project explores healthy life expectancy using the 2020 World Happiness dataset while demonstrating a professional Python data analytics workflow.

## Custom Analysis

For my custom analysis, I changed the CSV pipeline from summarizing the overall Ladder score to summarizing Healthy life expectancy.

The analysis processed 153 countries. Healthy life expectancy ranged from about 45.2 years to 76.8 years, with an average of about 64.45 years.

I observed a large difference between the lowest and highest values. This suggests that healthy lifespan varies substantially across countries and provides another way to compare quality-of-life conditions beyond the overall happiness score.

## Project Workflow

The project follows an Extract / Transform / Verify / Load workflow:

- Extract data from the source file
- Transform the selected values into descriptive statistics
- Verify the results
- Load the verified results into a processed output file

## What This Project Demonstrates

This project demonstrates my ability to work with multiple data file types in Python and apply a consistent ETL process to each one.

The project includes:

- CSV data analysis using descriptive statistics
- JSON data grouped by category
- Excel text analysis
- Plain-text file analysis
- Verification of results before output
- Git and GitHub version control
- Automated checks and hosted project documentation

## Documentation Index

- **Home** - this landing page
- [**Project Instructions**](./project-instructions.md)
- [**Concepts**](./concepts.md)
- [**Data Card**](./data-card.md)
- [**API**](./api.md)

## Initial Results

The project processes four different types of raw data
and writes the results to **data/processed/**.
Each pipeline follows the
**Extract / Transform / Verify / Load** structure.

- **CSV** - reads the world happiness CSV file,
  extracts the selected numeric column,
  calculates descriptive statistics,
  verifies the results,
  and writes the statistics to a text file.
  (TODO: link or disply results).

- **JSON** - reads the astronauts JSON file,
  extracts the list of people,
  counts people by spacecraft,
  verifies the results,
  and writes the counts to a text file.
  (TODO: link or disply results).

- **XLSX** - reads the feedback Excel file,
  extracts text from the selected column,
  counts occurrences of the selected word,
  verifies the result,
  and writes the count to a text file.
  (TODO: link or disply results).

- **TXT** - reads the Romeo and Juliet text file,
  counts its lines, words, and characters,
  verifies the results,
  and writes the summary to a text file.
  (TODO: link or disply results).
