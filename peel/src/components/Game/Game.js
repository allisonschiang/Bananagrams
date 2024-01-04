import Tile from "../Tile/Tile";
import FlipTileButton from "../FlipTileButton/FlipTileButton";
import { useState, useEffect } from "react";

const Game = () => {
  const [tiles, addTile] = useState([]);

  var ws = null;
  var initialized = false;

  if (!initialized) {
    ws = new WebSocket("ws://localhost:8000/ws");
  }
  initialized = true;

  ws.onmessage = function(event) {
    let data = JSON.parse(event.data);
    if (data["action"]=="flip_tile"){
      const newTile = <Tile value={data["text"]} />;
      addTile((prevTiles) => [...prevTiles, newTile]);
    }

  };

  const flipTile = async () => {
    let data = {action: "flip_tile"}
    let json = JSON.stringify(data)
    ws.send(json)
  };

  return (
    <div className="game">
      {tiles}
      <FlipTileButton onTileFlip={flipTile} />
    </div>
  );
};

export default Game;
