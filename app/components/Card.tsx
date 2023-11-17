"use client";
import React from "react";
import { CodeData } from "./CodeData";

const Card = ({ id, name, code, language, difficulty }: CodeData) => {
    return (
        <div
            onClick={() => document.getElementById("codeModal")!.showModal()}
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
            <dialog id="codeModal" className="modal">
                <div className="modal-box">
                    <div className="mockup-code">
                        <pre>
                            <code>{code}</code>
                        </pre>
                    </div>
                </div>
                <form method="dialog" className="modal-backdrop">
                    <button>Close</button>
                </form>
            </dialog>
        </div>
    );
};

export default Card;
