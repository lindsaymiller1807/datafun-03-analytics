# datafun-03-analytics

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: working with data files for analytics.

## Lindsay Miller's Data Analytics Project

This project demonstrates my work with Python data analytics using multiple file types, including CSV, JSON, Excel, and text files.

I am using this project to practice the Extract / Transform / Verify / Load process while building my skills with Python, Git, GitHub, and professional project organization.

## Custom Analysis: Healthy Life Expectancy

For my custom analysis, I changed the CSV pipeline from summarizing the overall Ladder score to summarizing Healthy life expectancy in the 2020 World Happiness dataset.

I chose this variable because healthy life expectancy is an important measure of quality of life and gives another way to compare countries beyond an overall happiness score.

The analysis processed 153 countries. Healthy life expectancy ranged from about 45.2 years to 76.8 years, with an average of about 64.45 years.

I observed a large difference between the lowest and highest values. This suggests that expected healthy lifespan varies substantially across countries and can provide useful information about differences in quality-of-life conditions.

## Motivation

Data usually needs some work it can be used.
We may need to read it from a source,
select or change values, check our results,
and save useful information for later.

Common tasks can be standardized into a repeatable workflow.
Defining clear steps makes a data pipeline easy to implement.

## This Project

This project illustrates **ETVL data pipelines** for extracting raw data,
transforming it, verifying results, and loading useful output.

The project processes four different types of raw data:

- **CSV** - summarizes a numeric column from world happiness data
- **JSON** - counts astronauts by spacecraft
- **XLSX** - counts occurrences of a word in feedback text
- **TXT** - summarizes a plain-text document

Although the data and processing differ,
each pipeline follows the same ETVL structure:
**Extract / Transform / Verify / Load**

Review the project code and data-processing workflow.

I adapted the processing pipelines to generate new analytics and explore a custom question using the project data.

## Important Folders and Files

- **data/raw/** - raw input data files
- **data/processed/** - output created by the pipelines
- **docs/** - the project narrative and documentation
- **src/datafun/** - the Python instructions
- **zensical.toml** - update authorship & links

## Common Workflow

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
carefully.

## Challenges

One challenge was making sure the project was fully connected to my own GitHub repository and that GitHub Pages and Actions were configured correctly.

I also had to make sure my code changes were saved before rerunning the project so the updated analysis would appear in the terminal.

Working through these issues helped me become more comfortable with troubleshooting, GitHub, and the project workflow.

## Success

The project runs successfully on my machine and writes output files to `data/processed/`.

Running the project script completes all four pipelines and ends with:

```shell
===================================
END main() - Executed successfully!
===================================
```

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

Open a machine terminal in your `Repos` folder,
change directory (cd) into the new folder,
and run `code .` to open only this project in VS Code:

```shell
git clone https://github.com/lindsaymiller1807/datafun-03-analytics.git

cd datafun-03-analytics
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal**
in the root project folder.
Copy each command, paste into your terminal, and hit ENTER,
to run each command one at a time.

```shell
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made by pre-commit tasks
git add -A
uv run pre-commit run --all-files

# run the module
uv run python -m datafun.app

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress as you work
git add -A
git commit -m "your message here"
# repeat if changes were made (try the UP ARROW)
git add -A
git commit -m "your message here"

git push -u origin main
```

</details>

## Helpful Tips

- Use the **UP ARROW** and **DOWN ARROW** in the terminal
  to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Additional Resources

- [Concepts](docs/concepts.md)
- [Data Card](docs/data-card.md)
- [API Documentation](docs/api.md)
- [Glossary](docs/glossary.md)

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Documentation

- [Documentation](https://lindsaymiller1807.github.io/datafun-03-analytics/)

## Data Card

- [Project Data Card](./docs/data-card.md) - with 4 types of files

## Annotations

- [.annotations/annotations.md](./.annotations/annotations.md)

## Citation

- [CITATION.cff](./CITATION.cff)

## License

This project is licensed under the [MIT License](./LICENSE).
