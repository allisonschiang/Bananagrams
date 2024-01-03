import Tile from "../Tile/Tile"
import FlipTileButton from "../FlipTileButton/FlipTileButton";
import { useState } from "react";

const Game = () => {

    const [tiles, addTile]=useState([])

    const getTileValue = async() => {
        try{
            const response = fetch("http://localhost:8000/get_next_tile")
            if (!response.ok){
                throw new Error("Network error")
            }
            const text = await response.text()
            return text;
        }
        catch(error){
            console.error("fetch error",error)
        }
    }

    const flipTile = async () => {
        const value = await getTileValue();
        const newTile = <Tile value={value}/>
        addTile(prevTiles => [...prevTiles, newTile])
    }

    return (
        <div className="game">
            {tiles}
            <FlipTileButton onTileFlip={flipTile}/>
        </div>
    );
  };
  
  export default Game;