import React from "react";
import { Button } from "./ui/button";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function WaitingRoom() {
  const navigate = useNavigate();

  const declineCall = () => {
    navigate("/");
  };
  const acceptCall = () => {
    navigate("/chat");
  };

  return (
    <div
      className="relative bg-cover bg-center bg-no-repeat m-auto w-60 h-20"
      style={{
        backgroundImage:
          'url("https://media.discordapp.net/attachments/1289511299524329562/1289570599433404449/file-iEJAuYeUxGs9xNt8zOj12OUw.png?ex=66f9f675&is=66f8a4f5&hm=e3a44143848033db0a4de8cd2bf9714e12bd62bb7786cad657125633564c7c90&=&format=webp&quality=lossless&width=905&height=905")',
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
          right: "550px",
          top: "560px",
        }}
      >
        <Button
          className="w-16 h-16 text-lg font-medium bg-transparent border-black hover:bg-transparent hover:border-lime-100"
          onClick={acceptCall}
          style={{ borderRadius: "50%" }}
        ></Button>
      </div>
      <div
        className="absolute bottom-28"
        style={{
          left: "545px",
          top: "560px",
        }}
      >
        <Button
          className="w-16 h-16 text-lg font-medium bg-transparent border-black hover:bg-transparent hover:border-lime-100"
          onClick={declineCall}
          style={{ borderRadius: "50%" }}
        ></Button>
      </div>
    </div>
  );
}

export default WaitingRoom;
