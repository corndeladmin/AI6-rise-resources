# AI6-rise-resources

A Node.js tool for generating syntax-highlighted HTML code snippets for use in RISE modules.

## How It Works

- Place formatted code files in `src/snippets/` (group by language).
- On build each file is converted to a standalone, syntax-highlighted (based on language) HTML snippet using Handlebars and [Highlight.js](https://highlightjs.org/).
- On build output is written to the `public/` directory, including an `index.html` and an `iframes.html` with ready-to-copy iframe tags.

## Contributing Snippets

_Do not delete existing snippets unless 100% sure as they are used in live modules._

1. **Create a branch** for your snippets.
2. **Add your code snippets** to `src/snippets/` (create a subfolder for your language if not already present).

- To view locally run `npm run build` to generate `public`.

3. **Open a Pull Request** to `main`.

On merge, a **GitHub Action** will:

- Build the HTML output.
- Deploy the `public/` directory to the `gh-pages` branch.
  - If broken and as a last resort there is a manual deploy script `npm run build`

Your snippets will then be available online for embedding in RISE modules.

## Project Structure

```
src/
  module-projects   # Store Specific Projects Related to Modules 
  snippets/         # Add your code files here
  templates/        # Handlebars templates
  utils/            # Build utilities
  index.js          # Main script for processing snippets
public/             # Generated HTML output (auto-deployed)
```

## Local Development

```sh
npm install
npm run build
```

## Testing

This project uses Vitest (https://vitest.dev/) for testing. To run tests:

```sh
npm test
```

## module-projects

This is a folder to keep any module specific source code that is not large enough to be its own repository.

---