"'use client'";

import { Button } from "../components/ui/button";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../service/API.ts";
import axios from "axios";

export function Page() {
  const navigate = useNavigate();

  const [session, setSession] = useState(1);

  const sendData = () => {
    const payload = { name: "React" };
    axios
      .post("http://localhost:5000/api/data")
      .then((response) => {
        console.log("Response from server:", response.data);
      })
      .catch((error) => {
        console.error("Error sending data:", error);
      });
  };

  const createTicket = async () => {
    const API = api();
    const data = await sendData();
    console.log(data);
    const ticket = await API.createSession();
    setSession(ticket);
    alert(session);
    navigate("/waiting");
  };
  return (
    <div
      className=" relative bg-cover bg-center bg-no-repeat"
      style={{
        backgroundImage:
          'url("https://media.discordapp.net/attachments/1289511299524329562/1289570914035568641/file-1CKpvn1BIfM9jmHN4mB5qvD3.png?ex=66f94e00&is=66f7fc80&hm=1d773f44292d4f6aaeee38c960943b4cd7a2c4d4c493df18623fa899bc3fe468&=&format=webp&quality=lossless&width=905&height=905")',
        width: "1024px",
        height: "768px",
      }}
    >
      <div
        className="absolute bottom-28"
        style={{
          right: "538px",
        }}
      >
        <Button
          className="w-16 h-16 text-lg font-medium bg-transparent border-black hover:bg-transparent hover:border-lime-100"
          onClick={createTicket}
          style={{ borderRadius: "50%" }}
        ></Button>
      </div>
    </div>
  );
}
