"use client";

import { useState } from "react";
import avatar from "../assets/basia.png";
import axios from "axios";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { ScrollArea } from "../components/ui/scroll-area";
import "./Chat.css";
import { Avatar, AvatarFallback, AvatarImage } from "../components/ui/avatar";
import API from "../service/API";

function ChatPage() {
  const [messages, setMessages] = useState([
    { id: 1, text: "Dzień dobry. W czym mogę pomóc?", sender: "bot" },
  ]);

  const [newMessage, setNewMessage] = useState("");

  const handleSendMessage = async () => {
    if (newMessage.trim()) {
      const updatedMessages = [
        ...messages,
        { id: messages.length + 1, text: newMessage, sender: "user" },
      ];
      setMessages(updatedMessages);
      setNewMessage(""); // Clear field

      try {
        const api = API();
        const answer = await api.askQuestion(newMessage.trim());

        const updatedMessages2 = [
          ...updatedMessages,
          { id: messages.length + 1, text: answer, sender: "bot" },
        ];
        setMessages(updatedMessages2);
      } catch (error) {
        console.error("Error:", error);
      }
    }
  };

  return (
    <>
      <div className="flex flex-col h-screen bg-gray-100">
        <header className="bg-white shadow-sm pb-4 px-6">
          <h1 className="title text-4xl font-bold text-gray-800 text-center">
            Chat App KASia AI Beta 0.1
          </h1>
          <div className="left">
            <img
              src="https://media.discordapp.net/attachments/1289511299524329562/1289832299965452319/godlo-i-flaga-polski-z-ustawy2.png?ex=66fa4170&is=66f8eff0&hm=b36342e383c08629fcc37be082f99e538ceb1391e6850bed4a2f45fa211533ca&=&format=webp&quality=lossless"
              alt=""
              className="w-40"
            />
          </div>
          <div className="right bottom-24">
            <img
              src="https://media.discordapp.net/attachments/1289511299524329562/1289858044456603731/Logo_HQ.png?ex=66fa596a&is=66f907ea&hm=a3adfa47b0769d9d04d626a789039f17f1cec80a955cfded2bbd70ec0388ce4f&=&format=webp&quality=lossless&width=905&height=905"
              alt=""
              className="w-28"
            />
          </div>
        </header>
        <ScrollArea className="flex-grow p-6">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`flex ${
                message.sender === "user" ? "justify-end" : "justify-start"
              } mb-4 text-black`}
            >
              <div
                className={`flex items-start ${
                  message.sender === "user" ? "flex-row-reverse" : "flex-row"
                }`}
              >
                <Avatar className="w-12 h-12">
                  <AvatarImage
                    src={
                      message.sender === "user"
                        ? "/placeholder.svg?height=32&width=32"
                        : "/placeholder.svg?height=32&width=32&text=Bot"
                    }
                  />
                  <AvatarFallback>
                    {message.sender === "user" ? (
                      <i className="fas fa-user user-icon"></i>
                    ) : (
                      <img
                        src={avatar}
                        alt="Avatar of Basia"
                        className="border-r-8"
                        onError={(e) => {
                          e.target.onerror = null; // Prevent infinite loop
                          e.target.src = "/assets/default-avatar.png"; // Путь к запасному изображению
                        }}
                      />
                    )}
                  </AvatarFallback>
                </Avatar>
                <div
                  className={`mx-2 p-3 rounded-lg ${
                    message.sender === "user"
                      ? "bg-blue-500 text-white"
                      : "bg-white text-black"
                  }`}
                >
                  {message.text}
                </div>
              </div>
            </div>
          ))}
        </ScrollArea>
        <div className="p-4 bg-white border-t">
          <div className="flex space-x-2">
            <Input
              type="text"
              placeholder="Type your message..."
              value={newMessage}
              onChange={(e) => setNewMessage(e.target.value)}
              onKeyPress={(e) => {
                // Check Enter key
                if (e.key === "Enter") {
                  handleSendMessage(); // Call Function for send message
                }
              }}
              style={{
                color: "black",
                width: "1024px",
              }}
            />
            <Button onClick={handleSendMessage}>
              <i className="fas fa-paper-plane" />
            </Button>
          </div>
        </div>
      </div>
    </>
  );
}

export default ChatPage;
