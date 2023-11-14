import Header from "./components/Header";
import Card from "./components/Card";
import { extractCodeData, CodeData } from "./components/CodeData";

export default function Home() {
    const data = extractCodeData("app/code");

    return (
        <div>
            <Header />
            <div className="flex flex-wrap justify-center mx-auto">
                {data.map((codeData) => (
                    <Card
                        key={codeData.id}
                        id={codeData.id}
                        name={codeData.name}
                        code={codeData.code}
                        language={codeData.language}
                        date={codeData.date}
                        difficulty={codeData.difficulty}
                    />
                ))}
            </div>
        </div>
    );
}
