import { readdirSync } from "fs";
import path from "path";
import DirectoryWriter from "./utils/DirectoryWriter.js";
import Template from "./utils/Template.js";
import SnippetGenerator from "./utils/SnippetGenerator.js";

const codeSnippetTemplate = new Template("snippet.hbs");
const snippetsDirectory = path.join("src", "snippets");
const publicWriter = new DirectoryWriter("public");
const filesCreated = [];
const files = readdirSync(snippetsDirectory);

files.forEach((file) => {
  const snippetGenerator = new SnippetGenerator(
    codeSnippetTemplate,
    file,
    publicWriter
  );
  snippetGenerator.process();
  snippetGenerator.filesRead.forEach((fileRead) => filesCreated.push(fileRead));
});

const summaryTemplateFiles = ["index", "iframes"];

summaryTemplateFiles.forEach((file) => {
  const template = new Template(`${file}.hbs`);
  const populatedTemplate = template.compile({ filesCreated });
  publicWriter.write(`${file}.html`, populatedTemplate);
});
