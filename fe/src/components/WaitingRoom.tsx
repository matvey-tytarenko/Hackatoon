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
    alert("Accept Call");
    navigate('/chat')
  };

  return (
    <div
      className=" relative bg-cover bg-center bg-no-repeat"
      style={{
        backgroundImage:
          'url("https://media.discordapp.net/attachments/1289511299524329562/1289570599433404449/file-iEJAuYeUxGs9xNt8zOj12OUw.png?ex=66f94db5&is=66f7fc35&hm=8adac9cf62a3ec586549ebf69f37f9dd9f804e8d0b8d937dc6ab43257b24387d&=&format=webp&quality=lossless&width=905&height=905")',
        width: "1024px",
        height: "768px",
      }}
    >
      <Button
        className="w-16 h-16 text-lg font-medium bg-transparent border-black hover:bg-transparent hover:border-lime-100"
        onClick={() => acceptCall()}
        style={{
          borderRadius: "50%",
          position: "absolute",
          top: "605px",
          left: "410px",
        }}
      ></Button>
      <Button
        className="w-16 h-16 text-lg font-medium bg-transparent border-black hover:bg-transparent hover:border-lime-100"
        onClick={() => declineCall()}
        style={{
          borderRadius: "50%",
          position: "absolute",
          top: "605px",
          left: "545px",
        }}
      ></Button>
    </div>
  );
}

export default WaitingRoom;
