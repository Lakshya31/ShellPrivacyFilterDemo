//Import React Class
import React from 'react';

//Import Stylesheet
import './App.css';

//Importing Components
import TextBox from './Components/TextBox'

function App() {
  return (
    <div className="App">
      <div className="UpperBlue"></div>
      <div className="Lower">
        <div className="LeftPane"></div>
        <TextBox/>
      </div>
    </div>
  );
}


export default App;
