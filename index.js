/* eslint require-path-exists/exists: 0 */

/**
 * This is a small example app to turn off and on
 * the built-in LED of an arduino by data sent
 * from the browser with socket.io.
 */

'use strict';

// Initialize application constants
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const port = process.env.PORT || 3000;
const geo = require('geolib');

/* ===========================================
*
* Setup a simple server.
*
=========================================== */

app.get('/', (req, res) => {
  res.sendfile('index.html');
});

http.listen(port, () => {
  console.log(`listening on *:${port}`);
});

/* ===========================================
*
*  Socket.io stuff
*
=========================================== */

var spawn = require('child_process').spawn,
    py    = spawn('python', ['compute_center.py']);
var locations = [], i = 0;

io.on('connection', (socket) => {
  console.log('a user connected');
  /**
   * Socket listener to determine whether or not to send HIGH / LOW
   * values to Arduino.
   */
  socket.on('message', (msg) => {
    if (msg === 'middle-me') {
      middleMe();
    } else if (msg) {
      locations.push({id: i, latitude: msg.latitude, longitude: msg.longitude});
      i++;
    }
  });

  function sendClient(coordinates) {
    socket.emit('middle-found', coordinates);
  }

  function middleMe() {
    console.log(locations);
    var center = geo.getCenter(locations);
    console.log('The center: ', center);
    
    // // send to python script
    // py.stdout.on('data', function(data) {
    //   dataString += data.toString();
    // });

    // py.stdout.on('end', function() {
    //   console.log('Sum of numbers=',dataString);
    //   sendClient(dataString);
    // });

    // py.stdin.write(JSON.stringify(center));
    // py.stdin.end();
  }

});
