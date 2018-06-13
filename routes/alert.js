var express = require('express');
var router = express.Router();
var Patient = require('../models/alert');
var PythonShell = require('python-shell');


router.get('/form5', ensureAuthenticated, function(req, res){
	res.render('form5');
});

router.get('/wresult',ensureAuthenticated, function(req, res){
	res.render('wresult');
});


function ensureAuthenticated(req, res, next){
	if(req.isAuthenticated()){
		return next();
	} else {
		req.flash('error_msg','You are not logged in');
		res.redirect('/users/login');
	}
}

router.post('/form5', function(req, res){
	
	
	var nodemailer = require('nodemailer');

	var transporter = nodemailer.createTransport({
	service: 'gmail',
	auth: {
    user: 'pratikmobile0@gmail.com',
    pass: 'richardcastle'
	}
	});

	var mailOptions = {
	from: 'pratikmobile0@gmail.com',
	to: 'nichatpratik@gmail.com',
	subject: 'Appointment Scheduled at 10 AM ON 17 March 2018',
	text: 'Please be ready with your reports and be on time.'
	};

	transporter.sendMail(mailOptions, function(error, info){
	if (error) {
    console.log(error);
	} else {
    console.log('Email sent: ' + info.response);
	}
});
	
	var errors = req.validationErrors();

	if(errors){
		res.render('form5',{
			errors:errors
		});
	}else{ 
		req.flash('success_msg', 'Message Sent Successfully');
		res.redirect('/users/dashboard');
	}
	
});

module.exports = router;