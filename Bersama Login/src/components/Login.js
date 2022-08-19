import { useEffect, useState } from 'react'
import "./Login.css"

/* 
  Improvements:
  -write data into txt file  
  -connect to other network/ip address
*/

function Login() {
  const [id, setID] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [birthday, setBirthday] = useState("")
  const [gender, setGender] = useState("")
  const [nationality, setNationality] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [major, setMajor] = useState("");
  const [food, setFood] = useState("");
  const [sport, setSport] = useState("");
    
  const Submit = () => {
    // Compile and turn what user has submitted into an object
    const person = {first_name: firstName, 
                    last_name: lastName,
                    birthday: birthday,
                    gender: gender,
                    nationality: nationality,  
                    email: email,
                    phone_number: phone,
                    major: major,
                    favourite_food: food,
                    favourite_sport: sport                
    }; 

    // Add object into the local storage
    localStorage.setItem(id, JSON.stringify(person));
  }

  return (
    <div className='page'>
      <div className="login">
        <div className='logintitle'>
          <h1><b>Sign In</b></h1>
          &#160;&#160;
          <h1 id='bersama'><b>Bersama</b></h1>
        </div>

        <form onSubmit={Submit}>
          <label htmlFor="">Student ID: </label>
          <input type="number" placeholder='2608580' value={id} onChange={(event) => setID(event.target.value)} required/>
          <br />

          <label htmlFor="">First Name: </label>
          <input type="text" placeholder='Benedicto' onChange={(event) => setFirstName(event.target.value)} required/>
          <br />

          <label htmlFor="">Last Name: </label>
          <input type="text" placeholder='Elpidius' onChange={(event) => setLastName(event.target.value)}/>
          <br />

          <label htmlFor="">Birthday: </label>
          <input type="date" onChange={(event) => setBirthday(event.target.value)} required/>
          <br />
          
          <label htmlFor="">Gender: </label>
          <input type="radio" value="Male" name='gender' checked onChange={(event) => setGender(event.target.value)}/>
          <label htmlFor="">Male</label>
          <input type="radio" value="Female" name='gender' onChange={(event) => setGender(event.target.value)}/>
          <label htmlFor="">Female</label>
          <br />
          
          <label htmlFor="">Nationality: </label>
          <input type="text" placeholder='Indonesian' onChange={(event) => setNationality(event.target.value)} required/>
          <br />
          
          <label htmlFor="">Email: </label>
          <input type="email" placeholder='bee6@calvin.edu' onChange={(event) => setEmail(event.target.value)} required/>
          <br />
          
          <label htmlFor="">Phone Number: </label>
          <input type="number" placeholder='6168566397' onChange={(event) => setPhone(event.target.value)} required/>
          <br />
          
          <label htmlFor="">Major: </label>
          <input type="text" placeholder='Computer Science' onChange={(event) => setMajor(event.target.value)}/>
          <br />
          
          <label htmlFor="">Favourite Foods: </label>
          <input type="text" placeholder='Kwetiau Goreng' onChange={(event) => setFood(event.target.value)} required/>
          <br />
          
          <label htmlFor="">Favourite Sports: </label>
          <input type="text" placeholder='Basketball' onChange={(event) => (setSport(event.target.value))} required/>
          <br />
          
          <input type="submit" value="Submit"/>            
        </form>
      </div>  
    </div>
  )
}

export default Login
