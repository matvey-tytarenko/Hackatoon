import React from "react";
import { Button } from "./ui/button";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import background from "../assets/phone.png";

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
        backgroundImage: `url(${background})`,
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
