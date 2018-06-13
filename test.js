var twilio = require('twilio');
var accountSid = 'AC8dba9c453debf2a019e3525cbedc7c4e'; // Your Account SID from www.twilio.com/console
var authToken = '5ba6adc4f52b21f108d1310c65fe1a56';   // Your Auth Token from www.twilio.com/console

var twilio = require('twilio');
var client = new twilio(accountSid, authToken);

client.messages.create({
    body: 'Your appointment is approaching.',
    to: '+919664994910',  // Text this number
    from: '+12034242367' // From a valid Twilio number
})
.then((message) => console.log(message.sid));