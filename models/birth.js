var mongoose = require('mongoose');

var BirthSchema = mongoose.Schema({
	pid: {
		type: String,
		index:true
	},
	age: {
		type: Number
	},
	weight_mother: {
		type: Number
	},
	smoke_status: {
		type: Number
	},
	hist_premature_labor: {
		type: Number
	},
	history_hypertension: {
		type: Number
	},
	uterine_irritability: {
		type: Number
	},
});

var Birth = module.exports = mongoose.model('Birth', BirthSchema);
