import { useRef } from "react";
import "./App.css";

function App() {
  // Create file input file
  const SelectFile = useRef(null);

  // Обработчик клика по иконке
  const handleRef = () => {
    // Триггерим клик по скрытому input через реф
    SelectFile.current.click();
  };

  return (
    <>
      <div className="container">
        <div className="side_history">
          <a href="#" className="new">
            {/* Иконка, которая вызывает открытие окна выбора файла */}
            <i className="fas fa-marker" onClick={handleRef}></i>
          </a>
        </div>
        <div className="title">
          <h1>Nazwa</h1>
        </div>
        <div className="logo"></div>
        <div className="prompts">
          <input type="text" placeholder="Message Nazwa" />

          {/* Скрытый input для выбора файла */}
          <input
            type="file"
            id="file"
            className="file"
            ref={SelectFile} // Привязываем реф
            style={{ display: "none" }} // Скрываем элемент
          />
        </div>
      </div>
    </>
  );
}

export default App;
