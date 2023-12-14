import fs from "fs";
import path from "path";

export class CodeData {
    constructor(
        id: number,
        name: string,
        code: string,
        language: string,
        difficulty: string
    ) {
        this.id = id;
        this.name = name;
        this.code = code;
        this.language = language;
        this.difficulty = difficulty;
    }
    id: number;
    name: string;
    code: string;
    language: string;
    difficulty: string;
}

export function extractCodeData(directory: string): CodeData[] {
    const codeDataList: CodeData[] = [];
    const difficulties = fs.readdirSync(process.cwd() + directory);

    difficulties.forEach((difficulty) => {
        const difficultyPath = path.join(directory, difficulty);
        const files = fs.readdirSync(difficultyPath);

        files.forEach((file) => {
            const filePath = path.join(difficultyPath, file);

            var codeData = new CodeData(0, "", "", "", "");

            if (path.extname(filePath) === ".py") {
                const content = fs.readFileSync(filePath, "utf-8");
                const [id, name] = path
                    .basename(filePath)
                    .match(/(\d+)_(.+)\.(\w+)/)!
                    .slice(1);

                const code = content;

                codeData = new CodeData(
                    parseInt(id),
                    name,
                    code,
                    "Python",
                    difficulty
                );
            } else if (path.extname(filePath) === ".js") {
                const content = fs.readFileSync(filePath, "utf-8");
                const [id, name] = path
                    .basename(filePath)
                    .match(/(\d+)_(.+)\.(\w+)/)!
                    .slice(1);

                const code = content;

                codeData = new CodeData(
                    parseInt(id),
                    name,
                    code,
                    "JavaScript",
                    difficulty
                );
            }
            codeDataList.push(codeData);
        });
    });

    codeDataList.sort((a, b) => a.id - b.id);

    return codeDataList;
}
