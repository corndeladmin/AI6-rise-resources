import { writeFileSync, mkdirSync } from "fs";
import path from "path";

class DirectoryWriter {
  directory;

  constructor(directory, root = "") {
    this.directory = path.join(root, directory);
    try {
      mkdirSync(this.directory, { recursive: true });
      console.log(`[DirectoryWriter] Directory exists: ${directory}`);
    } catch (error) {
      console.error(
        `[DirectoryWriter] Failed to create directory "${directory}": ${error.message}`
      );
    }
  }

  write(fileName, fileContents) {
    const filePath = path.join(this.directory, fileName);
    try {
      writeFileSync(filePath, fileContents);
      console.log(`[DirectoryWriter] Wrote file: ${filePath}`);
    } catch (error) {
      console.error(
        `[DirectoryWriter] Failed to write file "${filePath}": ${error.message}`
      );
    }
  }
}

export default DirectoryWriter;
