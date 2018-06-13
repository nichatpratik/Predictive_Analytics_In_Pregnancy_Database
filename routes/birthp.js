var express = require('express');
var router = express.Router();
var Patient = require('../models/patient');
var PythonShell = require('python-shell');


router.get('/form4', ensureAuthenticated, function(req, res){
	res.render('form4');
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

router.post('/form4', function(req, res){
	
	var pyshell = new PythonShell('routes/birth.py');
	var pid = req.body.pid;
	var age = req.body.age;
	var weight_mother = req.body.weight_mother;
	var smoke_status=req.body.smoke_status;
	var hist_premature_labor=req.body.hist_premature_labor;
	var history_hypertension=req.body.history_hypertension;
	var uterine_irritability=req.body.uterine_irritability;
	

	// Validation
	req.checkBody('pid', 'Patient Id is required').notEmpty();

	var errors = req.validationErrors();

	if(errors){
		res.render('form4',{
			errors:errors
		});
	}else{ 
		
		Patient.getPatientByPid(pid, function(err, patient){
			if(err) throw err;
			if(patient){
				
				var dataString = '';
				
				pyshell.send(JSON.stringify([age,weight_mother,smoke_status,hist_premature_labor,history_hypertension,uterine_irritability]));
				
				pyshell.on('message', function (message) {
					dataString += message.toString();
				});
				
				pyshell.end(function (err) {
					if (err){
						throw err;
					};
					req.flash('bw', dataString);
					res.redirect('/birthp/wresult');
				});
			}
			else{
				req.flash('error_msg', 'Unknown Patient Id');
				res.redirect('/birthp/form4');
			}
		});
	}
});

module.exports = router;