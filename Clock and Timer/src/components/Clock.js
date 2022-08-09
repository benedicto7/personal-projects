import React, { useEffect, useState } from 'react'
import "./Clock.css"

function Clock() {
    // Initialize for year, month, day format
    const monthNames = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"];
    const [date, setDate] = useState();
    
    // Initialize the weeks
    const weekNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const [week, setWeek] = useState();

    // Initialize clock
    const [clock, setClock] = useState();

    /* 
    Every second, the clock variable gets updated and rendered with
    the realtime using new Date(). Then gets initialized to clock everytime 
    with setClock(), using useState().

    Still builts correctly without useEffect().
    */
    useEffect(() => {
        setInterval(() => {
            const date = new Date();

            // Weekday/Weekend
            let week = date.getDay();
            let today_week = weekNames[week];

            setWeek(today_week);

            // Date format
            let year = date.getFullYear();
            let date_number = date.getDate();
            let month = date.getMonth();
            let today_month = monthNames[month];

            let date_format = today_month + " " + date_number + ", " + year;
            setDate(date_format);

            // Time
            let hour = date.getHours();
            let minute = date.getMinutes();
            let second = date.getSeconds();
            let session = "AM";

            // 12h format
            if (hour === 0) {
                hour = 12;
            }
            if (hour > 12) {
                hour = hour - 12;
                session = "PM";
            }

            // Checks if the clock is 1 or 2 digit
            if (hour < 10) {
                hour = "0" + hour;
            }
            else {
                hour = hour;
            }

            if (minute < 10) {
                minute = "0" + minute;
            }
            else {
                minute = minute;
            }

            if (second < 10) {
                second = "0" + second;
            }
            else {
                second = second;
            }
            
            let time = hour + " : " + minute + " : " + second + " " + session;
            setClock(time);
            
            // 24h format
            //setClock(date.toLocaleTimeString());
        }, 1000); // 1 second
    }, [monthNames, weekNames]) // []
    
    return (
    <div>
        <div id='date'>
            <b>
             {week + ", " + date}
            </b>
        </div>
        <div id='clock'>
            <b>
                {clock}
            </b>
        </div>      
    </div>
    )
}

export default Clock