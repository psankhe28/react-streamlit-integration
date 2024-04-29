import React from 'react';
import './App.css';

const App = () => {
    return (
        <div className="documentation-container">
            <h2>Normal Distribution</h2>
            <p>
                The normal distribution, also known as the Gaussian distribution, is a continuous probability distribution that is symmetric about the mean.
            </p>
            <h2>Binomial Distribution</h2>
            <p>
                The binomial distribution describes the number of successes in a fixed number of independent Bernoulli trials.
            </p>
            <div className="streamlit-container">
                <iframe
                    src="http://localhost:8501/?embed=true"
                    title='streamlit'
                    height='1000'
                    style={{ width: '80%', backgroundColor: 'white' }}
                ></iframe>

            </div>
        </div>
    );
}

export default App;