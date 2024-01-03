import React from "react";
import "./Tile.css";

// Functional Component
const Tile = ({ value }) => {
  // Your component logic goes here
  return <div className="tile">{value}</div>;
};

export default Tile;
