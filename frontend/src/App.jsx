import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [products, setProducts] = useState([])

  useEffect(() => {
    fetch('http://localhost:8000/api/products')
      .then(response => response.json())
      .then(data => setProducts(data))
  }, [])

  return (
    <div className="catalog-container">
      <h1>Vitrine FitHub 💪</h1>
      <p>Equipamentos de alta performance para o seu treino.</p>
      
      <div className="product-grid">
        {products.map(product => (
          <div key={product.id} className="product-card">
            <h2 className='product-name'>{product.name}</h2>
            <p>{product.description}</p>
            <p className="product-price">R$ {product.price.toFixed(2)}</p>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App