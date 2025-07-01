# A16-rise-resources

A Node.js tool for generating syntax-highlighted HTML code snippets from source code files using Handlebars templates.

This project reads files from the `src/snippets` directory, processes them into HTML with syntax highlighting, and outputs them to a `public` directory, along with an index page.

## Features

- Reads code snippets from the `src/snippets` directory
- Uses Handlebars templates for HTML generation
- Outputs each snippet as a standalone HTML file in the `public` directory
- Generates an `index.html` listing all generated snippets
- Supports syntax highlighting via https://highlightjs.org/
- Easily extensible for new languages by adding a language folder and corresponding files to the `snippets` directory
- Uses Highlight.js to change the theme change the CSS link in `snippet.hbs` to use a different highlight.js theme: https://cdnjs.com/libraries/highlight.js

## Usage

### 1. Install dependencies

```sh
npm install
```

### 2. Add your code snippets

Place your code files in the `src/snippets` directory. Each file will be processed into an HTML snippet.

### 3. Build the HTML output

```sh
npm run build
```

This will generate HTML files for each snippet in the `public` directory and create an `index.html` page listing them.

### 4. Deploy to GitHub Pages

To publish your generated HTML files to GitHub Pages, use the deploy script:

```sh
npm run deploy
```

This will push the contents of the `public` directory to the `gh-pages` branch of the repository, making your snippets available online to add as a resource to a Rise module.

> **Todo:**  
> This process is manual at the moment, but I’d love to automate it with GitHub Actions when time allows.

## Project Structure

```
src/
  index.js                # Main script for processing snippets
  snippets/               # Place your code files here
  templates/
    snippet.hbs           # Handlebars template for individual snippets
    index.hbs             # Handlebars template for the index page
  utils/
    DirectoryWriter.js    # Handles writing files/directories
    Template.js           # Loads and compiles Handlebars templates
    SnippetGenerator.js   # Processes snippet files into HTML
public/                   # Output directory for generated HTML
```

## Testing

This project uses Vitest (https://vitest.dev/) for testing. To run tests:

```sh
npm test
```
