"'use client'"

import { useState } from "react"
import { Button } from "../components/ui/button"
import { Input } from "../components/ui/input";
import { ScrollArea } from "../components/ui/scroll-area";
import { Avatar, AvatarFallback, AvatarImage } from "../components/ui/avatar";

function Page() {
  const [messages, setMessages] = useState([
    { id: 1, text: "Hello! How can I help you today?", sender: "bot" },
    { id: 2, text: "I have a question about React hooks.", sender: "user" },
    { id: 3, text: "Sure, I'd be happy to help. What specifically would you like know about React hooks?", sender: "bot" },
  ])
  const [newMessage, setNewMessage] = useState("")

  const handleSendMessage = () => {
    if (newMessage.trim()) {
      setMessages([...messages, { id: messages.length + 1, text: newMessage, sender: "user" }])
      setNewMessage("")
      // Here you would typically send the message to a backend service
      // and then add the response to the messages array
    }
  }

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <header className="bg-white shadow-sm py-4 px-6">
        <h1 className="text-2xl font-bold text-gray-800">Chat App</h1>
      </header>
      <ScrollArea className="flex-grow p-6">
        {messages.map((message) => (
          <div key={message.id} className={`flex ${message.sender === "'user'" ? "'justify-end'" : "'justify-start'"} mb-4 text-black`}>
            <div className={`flex items-start ${message.sender === "'user'" ? "'flex-row-reverse'" : "'flex-row'"}`}>
              <Avatar className="w-8 h-8">
                <AvatarImage src={message.sender === "'user'" ? "/placeholder.svg?height=32&width=32" : "/placeholder.svg?height=32&width=32&text=Bot"} />
                <AvatarFallback>{message.sender === "'user'" ? "'U'" : "'B'"}</AvatarFallback>
              </Avatar>
              <div className={`mx-2 p-3 rounded-lg ${message.sender === "'user'" ? "'bg-blue-500 text-white'" : "'bg-white' text-black"}`}>
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
            onKeyPress={(e) => e.key === "'Enter'" && handleSendMessage()}
            style={{
              color: 'black'
            }}
          />
          <Button onClick={handleSendMessage}>Send</Button>
        </div>
      </div>
    </div>
  )
}

export default Page;