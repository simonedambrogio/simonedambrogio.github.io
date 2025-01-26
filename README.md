This repository is based on [Academic Pages](https://github.com/academicpages/academicpages.github.io), a Github Pages template for academic websites.

## Running locally

To run the website locally:

```bash
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`.

## Adding Publications

To add a new publication:

1. Add your paper's BibTeX entry to `markdown_generator/pubs.bib`
2. Run the Python script to generate the markdown file:
   ```bash
   python3.12 markdown_generator/pubsFromBib.py
   ```
   This will create a new markdown file in the `_publications` directory.
