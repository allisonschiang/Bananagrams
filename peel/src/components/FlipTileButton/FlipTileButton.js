import Tile from "../Tile/Tile";
import { useState } from "react";

const FlipTileButton = ({ onTileFlip }) => {
  return <button onClick={onTileFlip}>Flip Tile</button>;
};

export default FlipTileButton;
