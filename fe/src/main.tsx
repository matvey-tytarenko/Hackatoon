import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'
import Chat from './components/Chat.tsx'
import WaitingRoom from './components/WaitingRoom.tsx'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './index.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
     <Routes>
      <Route path='/' element={<App />} />
      <Route path=':ticketorder' element={<Chat />} />
      <Route path='/waiting' element={<WaitingRoom />} />
     </Routes>
    </BrowserRouter>
  </StrictMode>,
)
