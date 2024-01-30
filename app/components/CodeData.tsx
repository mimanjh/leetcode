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

export function extractCodeData(): CodeData[] {
    const codeDataList: CodeData[] = [];
    const dir = path.resolve("./public", "code");
    const difficulties = fs.readdirSync(dir);

    difficulties.forEach((difficulty) => {
        const difficultyPath = path.join(dir, difficulty);
        const files = fs.readdirSync(difficultyPath);

        files.forEach((file) => {
            const filePath = path.join(difficultyPath, file);

            var codeData = new CodeData(0, "", "", "", "");

            var language = "";
            if (path.extname(filePath) === ".py") {
                language = "Python";
            } else if (path.extname(filePath) === ".js") {
                language = "JavaScript";
            }
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
                language,
                difficulty
            );

            codeDataList.push(codeData);
        });
    });

    codeDataList.sort((a, b) => a.id - b.id);

    return codeDataList;
}
