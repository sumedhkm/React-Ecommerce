import React, { useContext } from 'react';
import { useParams } from 'react-router-dom';
import { ShopContext } from './ShopContext';
import BreadCrum from './BreadCrum/BreadCrum';
import ProductDisplay from './ProductDisplay/ProductDisplay';

const Product = () => {
  const { all_product } = useContext(ShopContext);
  const { productId } = useParams();
  const product = all_product.find((e) => e.id === Number(productId));
  
  return (
    <div>
      <BreadCrum product={product} />
      <ProductDisplay  product={product}/>
    </div>
  );
};

export default Product;
