function preLoad(){
	nameimages = new Array('nimage0','nimage1','nimage2','nimage3','nimagen');
	images = {};
	loadAllImages();
	function loadAllImages(){
		for (name in nameimages){
			images[nameimages[name]] = new Image();
			images[nameimages[name]].onload = function() { 
									resourceLoaded();
									}
			images[nameimages[name]].src = "images/" + nameimages[name] + ".png";
		}
	}
	var totalResources = nameimages.length;
	var numResourcesLoaded = 0;
	function resourceLoaded() {
	  numResourcesLoaded += 1;
	  if(numResourcesLoaded === totalResources) {
		main();
	  }
	}
}