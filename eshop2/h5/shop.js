

// localStorage.setItem("token", "d49c32c8f0ff16dceae60e57c5356245b9c73313");


function myheader(){
	return {Authorization: 'Token ' + localStorage.getItem("token")};
};
