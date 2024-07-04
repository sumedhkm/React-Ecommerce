import React from 'react';
import './Popular.css';
import data_product from '../Assets/data';
import Item from '../Item/Item';  // Ensure the correct relative path to Item.js

const Popular = () => {
  return (
    <div className='popular'>
      <h1>POPULAR IN WOMAN</h1>
      <hr />
      <div className='popular-item'>
        {data_product.map((item) => (
          <Item
            key={item.id}
            id={item.id}
            name={item.name}  // Pass the name to Item component
            image={item.image}
            new_price={item.new_price}
            old_price={item.old_price}
          />
        ))}
      </div>
    </div>
  );
};

export default Popular;
