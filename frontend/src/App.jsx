import { useState, useEffect } from 'react';

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Aponta para a porta padrão do container backend
    fetch('http://localhost:8000/api/products')
      .then((res) => res.json())
      .then((data) => {
        setProducts(data);
        setLoading(false);
      })
      .catch((err) => {
        print("Erro ao buscar produtos:", err);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <header style={{ borderBottom: '2px solid #333', paddingBottom: '10px', marginBottom: '20px' }}>
        <h1 style={{ color: '#e63946' }}>FitHub 💪</h1>
        <p>Acessórios de Alto Desempenho para o seu Treino</p>
      </header>

      {loading ? (
        <p>Carregando produtos...</p>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
          {products.map((product) => (
            <div key={product.id} style={{ border: '1px solid #ddd', padding: '15px', borderRadius: '8px', backgroundColor: '#f9f9f9' }}>
              <span style={{ fontSize: '12px', color: '#666', textTransform: 'uppercase' }}>{product.category}</span>
              <h3 style={{ margin: '5px 0' }}>{product.name}</h3>
              <p style={{ fontWeight: 'bold', color: '#1d3557' }}>R$ {product.price.toFixed(2)}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;