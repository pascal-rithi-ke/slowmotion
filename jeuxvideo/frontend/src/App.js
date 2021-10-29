import './App.css';
import React, { useState } from 'react';
import axios from 'axios';
import {useEffect} from 'react/cjs/react.development';

function App() {
  const apiURL = "http://localhost:5000/";
  const [jv,getJeuxVideo] = useState('');
  useEffect(() => {
      JeuxVideo();
  }, []);

  const JeuxVideo = () => { 
      axios.get(apiURL).then((res) =>  {
      const dataJeuxVideo = res.data.results;
      console.log(dataJeuxVideo);
      getJeuxVideo(dataJeuxVideo);
      })
  .catch(error => console.error(`Error:${error}`));
  }

    return (
      <div>
        <header>
          <h1>Slow Motion</h1>
        </header>
      <>
      <div className="contenu">
      {jv ? 
          jv.map(jv => {
              return( 

                <div className="jv" key={jv.id}>
                  <img className="jeux_img" src={jv.img} alt={jv.name}></img>
                   <h3>{jv.name}</h3>
                   <p className="jeux_genres">{jv.genres}</p>
                   <p>{jv.note}</p>
                   <button className="square">Info</button>
                </div>

              )
          }) : <h3>No data yet</h3> }
      </div>
      </>
      </div>
    );
}

export default App;