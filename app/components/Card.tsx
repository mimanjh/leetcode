"use client";
import React from "react";
import { CodeData } from "./CodeData";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

const Card = ({ id, name, code, language, difficulty }: CodeData) => {
    const [modalId, setModalId] = React.useState(id.toString());

    return (
        <div
            onClick={() =>
                (
                    document.getElementById(modalId)! as HTMLDialogElement
                ).showModal()
            }
            className="card card-compact w-96 shadow-xl m-4 bg-red-50 text-black"
            style={{ cursor: "pointer" }}
        >
            <div className="card-body">
                <h2 className="card-title font-bold">
                    {id}: {name}
                </h2>
                <p>
                    {difficulty} | {language}
                </p>
            </div>
            <dialog id={modalId} className="modal">
                <div className="modal-box max-w-5xl">
                    <SyntaxHighlighter
                        language={language.toLowerCase()}
                        style={oneDark}
                    >
                        {code}
                    </SyntaxHighlighter>
                </div>
                <form method="dialog" className="modal-backdrop">
                    <button>Close</button>
                </form>
            </dialog>
        </div>
    );
};

export default Card;
