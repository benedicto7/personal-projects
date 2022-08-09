import React, { useEffect, useState } from 'react'
import "./Timer.css"

function Timer() {
  // Initialize hour, minute, second, and timer
  const [hour, setHour] = useState(0);
  const [minute, setMinute] = useState(0);
  const [second, setSecond] = useState(0);
  const [timer, setTimer] = useState(false);

  // Set the max value allowed for hour, minute, second
  if (second > 59) {
    setSecond(59);
  }
  if (minute > 59) {
    setMinute(59);
  }
  if (hour > 24) {
    setHour(24);
  }

  // Countdown
  let total = second + minute + hour;
  useEffect(() => {
    // Starts countdowns when start button pressed
    if (timer) {
      var countdown = setInterval(() => {
        // Stops countdown when timer reaches 0
        if ((second <= 0) && (minute <= 0) && (hour <= 0)) {
          clearInterval(countdown);
          setTimer(false);
          alert("Time's Up!");
        }
        else { 
          // Count down by 1 every second
          setSecond((prevCount) => prevCount - 1);

          // Updates the second, minute, and hour accordingly when second reaches 0
          if ((second <= 0) && (minute > 0)) {
            setSecond(59);
            setMinute((prevCount) => prevCount - 1);
          }
          if ((second <= 0) && (minute <= 0) && (hour > 0)) {
            setSecond(59);
            setMinute(59);
            setHour((prevCount) => prevCount - 1);
          }
        }
      }, 1000); 
    }
    
    // Stops countdown when stop button pressed
    else {
      clearInterval(countdown);
    }

    return () => clearInterval(countdown); // ???
  }, [timer, hour, minute, second]) // At every render/events, updates the timer, hour, minute, and second variables accordingly
  
  // Initialize start button state
  const [start, setStart] = useState(false);
  
  // Initialize stop button state
  const [stop, setStop] = useState(true);

  // Initialize increment and decrement state
  const [operator, setOperator] = useState(false)

  // Checks if timer is 1 or 2 digits
  let s;
  let m;
  let h;
  if (second < 10) {
    s = "0" + second;
  }
  else {
    s = second;
  }

  if (minute < 10) {
    m = "0" + minute;
  }
  else {
    m = minute;
  }

  if (hour < 10) {
    h = "0" + hour;
  }
  else {
    h = hour;
  }

  return (
    <div>
          <div className='Timer'>
            <section className='timerSection'> 
              <button className='increment' disabled = {operator} onClick = {() => setHour((prevCount) => prevCount + 1)}><b>+</b></button>
              <button className='decrement' disabled = {operator} onClick = {() => setHour((prevCount) => prevCount - 1)}><b>-</b></button>

              <p><b>{h}</b></p>
              <p><b>Hours</b></p>
            </section>

            <section className='timerSection'>
              <button className='increment' disabled = {operator} onClick = {() => setMinute((prevCount) => prevCount + 2)}><b>+</b></button>
              <button className='decrement' disabled = {operator} onClick = {() => setMinute((prevCount) => prevCount - 2)}><b>-</b></button>

              <p><b>{m}</b></p>
              <p><b>Minutes</b></p>
            </section>
            
            <section className='timerSection'>
              <button className='increment' disabled = {operator} onClick = {() => setSecond((prevCount) => prevCount + 5)}><b>+</b></button>
              <button className='decrement' disabled = {operator} onClick = {() => setSecond((prevCount) => prevCount - 5)}><b>-</b></button>

              <p><b>{s}</b></p>
              <p><b>Seconds</b></p>
            </section>
          </div>

          <div>
            <button disabled = {start} onClick={() => {setTimer(true); setStart(true); setStop(false); setOperator(true)}}><b>Start</b></button> 
            <button disabled = {stop} onClick={() => {setTimer(false); setStart(false); setStop(true); setOperator(false)}}><b>Stop</b></button> 
            <button onClick = {
              () => {setHour(0); 
                    setMinute(0); 
                    setSecond(0);
                    setTimer(false);
              }
            }><b>Reset</b></button>
          </div>

          <div id="endTimer">
            {(total <= 0) ? "Time's Up!" : "Into the abyss..."}
          </div>
    </div>
  )
}

export default Timer