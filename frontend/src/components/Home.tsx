"use client";

import axios from "axios";

import { Button } from "../components/ui/button";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../service/API.ts";
import basia from '../assets/basia.png'
import background from "../assets/img.png";

export function Page() {
  const navigate = useNavigate();
  const [session, setSession] = useState(1);

  const createTicket = async () => {
    try {
      navigate("/waiting");
      const API = api();
      const ticket = await API.createSession();
      setSession(ticket);
      alert(ticket);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div
      className="relative bg-cover bg-center bg-no-repeat m-auto w-60 h-20"
      style={{
        backgroundImage:`url(${background})`,
        width: "100%",
        maxWidth: "1024px",
        height: "678px",
        position: "absolute",
        margin: "auto",
        top: "250px",
        left: "255px",
      }}
    >
      <div
        className="absolute bottom-28"
        style={{
          right: "540px",
          top: "548px",
        }}
      >
        <Button
          className="w-16 h-16 text-lg font-medium bg-transparent border-black hover:bg-transparent hover:border-lime-100"
          onClick={createTicket}
          style={{ borderRadius: "50%" }}
        ></Button>

        <div className="message-container absolute top-1920">
            <img
              src={basia}
              alt="avatar"
              className="avatar"
            />
            <div className="message-box">
              <p>Welcome</p>
            </div>
          </div>
        </div>
      </div>
  );
}
