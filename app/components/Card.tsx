"use client";
import React from "react";
import { CodeData } from "./CodeData";

const Card = ({ id, name, code, language, difficulty }: CodeData) => {
    return (
        <div
            onClick={() => document.getElementById("codeModal")!.showModal()}
            className="card card-compact w-96 bg-base-100 shadow-xl m-4"
            style={{ cursor: "pointer" }}
        >
            <div className="card-body">
                <h2 className="card-title">
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
