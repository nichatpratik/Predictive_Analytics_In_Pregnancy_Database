var mongoose = require('mongoose');

var AlertSchema = mongoose.Schema({
	pid: {
		type: String,
		index:true
	},
	contact: {
		type: Number
	},
	
});

var alert = module.exports = mongoose.model('alert', AlertSchema);
