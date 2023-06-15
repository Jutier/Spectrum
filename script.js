function Log(){
	let Target = parseFloat(document.getElementById("Target").value);
	let Projectile = parseFloat(document.querySelector('input[name="Projectile"]:checked').value);
	let Angle = Math.PI*(document.getElementById('range').value/180)
	let K = ((Math.sqrt((Target**2)-((Projectile**2)*Math.sin(Angle))) + (Projectile*Math.cos(Angle)))/(Target + Projectile))**2
	console.log(K)
	factorK.innerHTML = `<p>${K}</p>`;


}




// Slider
const
	range = document.getElementById('range'),
	rangeV = document.getElementById('rangeV'),
	setValue = ()=>{
		const
			newValue = Number( (range.value - range.min) * 100 / (range.max - range.min) ),
			newPosition = 10 - (newValue * 0.2);
		rangeV.innerHTML = `<span>${range.value}</span>`;
		rangeV.style.left = `calc(${newValue}% + (${newPosition}px))`;
	};
document.addEventListener("DOMContentLoaded", setValue);
range.addEventListener('input', setValue);
//

// Mass table

let ElementMass = {
	"H" : 1,
	"He" : 4,
	"Li" : 7,
	"Be" : 9,
	"B" : 11,
	"C" : 12,
	"N" : 14,
	"O" : 16,
	"F" : 19,
	"Ne" : 20,
	"Na" : 23,
	"Mg" : 24,
	"Al" : 27,
	"Si" : 28
}