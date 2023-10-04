 // Function to update the displayed date and time
 function updateDateTime() {
    var currentDate = new Date();
    var dateOptions = { year: 'numeric', month: 'short', day: 'numeric' };
    var timeOptions = { hour: '2-digit', minute: '2-digit', hour12: true };

    var formattedDate = currentDate.toLocaleDateString(undefined, dateOptions);
    var formattedTime = currentDate.toLocaleTimeString(undefined, timeOptions);

    document.getElementById("date-time-now").innerHTML = formattedDate + " " + formattedTime;
}

// Update the date and time immediately
updateDateTime();

// Update the date and time every second (10000 milliseconds)
setInterval(updateDateTime, 10000);