//Import React Class
import React from 'react';

//Import Stylesheet
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

//Importing Components
import Particles from 'react-particles-js';
import MainApp from './Components/MainApp';

//Globals
const ParticleOptions = {
  particles: {
    color: {
      // value: "#0970D4"
      value: "#000000"
    },
    line_linked: {
      color: {
        // value: "#0970D4"
        value: "#000000"
      }
    },
    number: {
      value: 150
    },
    size: {
      value: 1
    }
  },
  interactivity: {
    events: {
        onhover: {
            enable: true,
            mode: "repulse"
        }
    }
}
}

function App() {
  return (
    <div className="App">
      <Particles params={ParticleOptions} className="Particles" />
      <MainApp />
    </div>
  );
}


export default App;
