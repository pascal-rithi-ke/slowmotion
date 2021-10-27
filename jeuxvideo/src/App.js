import './App.css';
import React,{useState} from 'react';
import axios from "axios";
import { useEffect } from 'react/cjs/react.development';



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
      <>
      {jv ? 
          jv.map(jv => {
              return(
                 <div className="jv" key={jv._id.$oid.toString()}>
                   <h3>{jv.name}</h3>
                   <p>{jv.note}</p>
                 </div>
              )
          }) : <h3>No data yet</h3> }
      </>
  );
}

export default App;
