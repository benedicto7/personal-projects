import React, { useState } from 'react'
import "./Search.css"

/* 
    Improvements:
    -print output nicely
*/

function Search() {
    // Turn the keys into an array
    let keys = Object.keys(localStorage);

    // Total number of keys
    let count = localStorage.length; 

    let student_to_be_removed = null;

    // Keeps in check what the user inputs
    const [search, setSearch] = useState("");

    // Finds and check if the data the user inputted is in local storage 
    const Find = () => {
        let initial = 0;
        while (initial < count) {
            if (search == keys[initial]) {
                student_to_be_removed = search;

                // Receives the data and turns it into an object
                const get = JSON.parse(localStorage.getItem(search));

                // Turns the object into a string
                const output = JSON.stringify(get, null, 2);

                // alert(output);

                // Pretty-Print
                const final = output.split(", ").join('\n')
            
                return final;
            }
            ++initial;
        }
    }

    // Keeps calling the function
    let found = Find();

    // Remove student from data when user clicks remove button
    const remove_student = () => {
        if (found != "") {
            // Remove data from local storage
            localStorage.removeItem(student_to_be_removed);

            // Sets output to blank
            document.getElementById("found").innerHTML = "";
        }
    }

    // Remove all student from data when user clicks remove button
    const remove_all = () => {
        localStorage.clear();
    }

    return (
        <div>
            <div className='searchstudent'>
                <h1><b>Search Student ID</b></h1>

                <form onSubmit={Find} >
                <input type="search" placeholder='2608580' id='search' onChange={(event) => setSearch(event.target.value)}/>
                </form>
                
                <p id='found'>{found}</p>
                <button onClick={remove_student}>Remove Student</button>

                <br />

                <button onClick={remove_all}>Remove All Data</button>
            </div>    
        </div>
    )
}

export default Search