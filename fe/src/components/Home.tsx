"use client";

import axios from "axios";

import { Button } from "../components/ui/button";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "../service/API.ts";
import basia from '../assets/basia.png'

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
        backgroundImage:
          'url("https://media.discordapp.net/attachments/1289511299524329562/1289570914035568641/file-1CKpvn1BIfM9jmHN4mB5qvD3.png?ex=66f9f6c0&is=66f8a540&hm=2939357c4f185ccaed92b2ddd7f87aa91fd7ddedf92e10da4edc1ce018e5f4dc&=&format=webp&quality=lossless&width=905&height=905")',
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
