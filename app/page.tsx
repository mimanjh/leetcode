import Header from "./components/Header";
import Card from "./components/Card";
import { extractCodeData, CodeData } from "./components/CodeData";
import SearchBar from "./components/SearchBar";

export default function Home({
    searchParams,
}: {
    searchParams: { query?: string };
}) {
    const query = searchParams?.query?.toLowerCase() || "";

    const fetchFilteredData = (codeData: CodeData[], query: string) => {
        const filteredData = codeData.filter((d: CodeData) => {
            return (
                d.name.toLowerCase().includes(query) ||
                d.language.toLowerCase().includes(query) ||
                d.difficulty.toLowerCase().includes(query) ||
                d.id.toString().includes(query)
            );
        });

        return filteredData;
    };
    const data = fetchFilteredData(extractCodeData(), query);

    return (
        <div>
            <Header />
            <SearchBar placeholder="Search" />
            <div className="flex flex-wrap justify-center mx-auto">
                {data.map((codeData: CodeData) => (
                    <Card
                        key={codeData.id}
                        id={codeData.id}
                        name={codeData.name}
                        code={codeData.code}
                        language={codeData.language}
                        difficulty={codeData.difficulty}
                    />
                ))}
            </div>
        </div>
    );
}
